import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

# load env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")

# set command prefix
client = commands.Bot(command_prefix = COMMAND_PREFIX)


@client.event
async def on_ready():
    print('SVC ready to go sir!')
    print('--------------------------')

@client.command()
async def hello(ctx):
    await ctx.send('hello, SCV I am')

# act member joins the server
@client.event
async def on_member_join(member):
    await print('welcome' + str(member.name))



client.run(BOT_TOKEN)
