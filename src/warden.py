import discord
from . import database as db
from typing import *
import datetime
import random
from . import config
from .stasilogging import log
from . import utils

"""
This manages mutes.
When a "prisoner" is muted, their roles are saved, removed, and replaced with a "Prisoner" role.
A "warrant" is a separate order to mute the prisoner. They can be stacked on top of each other.

prisoner = {
    "_id": user.id,
    "roles": [role_id1, role_id2, role_id3],
    "committed": datetime,
    "warrants": {
        "_id": "asd9339dj",
        "category": "admin",
    }
}

- [ ] Handling when user leaves server
- [ ] Void warrants by ID
-  [ ] Fail gracefully if warrant doesn't exist
- [ ] Void warrants by category
- [ ] Void warrants by author
- [ ] Void warrants by prisoner
"""

PRISONERS: List["Warrant"] = []

class Warrant:
    def __init__(self):
        self._id = None
        self.category = None
        self.description = None
        self.author = None
        self.created = None
        self.started = None
        self.len_seconds = 0
        self.expires = None
        self.frozen = None
        self.no_enforce = None

    def status(self) -> str:
        if self.expires:
            time_left_seconds = (self.expires - datetime.datetime.now(datetime.timezone.utc)).total_seconds()
            return f"Active ({utils.seconds_to_time_long(time_left_seconds)} remaining)"
        elif self.len_seconds == -1:
            return "Active (indefinite)"
        elif self.len_seconds > 0:
            return f"Pending Sentence ({utils.seconds_to_time_long(self.len_seconds)})"
        elif self.frozen:
            return f"Frozen ({utils.seconds_to_time_long(self.len_seconds)} remaining)"

    def activate(self):
        self.started = datetime.datetime.now(datetime.timezone.utc)
        self.expires = self.started + datetime.timedelta(seconds=self.len_seconds)

    def deactivate(self):
        if self.expires:
            diff = self.expires - datetime.datetime.now(datetime.timezone.utc)
            self.len_seconds = diff.total_seconds()
            self.expires = None
        
    def freeze(self):
        self.deactivate()
        self.frozen = True

    def generateNewID(self):
        return f"{random.randint(1000,9999)}-{random.choice(utils.elements).title()}-{random.choice(utils.elements).title()}-{random.choice(utils.elements).title()}"

    def New(self, category: str, description: str, author: int, len_seconds: int) -> "Warrant":
        self._id = self.generateNewID()
        self.category = category
        self.description = description
        self.author = author
        self.created = datetime.datetime.now(datetime.timezone.utc)
        self.len_seconds = len_seconds
        log("justice", "warrant", f"New warrant: ({self._id})")
        return self
    
    def loadFromDict(self, data):
        self._id = data["_id"]
        self.category = data["category"]
        self.description = data["description"]
        self.author = data["author"]
        self.created = data["created"]
        self.started = data["started"]
        self.len_seconds = data["len_seconds"]
        self.expires = data["expires"]
        if self.expires:
            self.expires = self.expires.replace(tzinfo=datetime.timezone.utc)
        self.frozen = data["frozen"]
        self.no_enforce = data["no_enforce"]
        return self

class Prisoner:
    
    def __init__(self, guild):
        self.guild: discord.Guild = guild
        self._id = None
        self.roles = []
        self.committed = None
        self.warrants: List[Warrant] = []

    def New(self, user: discord.Member) -> "Prisoner":
        self._id = user.id
        log("justice", "prisoner", f"New prisoner: {utils.normalUsername(user)} ({user.id})")
        return self

    def prisoner(self) -> Optional[discord.Member]:
        return self.guild.get_member(self._id)

    async def book(self):  # takes their roles, memorizes time committed, and gives them the prisoner role
        if self.roles:
            return

        log("justice", "prisoner", f"Booking prisoner: {utils.normalUsername(self.prisoner())} ({self._id})")
        prisoner_role = self.guild.get_role(config.C["prison_role"])
        user = self.prisoner()
        if prisoner_role in user.roles:
            return
        self.roles = [role.id for role in user.roles]
        self.committed = datetime.datetime.now(datetime.timezone.utc)
        await user.edit(roles=[prisoner_role])

    async def release(self):  # gives them roles back and nothing more
        if not self.roles:
            return
        log("justice", "prisoner", f"Releasing prisoner: {utils.normalUsername(self.prisoner())} ({self._id})")
        user = self.prisoner()
        await user.edit(roles=[self.guild.get_role(role_id) for role_id in self.roles])
        self.roles = []

    def getNextWarrant(self) -> Optional[Warrant]:
        if not self.warrants:
            return None
        for warrant in self.warrants:
            if not warrant.expires:
                if not warrant.frozen and warrant.len_seconds != -1:  # stayed warrants are still served, they're just served out of prison
                    return warrant
            else:
                return None

    def canFree(self):  # whether or not the prisoner can have their roles back
        if not self.warrants:
            return True
        for warrant in self.warrants:
            if not warrant.frozen and not warrant.no_enforce:
                return False
        
    def canArchive(self):
        if self.warrants:
            return False
        if self.roles:
            return False
        return True

    def loadFromDict(self, data):
        self._id = data["_id"]
        self.roles = data["roles"]
        self.committed = data["committed"]
        self.warrants = [Warrant().loadFromDict(warrant) for warrant in data["warrants"]]
        log("justice", "prisoner", f"Loaded prisoner: {utils.normalUsername(self.prisoner())} ({self._id})")
        return

    async def Archive(self):
        log("justice", "prisoner", f"Archiving prisoner: {utils.normalUsername(self.prisoner())} ({self._id})")
        db_ = await db.create_connection("Warden")
        grab = await db_.delete_one({"_id": self._id})
        PRISONERS.remove(self)

    async def Save(self):
        db_ = await db.create_connection("Warden")
        save = self.__dict__.copy()
        save["warrants"] = [warrant.__dict__ for warrant in save["warrants"]]
        save["guild"] = save["guild"].id
        await db_.update_one({"_id": self._id}, {"$set": save}, upsert=True)

    async def Tick(self):
        await self.HeartBeat()
        if not self.canArchive():
            await self.Save()

    async def HeartBeat(self):
        
        for warrant in self.warrants:
            if warrant.expires and datetime.datetime.now(datetime.timezone.utc) > warrant.expires:
                self.warrants.remove(warrant)
                log("justice", "warrant", f"Warrant expired: {utils.normalUsername(self.prisoner())} ({warrant._id})")
        
        if nxt := self.getNextWarrant():
            nxt.activate()
            log("justice", "warrant", f"Warrant activated: {utils.normalUsername(self.prisoner())} ({nxt._id})")
        
        if self.canFree():
            await self.release()
        else:
            await self.book()

        if self.canArchive():
            await self.Archive()

async def populatePrisoners(guild: discord.Guild):
    db_ = await db.create_connection("Warden")
    prisoners = await db_.find({}).to_list(length=None)
    for prisoner in prisoners:
        p = Prisoner(guild)
        p.loadFromDict(prisoner)
        PRISONERS.append(p)

def voidWarrantByID(warrant_id: str):
    for prisoner in PRISONERS:
        for warrant in prisoner.warrants:
            if warrant._id == warrant_id:
                prisoner.warrants.remove(warrant)
                log("justice", "warrant", f"Warrant voided: {utils.normalUsername(prisoner.prisoner())} ({warrant._id})")
                return

def getWarrantByID(warrant_id: str) -> Optional[Warrant]:
    for prisoner in PRISONERS:
        for warrant in prisoner.warrants:
            if warrant._id == warrant_id:
                return warrant

def getPrisonerByWarrantID(warrant_id: str) -> Optional[Prisoner]:
    for prisoner in PRISONERS:
        for warrant in prisoner.warrants:
            if warrant._id == warrant_id:
                return prisoner

def getPrisonerByID(user_id: int) -> Optional[Prisoner]:
    for prisoner in PRISONERS:
        if prisoner._id == user_id:
            return prisoner

async def newWarrant(target: discord.Member, category: str, description: str, author: int, len_seconds: int) -> Warrant:
    warrant = Warrant().New(category, description, author, len_seconds)
    if prisoner := getPrisonerByID(target.id):
        prisoner.warrants.append(warrant)
        await prisoner.Tick()
        return warrant
    else:
        prisoner = Prisoner(target.guild).New(target)
        prisoner.warrants.append(warrant)
        PRISONERS.append(prisoner)
        await prisoner.Tick()
        return warrant