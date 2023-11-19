from typing import Optional

import motor  # doing this locally instead of in database.py for greater modularity
import datetime
import random

import discord
from discord import option, slash_command
from discord.ext import commands, tasks

from . import database as db
from . import config
from . import utils
from .stasilogging import *
from . import casemanager as cm



class Justice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.CaseManager.start()

    
    case_selection = {}
    
    def setActiveCase(self, member, case):
        self.case_selection[member.id] = case

    def getActiveCase(self, member) -> cm.Case:
        return self.case_selection[member.id] if member.id in self.case_selection else None

    async def active_case_options(ctx: discord.AutocompleteContext):
        return [f"{case}: {case.id}" for case in cm.ACTIVECASES]

    case = discord.SlashCommandGroup("case", "Basic case management commands")
    @case.command(name="select", description="Select a case as your active case.")
    async def select_case(self, ctx, case: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(active_case_options))):
        case = cm.getCaseByID(case.split(" ")[-1])
        if case is None:
            return await ctx.respond("Invalid case ID.", ephemeral=True)
        
        self.setActiveCase(ctx.author, case)
        return await ctx.respond(f"Selected case **{case}** (`{case.id}`) as your active case.", ephemeral=True)
    

    case = discord.SlashCommandGroup("case", "Basic case management commands")
    @case.command(name="info", description="Get information about a case.")
    async def case_info(self, ctx):
        case = self.getActiveCase(ctx.author)
        if case is None:
            return await ctx.respond("You do not have an active case.", ephemeral=True)
        embed=discord.Embed(title=str(case), description=str(case.id))
        embed.add_field(name="Filed Datetime", value=discord_dynamic_timestamp(case.created, 'F'), inline=False)
        embed.add_field(name="Filed Relative", value=discord_dynamic_timestamp(case.created, 'R'), inline=False)
        embed.add_field(name="Filed By", value=case.nameUserByID(case.plaintiff_id), inline=False)




    @slash_command(name='normalusername', description='Get a user\'s normal username.')
    @option("member", discord.Member, description="The member to get the normal username of.")
    async def normal_username(self, ctx, member: discord.Member):
        await ctx.respond(cm.Case.normalUsername(None, member), ephemeral=True)

    @slash_command(name='filetestcase', description='File a test case.')
    @option("member", discord.Member, description="The member to file a case against.")
    @option("reason", str, description="The reason for filing a case.")
    async def test_case(self, ctx, member: discord.Member, reason: str):
        await cm.Case().New(ctx.guild, self.bot, f"{cm.Case.normalUsername(None, ctx.author)} v. {cm.Case.normalUsername(None, member)}", reason, ctx.author, member, cm.WarningPenalty(cm.Case))

    # add option to report a user by right clicking a message
    @commands.message_command(name="Report Message to Server Staff")
    async def report_message(self, ctx, message: discord.Message):
        return await ctx.respond("This command is not yet implemented.", ephemeral=True)

    @commands.user_command(name="Report User to Server Staff")
    async def report_user(self, ctx, member: discord.Member):
        return await ctx.respond("This command is not yet implemented.", ephemeral=True)

    @tasks.loop(minutes=15)
    async def CaseManager(self):
        log("Justice", "CaseManager", "Doing Periodic Case Manager Loop")
        for case in cm.ACTIVECASES:
            await case.Tick()
        return

def setup(bot):
    bot.add_cog(Justice(bot))
