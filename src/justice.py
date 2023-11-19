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
    
    # TODO: Confirmation message
    @case.command(name="statement", description="Make a statement in your active case.")
    async def statement(self, ctx, statement: str):
        case = self.getActiveCase(ctx.author)
        if case is None:
            return await ctx.respond("You do not have an active case.", ephemeral=True)
        # TODO: check if user is actually involved in case before allowing them to make a statement
        await case.personalStatement(ctx.author, statement)
        await ctx.respond("Statement added.", ephemeral=True)

    @case.command(name="info", description="Get information about a case.")
    async def case_info(self, ctx, ephemeral: bool = True):
        case = self.getActiveCase(ctx.author)
        if case is None:
            return await ctx.respond("You do not have an active case.", ephemeral=True)

        front_page = discord.Embed(title=str(case), description=str(case.id))
        front_page.add_field(name="Current Status", value=case.status, inline=False)
        front_page.add_field(name="Filed Datetime", value=discord_dynamic_timestamp(case.created, 'F'), inline=True)
        front_page.add_field(name="Filed Relative", value=discord_dynamic_timestamp(case.created, 'R'), inline=True)
        front_page.add_field(name="Filed By", value=case.nameUserByID(case.plaintiff_id), inline=True)
        front_page.add_field(name="Filed Against", value=case.nameUserByID(case.defense_id), inline=True)
        if case.motion_in_consideration is not None:
            front_page.add_field(name="Motion in Consideration", value=case.motion_in_consideration, inline=False)
            front_page.add_field(name="Voting Ends", value=discord_dynamic_timestamp(case.motion_in_consideration.Expiry, 'R'), inline=False)
        front_page.add_field(name="Guilty Penalty", value=case.describePenalties(case.penalties), inline=False)

        event_page = discord.Embed(title=str(case), description=str(case.id))
        event_page.add_field(name="Event Log Length", value=len(case.event_log), inline=False)
        event_page.add_field(name="Last Event Title", value=case.event_log[-1]["name"])
        event_page.add_field(name="Last Event Desc", value=case.event_log[-1]["desc"])
        event_page.add_field(name="Last Event Datetime", value=discord_dynamic_timestamp(case.event_log[-1]["timestamp"], 'F'))

        class caseinfoview(discord.ui.View):
            @discord.ui.button(label="Main Info", style=discord.ButtonStyle.primary, emoji="📔")
            async def main_info(self, button, interaction: discord.Interaction):
                await interaction.response.edit_message(embed=front_page)

            @discord.ui.button(label="Event Log Info", style=discord.ButtonStyle.primary, emoji="📇")
            async def event_log(self, button, interaction: discord.Interaction):
                await interaction.response.edit_message(embed=event_page)
            
        await ctx.respond(embed=front_page, view=caseinfoview(), ephemeral=ephemeral)

    jury = discord.SlashCommandGroup("jury", "Jury commands")
    
    async def active_case_options(ctx: discord.AutocompleteContext):
        return [f"{case}: {case.id}" for case in cm.ACTIVECASES if case.stage == 1 and ctx.author.id in case.jurors]

    @jury.command(name="join", description="Join an active case as a juror.")
    async def jury_join(self, ctx, case: discord.Option(str, autocomplete=discord.utils.basic_autocomplete(active_case_options))):
        case = cm.getCaseByID(case.split(" ")[-1])
        if case is None:
            return await ctx.respond("Invalid case ID.", ephemeral=True)
        if ctx.author.id not in case.jury_invites:
            return await ctx.respond("You have not been invited to this case.", ephemeral=True)
        
        self.setActiveCase(ctx.author, case)
        await case.addJuror(ctx.author)

        return await ctx.respond(f"Joined case **{case}** (`{case.id}`) as a juror.", ephemeral=True)

    @slash_command(name='normalusername', description='Get a user\'s normal username.')
    @option("member", discord.Member, description="The member to get the normal username of.")
    async def normal_username(self, ctx, member: discord.Member):
        await ctx.respond(cm.Case.normalUsername(None, member), ephemeral=True)

    @slash_command(name='filetestcase', description='File a test case.')
    @option("member", discord.Member, description="The member to file a case against.")
    @option("reason", str, description="The reason for filing a case.")
    async def test_case(self, ctx, member: discord.Member, reason: str):
        case = await cm.Case().New(ctx.guild, self.bot, f"{cm.Case.normalUsername(None, ctx.author)} v. {cm.Case.normalUsername(None, member)}", reason, ctx.author, member, cm.WarningPenalty(cm.Case))
        self.setActiveCase(ctx.author, case)
        self.setActiveCase(member, case)
        await ctx.respond(f"Filed test case **{case}** (`{case.id}`) It has automatically been set as your active case.", ephemeral=True)

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
