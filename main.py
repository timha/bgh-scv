import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

# load env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
CH_WELCOME = os.getenv("CH_WELCOME")

intents = discord.Intents.default()
intents.members = True

# set command prefix
client = commands.Bot(command_prefix = COMMAND_PREFIX, intents=intents)


@client.event
async def on_ready():
    print('Map loaded')
    print('--------------------------')

@client.command()
async def hello(ctx):
    await ctx.send('SCV good to go sir!')

# act member joins the server
@client.event
async def on_member_join(member):
    print("Member: " + str(member.id))
    print("Joined: " + str(member.joined_at))
    print("----------------------------------")
    channel = client.get_channel(int(CH_WELCOME))
    await channel.send("Welcome to Big Game Hunters, " + str(member.name) + "!")


client.run(BOT_TOKEN)
