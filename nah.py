import discord
import random
import datetime
from discord.ext import commands
from discord.ext import tasks
import asyncio



TOKEN = "" 
prefix = "" 
bot = commands.Bot(command_prefix=prefix)
color = 0xffffff
timestamp = (datetime.datetime.utcnow())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bot is ready for use")
    await bot.change_presence(activity=discord.Game(name='anon heart :>'))


@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Commands",color=color,timestamp=timestamp)
    embed.add_field(name=">",value="n",inline=False)
    embed.add_field(name=">",value="n",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def lanx(ctx):
    await ctx.send("lanx is gay")


@bot.command()
async def pp(ctx):
    code = ["1%","2%","3%","4%"]
    no = random.choice(code)
    await ctx.send("your gay is "+no)


bot.run(TOKEN)
