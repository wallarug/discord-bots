#!/usr/bin/python3
import discord
import os
from datetime import datetime

## Load the configuration file(s)
# check if config.json exists, if not return error
if not os.path.isfile("config.txt"):
    print("ERROR: config.json not found. Please create config.txt in the same directory as this file. See config_example.txt for an example template.")
    exit()

# Load config file data in variables (config.txt)
dir_path = os.path.dirname(__file__)
f = open(dir_path + "/config.txt", "r")
DISCORD_TOKEN = f.readline().strip()
PRIMARY_GUILD = f.readline().strip()
ADMIN_ROLE_ID = f.readline().strip()
LOG_CHANNEL_ID = f.readline().strip()
f.close()

## Setup the Discord Bot Client
bot = discord.Client()

## Use this if you need bot intents.
## See: 
#intents = discord.Intents().all()
#bot = discord.Client(intents=intents)

## User Variables - moved to config.txt
#DISCORD_TOKEN = "your-bot-token"
#active_server = "your-server-name"


## Bot Events - when the bot starts up or reconnects to a server
# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to Discord!')
#     print(f'Active on the following servers:')
#     for guild in bot.guilds:
#         print(f' - {guild.name}')

## Bot Events - when a message is sent to a channel
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('!hello'):
#         await message.channel.send('Hello!')

## Bot Events - when a user joins a server
# @bot.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to {active_server}!'
#     )

## Bot Events - when a user updates their profile
# @bot.event
# async def on_member_update(before, after):
#     if before.display_name != after.display_name:
#         print(f'{before.display_name} changed their name to {after.display_name}')
#     if before.status != after.status:
#         print(f'{before.display_name} changed their status to {after.status}')
#     if before.activity != after.activity:
#         print(f'{before.display_name} changed their activity to {after.activity}')

## Run the bot
bot.run(DISCORD_TOKEN)