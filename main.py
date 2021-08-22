import json
import os
import discord
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio as ffmpeg

intents = discord.Intents.default()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print(f"{client.user} bot has logged in.")

@client.command()
async def load(ctx, ext):
    await ctx.send("Loading...")
    client.load_extension(f'cogs.{ext}')

@client.command()
async def unload(ctx, ext):
    client.unload_extension(f'cogs.{ext}')

@client.command()
async def reload(ctx, ext):
    client.reload_extension(f'cogs.{ext}')


if __name__ == '__main__':
    with open('config.json', 'r') as file:
        data=file.read()
    config = json.loads(data)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

    client.run(config['token'])