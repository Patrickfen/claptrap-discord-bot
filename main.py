import importlib
import discord
import asyncio

token = None
with open('cred.txt') as f:
    token = f.read().rstrip()

print(token)

client = discord.Client()

@client.event
async def on_message(message):
    if(message.content == '!ping'):
        await client.send_message(message.channel, "pong!")

client.run(token)
