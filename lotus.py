import discord
import json
import time
import urllib.request
import shutil
import path
import os
import asyncio
import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import datetime
import re
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
    return prefixes[str(message.guild.id)]
    #a = str(message.guild.id)
    #extras = await prefixes[(a)]
    
    #return commands.when_mentioned_or(*extras)(bot,message)



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

@bot.command()
async def test(ctx):
    with requests.get(ctx.author.avatar_url) as r:
        img_data = r.content 
    with open('profile.jpg', 'wb') as handler:
        handler.write(img_data)
    im1 = Image.open("background.png")
    im2 = Image.open("profile.jpg")

    draw = ImageDraw.Draw(im1)
    font = ImageFont.truetype("adamcg.otf", 20)
    guild = bot.get_guild(ctx.author.guild.id)
    draw.text((160, 40),f"Welcome {ctx.author.name}",(255,255,255),font=font)
    draw.text((160, 80),f"You are the 10th member",(255,255,255),font=font)

    size = 129

    im2 = im2.resize((size, size), resample=0)

    mask_im = Image.new("L", im2.size, 0)
    draw = ImageDraw.Draw(mask_im)
    draw.ellipse((0, 0, size, size), fill=255)

    mask_im.save('mask_circle.png')


    back_im = im1.copy()
    back_im.paste(im2, (11, 11), mask_im)


    back_im.save('welcomeimage.png', quality=95)
    with open("welcomeimage.png", "rb") as fp:
        await ctx.send(file=discord.File(fp, 'test.png'))
    #f = discord.File(filename="welcomeimage.png")

    #embed = discord.Embed()
    #embed.set_image(url="attachment://welcomeimage.png")


    #await bot.get_channel(ctx.author.channel_id).send(file=f, embed=embed)
""" 
@bot.command(pass_context=True)
async def info123(ctx, user: discord.Member):
    img = Image.open("infoimgimg.png") #Replace infoimgimg.png with your background image.
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Modern_Sans_Light.otf", 100) #Make sure you insert a valid font from your folder.
    fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) #Make sure you insert a valid font from your folder.
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
    draw.text((200, 0), "Information:", (255, 255, 255), font=fontbig) #draws Information
    draw.text((50, 500), "Username: {}".format(user.name), (255, 255, 255), font=font) #draws the Username of the user
    draw.text((50, 700), "ID:  {}".format(user.id), (255, 255, 255), font=font) #draws the user ID
    draw.text((50, 900), "User Status:{}".format(user.status), (255, 255, 255), font=font) #draws the user status
    draw.text((50, 1100), "Account created: {}".format(user.created_at), (255, 255, 255), font=font) #When the account was created 
    draw.text((50, 1300), "Nickname:{}".format(user.display_name), (255, 255, 255), font=font) # Nickname of the user
    draw.text((50, 1500), "Users' Top Role:{}".format(user.top_role), (255, 255, 255), font=font) #draws the top rome
    draw.text((50, 1700), "User Joined:{}".format(user.joined_at), (255, 255, 255), font=font) #draws info about when the user joined
    img.save('infoimg2.png') #Change infoimg2.png if needed.
    with open("infoimg2.png", "rb") as fp:
                await ctx.send(file=discord.File(fp, 'infoimg2.png'))
"""
#@bot.command()
#async def cinta(ctx):
#    f = open("prefixes.json","r")
#    d = f.read()
#    print(d)
#    print("=======================================================================")
#    await ctx.send(f"Sent message to heroku bot abt `{get_prefix}`")
#bot.run("NzU1Mzc2NDg0NDc4MjIyMzg2.X2CZLA.QUuCps0AMm7_JDNY-INyzx8nEFk")
bot.run("BOT_TOKEN")
