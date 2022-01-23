from pickle import TRUE
import discord
from discord.ext import commands
from discord import FFmpegOpusAudio

import os
from dotenv import load_dotenv

# load env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
CH_WELCOME = os.getenv("CH_WELCOME")
CH_LOUNGE = os.getenv("CH_LOUNGE")
GUILD_ID = os.getenv("GUILD_ID")
SONG = os.getenv("SONG")




intents = discord.Intents.all()

client = commands.Bot(command_prefix = COMMAND_PREFIX, intents=intents)

client.is_playing = False

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


# bot auto-join voice channel
@client.event
async def on_voice_state_update(member, before, after):
    voice_channel = client.get_channel(int(CH_LOUNGE))
    welcome_channel = client.get_channel(int(CH_WELCOME))
    member_count = len(voice_channel.members)
    if member_count > 0 and not client.is_playing:
        client.is_playing = True
        voice = await voice_channel.connect()
        source = FFmpegOpusAudio(SONG)
        audio_player = voice.play(source)
        print("starting music . . .")
        await welcome_channel.send("START")
        # await voice_channel.connect()
    elif member_count == 1 and client.is_playing:
        await client.get_guild(int(GUILD_ID)).voice_client.disconnect()




        client.is_playing = False
        print("stopping music . . .")
        await welcome_channel.send("STOP")


client.run(BOT_TOKEN)
