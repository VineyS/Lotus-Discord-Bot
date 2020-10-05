import discord
import json
import sys
import traceback
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, MissingPermissions, MissingRequiredArgument
import sqlite3
async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("lotus!")(bot,message)

    with open(r'prefixes.json','r') as f:
        prefixes = json.load(f)
    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or("lotus!")(bot,message)
    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot,message)



bot = commands.Bot(command_prefix = get_prefix)
@bot.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MAIN(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    db1 = sqlite3.connect('main1.sqlite')
    cursor = db1.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MAIN1(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    db2 = sqlite3.connect('autorole.sqlite')
    cursor = db2.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AUTOROLE(
        guild_id TEXT,
        channel_id TEXT,
        role_id TEXT
        )
        ''')
    db3 = sqlite3.connect('levelll.sqlite')
    cursor = db3.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS levels(
        guild_id TEXT,
        user_id TEXT,
        exp TEXT,
        level TEXT
        )
        ''')
    print(f'Logged In As {bot.user}')
    print("---------------------------")
    print("Started Tracking All guilds")
    print("_________________________________________________________________________")
    change_status.start()
initial_extension = ['cogs.moderation',
                     'cogs.welcome',
                     'cogs.leave',
                     'cogs.channel',
                     'cogs.serverprefix',
                     'cogs.info',
                     'cogs.urban',
                     'cogs.gtrans']
if __name__ == '__main__':
    for extension in initial_extension:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed To Load {extension}",file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    a = f"{message.channel}: {message.author}: {message.author.name}: {message.content}"
    f = open(r'log.txt','a',encoding='utf-8')
    f.write(f"{a}\n")
    #f.write(f"\n")
    f.close()
    await bot.process_commands(message)
        
@tasks.loop()
async def change_status():
    await bot.change_presence(activity=discord.Streaming(name="lotus!help | @Lotus help", url=f"https://www.twitch.tv/test"))
@bot.command()
async def wai(ctx):
    for a in bot.guilds:
        await ctx.send(a)
@bot.command()
@has_permissions(administrator = True)
async def nick(ctx,name):
    await ctx.message.guild.me.edit(nick=name)
    await ctx.send("Nickname changed!!!")
@nick.error
async def nickerror(ctx,error):
    await ctx.send("You Don't Have Administrative Priviledges!!")
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title  = "About",
        aliases = ['support','invite'],
        description = "Hello, I am the Lotus Bot. Lotus, A Pink Aquatic Flower, which dignifies loyalty, hope, love and peace. This bot is built with love and showers that love to your server and guild members. Thank You For Inviting me!",
        colour = discord.Colour.green()
    )
    embed.set_thumbnail(url="https://i.imgur.com/W5z4Chi.png")
    embed.add_field(name="Join Our Support Server",value = "http://bit.ly/LotusSupportServer",inline = False)
    embed.add_field(name="Invite our bot",value = "http://bit.ly/LotusBotInvite",inline = False)
    await ctx.send(embed=embed)

bot.run("BOT_TOKEN")
