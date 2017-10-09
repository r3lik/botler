#!/usr/bin/python3.5
import discord
import asyncio
import os

client = discord.Client()
#uses environment variable set in .bash_profile
secret = os.environ['DISCORD_TOKEN']

@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

@client.event
async def on_message(message):
        if message.content.startswith('!ping'):
                await client.send_message(message.channel, 'Pong!')

client.run(secret)
