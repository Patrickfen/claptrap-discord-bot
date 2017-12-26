import importlib
import discord
import asyncio
import json
import random

token = None
with open('cred.txt') as f:
    token = f.read().rstrip()

responses = None
with open('responses.json') as f:
    responses = json.loads(f.read())

client = discord.Client()

@client.event
async def on_message(message):
    if(message.content.startswith("!")):
        try:
            response = random.choice(responses[message.content])
            await(client.send_message(message.channel, "```"+response+"```"))
        except:
            pass

client.run(token)
