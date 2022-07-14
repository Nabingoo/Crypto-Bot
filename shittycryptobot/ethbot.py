from pycoingecko import CoinGeckoAPI
import time
import threading
import os
import discord
from discord.ext import commands
from discord.ext import tasks, commands
from datetime import date
from datetime import timedelta
intents = discord.Intents.default()

cg = CoinGeckoAPI()

    

intents.guilds = True

activity = discord.Activity(type=discord.ActivityType.watching, name="Working...")
bot = commands.Bot(command_prefix = "?", intents = intents, activity=activity, status=discord.Status.online)

@tasks.loop(seconds=60) # task runs every 60 seconds
async def cryptoupdate():

    await bot.wait_until_ready()
    
    
    
    
    
    
    currprice = cg.get_price(ids='solana', vs_currencies='usd')
    
    change = cg.get_price(ids='solana', vs_currencies='usd',include_24hr_change='true')
    
    
    time.sleep(3)
    
    newcurrprice = str(int(''.join(filter(str.isdigit, str(currprice)))))
    
    num1 = (change["solana"]["usd_24h_change"])
    math1 = (float(num1) / float(newcurrprice))
    math2 = (math1 * 100)
    print(math2 * 100)
    if math2 > 0:
        sign1 = "+"
    else:
        sign1 = "-"
    await bot.get_guild(942153314915713126).me.edit(nick=str(newcurrprice)[:2] + "." + str(newcurrprice)[2:len(newcurrprice)] + " USD")
    
    
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name= sign1 + str(round(math2,3))+ "%" + " | SOL | NABINGO IS THE BEST"))

cryptoupdate.start()

bot.run("OTUwNTgyMzY2NTYzMzY4OTYx.YibA0Q._QaCAqSB43jb9mdv4OS4KeWWqdU")