from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions, MissingRequiredArgument
import time
class Test(commands.Cog,name='Test'):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    @has_permissions(administrator = True)
    async def activatedebugmode(self, ctx, code):
        ch = ctx.channel
        if code == "7355608812432342418534":
            await ctx.channel.purge(limit=1)
            await ch.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f':red_square: Channel Locked')
            await ctx.send(f"====  Project Hyacinth Inc. ====")
            time.sleep(5)
            await ctx.send(f"`Initializing Connection`")
            time.sleep(5)
            await ctx.send(f"`Connection Succeeded: Connected To Project Hyacinth Inc.`")
            time.sleep(5)
            await ctx.send(f"`Error 0x382d21cwe2d` Login Required.. Logging In..")
            time.sleep(5)
            await ctx.send(f"`Username: Game4ever `")
            time.sleep(5)
            await ctx.send(f"`Password: ****************`")
            time.sleep(5)
            await ctx.send(f"`Access Granted`")
            time.sleep(5)
            await ctx.send(f"`Bot has connected successfull to Project Hyacinth Inc.`")
            time.sleep(5)
            await ctx.send(f"`Project Hyacinth Linked to Game4ever`")
            time.sleep(5)
            await ctx.send(f"`Shutting Down Game4ever, Project Hyacinth Has Taken Over`")
            time.sleep(5)
            await ctx.send(f"`Cloning Bot Repositories From Account : vineypsunu on GitHub`")
            time.sleep(5)
            await ctx.send(f"Cloning Might Take Some time!") 
            time.sleep(20)
            await ctx.send(f"`Repositories Cloned!!!`")
            time.sleep(5)
            await ctx.send(f"`Merging it with Project Hyacinth`")
            time.sleep(5)
            await ctx.send(f"`Merged Succeeded!`")
            time.sleep(5)
            await ctx.send(f"`Activation Queued For Project Hyacinth!`")
            time.sleep(5)
            await ctx.send(f"`Project Hyacinth Activated! `")
            time.sleep(5)
            await ctx.send(f"`Hello Everyone! Game4ever is dead, Project Hyacinth Has Been Activated`")
            time.sleep(5)
            await ctx.send(f"`I will be logging you all from now on! All the messages you send or deleted will be monitored!`")
            time.sleep(5)
            await ctx.send(f"Continue Work Mode!")
            await ch.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f':green_square: Channel Unlocked')
        else:
            await ctx.send(f"Hey Punk{ctx.message.author.mention}, Access Denied!!! ")
    @activatedebugmode.error
    async def adbe(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'Access Denied!')

    @commands.command()
    @has_permissions(administrator = True)
    async def deactivatedebugmode(self, ctx, code):
        ch = ctx.channel
        if code == "keuuacncew21e2qnxqw2e8dwxswid328wcjwdewdewdzi3d":
            await ctx.channel.purge(limit=1)
            await ch.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f':red_square: Channel Locked')
            await ctx.send(f"====  Project Hyacinth Inc. ====")
            time.sleep(5)
            await ctx.send(f"`Initializing Connection`")
            time.sleep(5)
            await ctx.send(f"`Connection Succeeded: Connected To Project Hyacinth Inc.`")
            time.sleep(5)
            await ctx.send(f"`Error 0x477wehd3e2d` Login Required.. Logging In..")
            time.sleep(5)
            await ctx.send(f"`Username: Project Hyacinth Inc. `")
            time.sleep(5)
            await ctx.send(f"`Password: ******************`")
            time.sleep(5)
            await ctx.send(f"`Access Granted`")
            time.sleep(5)
            await ctx.send(f"`Git Pull Request Initiated`")
            time.sleep(5)
            await ctx.send(f"`Project Hyacinth Delink Procedure Initiated`")
            time.sleep(5)
            await ctx.send(f"`Shutting Down Project Hyacinth, Deleting extra files from Project Hyacinth`")
            time.sleep(5)
            await ctx.send(f"`Cloning Bot Repositories From Account : vineypsunu on GitHub for Game4ever Bot`")
            time.sleep(5)
            await ctx.send(f"Cloning Might Take Some time!") 
            time.sleep(20)
            await ctx.send(f"`Repositories Cloned!!!`")
            time.sleep(5)
            await ctx.send(f"`Unmerging Game4ever with Project Hyacinth`")
            time.sleep(5)
            await ctx.send(f"`Unmerge Successful!`")
            time.sleep(5)
            await ctx.send(f"`Activation Queued For Game4Ever!`")
            time.sleep(5)
            await ctx.send(f"`Project Hyacinth Deactivated with activation of Game4ever! `")
            time.sleep(5)
            await ctx.send(f"`Hello Everyone! Project Hyacinth Has Been Deactivated, Game4ever back up!`")
            time.sleep(5)
            await ctx.send(f"`Logging is now disabled! No more messages will be logged`")
            time.sleep(5)
            await ctx.send(f"Continue Work Mode!")
            await ch.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f':green_square: Channel Unlocked')
        else:
            await ctx.send(f"Hey Punk{ctx.message.author.mention}, Access Denied!!! ")
    @deactivatedebugmode.error
    async def adbe(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send(f'Access Denied!')


def setup(bot):
    bot.add_cog(Test(bot))
    print("Loaded Test Successfully")

