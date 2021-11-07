import discord
import os
from discord.ext import commands,tasks 
import youtube_dl
from random import choice
import music
client = discord.Client()
client = commands.Bot(command_prefix  = '!',intents = discord.Intents.all())
cogs = [music]
for i in range(len(cogs)):
  cogs[i].setup(client)



my_secret = os.environ['TOKEN']

client.run(my_secret)
