import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions, MissingRequiredArgument
import asyncio
import datetime
import time
class ModCog(commands.Cog,name='Moderation'):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['cls','clear','clearchat'])
    async def purge(self,ctx,number:int=None):
        c = 0
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send(f"You must enter a number!!")
                else:
                    deleted = await ctx.channel.purge(limit=number+1)
                    await ctx.send(f"`{len(deleted)-1}` messages have been deleted")
                    time.sleep(3)
                    await ctx.channel.purge(limit=1)
            except:
                await ctx.send("I am not permitted to delete messages. Please give me the role `Manage Messages`")
        else:
            await ctx.send(f"{ctx.message.author.mention} You are missing following permissions: `Manage Messages`")
    @commands.command()
    async def kick(self,ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_guild:
            await ctx.send("This user is either a moderator or administrator. I can't kick them")
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user, reason='None')
                await ctx.send(f'{user} has been kicked')
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{user} has been kicked')
        else:
            await ctx.send(f'{ctx.message.author.mention} You are missing the following permissions: `Kick Members`')
    @kick.error
    async def kickerror(self,ctx,error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f"I can't kick this member, I need the permissions `kick members`")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f"Bruh! You must mention the member to be kicked")
            await ctx.send(f"`{ctx.prefix}kick <member> ??? Member argument is Missing!`")
        else:
            await ctx.send(f"I must be placed to a higher hierarchy to kick the member out{ctx.message.author.mention}")


    @commands.command()
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        if user.guild_permissions.manage_guild:
            await ctx.send("This user is either a moderator or administrator. I can't ban them")
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await ctx.send(f'`{ctx.prefix}ban <member> <reason> ??? Reason Missing`')
            else:
                await ctx.guild.ban(user=user, reason=reason)
                await ctx.send(f'{user} has been banned for {reason}')
        else:
            await ctx.send(f'{ctx.message.author.mention} You are missing the following permissions: `Ban Members`')
    @ban.error
    async def banerror(self,ctx,error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f"I can't ban this member, I need the permissions `ban members`")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f"Bruh, You must mention the member to be banned!")
            await ctx.send(f"`{ctx.prefix}ban <member> <reason> ??? Member Argument Missing!`")
        else:
            await ctx.send(f"I must be placed to a higher hierarchy to ban the member{ctx.message.author.mention}")

def setup(bot):
    bot.add_cog(ModCog(bot))
    print("Loaded Moderation Successfully")
