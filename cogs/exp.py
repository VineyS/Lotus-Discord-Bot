import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
import math
class LevelCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            db = sqlite3.connect('levelll.sqlite')
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
            result = cursor.fetchone()
            if result is None:
                sql = ("INSERT INTO levels(guild_id, user_id, exp, level) VALUES(?,?,?,?)")
                val = (message.author.guild.id, message.author.id, 2, 0)
                cursor.execute(sql, val)
                db.commit()
            else:
                cursor.execute(f"SELECT user_id, exp, level FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
                result1 = cursor.fetchone()
                exp = int(result1[1])
                sql = ("UPDATE levels SET exp = ? WHERE guild_id = ? and user_id = ?")
                val = (exp + 2, str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()

                cursor.execute(f"SELECT user_id, exp, level FROM levels WHERE guild_id = '{message.author.guild.id}' and user_id = '{message.author.id}'")
                result2 = cursor.fetchone()

                xp_start = int(result2[1])
                lvl_start=int(result2[2])
                xp_end = math.floor(5* (lvl_start ^ 2)+50 * lvl_start + 100)
                if xp_end < xp_start:
                    await message.channel.send(f"{message.author.mention} has leveled up to Level {lvl_start + 1}")
                    sql = ("UPDATE levels set level = ? WHERE guild_id = ? and user_id = ?")
                    val = (int(lvl_start+1), str(message.guild.id), str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    sql = ("UPDATE levels set exp = ? WHERE guild_id = ? and user_id = ?")
                    val = (0, str(message.guild.id), str(message.author.id))
                    cursor.execute(sql, val)
                    db.commit()
                    cursor.close()
                    db.close()
    @commands.command()
    async def rank(self, ctx, user:discord.User=None):
        if user is None or not user.bot:
            if user is not None:
                db = sqlite3.connect('levelll.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, exp, level FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{user.id}'")
                result = cursor.fetchone()
                if result is None:
                    await ctx.send("This user is not yet ranked!!")
                else:
                    await ctx.send(f"{user.name} is currently level '{str(result[2])}' and has '{str(result[1])}' XP")
                cursor.close()
                db.close()
            elif user is None:
                db = sqlite3.connect('levelll.sqlite')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, exp, level FROM levels WHERE guild_id = '{ctx.message.author.guild.id}' and user_id = '{ctx.message.author.id}'")
                result = cursor.fetchone()
                if result is None:
                    await ctx.send("This user is not yet ranked!!")
                else:
                    await ctx.send(f"{ctx.message.author.name} is currently level '{str(result[2])}' and has '{str(result[1])}' XP")
                cursor.close()
                db.close()
        #elif ctx.author.bot is True or user.bot is True:
        else:
            await ctx.send(f"Bots aren't ranked for leveling system!")
    @commands.command()
    async def leaderboard(self, ctx):
        db = sqlite3.connect('levelll.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, level, exp FROM levels WHERE guild_id = '{ctx.author.guild.id}' ORDER BY level DESC")
        result = cursor.fetchall()
        print(result)
        l = []
        rem = []
        for i in result:
            print(i[0])
            #ann = "<#" str(i[0])
            l.append(i[0])
            rem.append(i[1])
        new_rank = []
        for a in l:
            #await ctx.send(self.bot.get_user(a))
            member = await self.bot.fetch_user(a)
            await ctx.send(member)
            new_rank.append(member)
        pos = 1
        post1 = 0
        trial = 1
        for final in range(len(new_rank)):
            form = str(trial) + '.' + ' ' + final + rem[post1]
            print(form)
            trial = eval(trial)
            trial+=1
            post1+=1
        

        



def setup(bot):
    bot.add_cog(LevelCog(bot))
    print("Loaded Level Successfully")
