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

print(token)

client = discord.Client()
debug = client.get_channel(395329131606179851)

@client.event
async def on_message(message):
    if(message.content == '!ping'):
        await client.send_message(message.channel, "pong!")
    elif(message.content == '!help'):
        await client.send_message(message.channel, "```Hi there!\nI'm CL4P-TP! but you can call me B4DA55 for short.\nIm here to manage you bunch.```")
    else:
        try:
            response = random.choice(responses[message.content])
            await(client.send_message(message.channel, "```"+response+"```"))
        except:
            pass

client.run(token)
