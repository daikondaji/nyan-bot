import os
import json
import asyncio
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio as ffmpeg


class Soundboard(commands.Cog):
    sounds = None

    def __init__(self, client):
        self.client = client

        with open('config.json', 'r') as file:
            data = file.read()
        
        config = json.loads(data)
        self.sounds = config['sounds']


    # Commands
    @commands.command()
    async def play(self, ctx, sound):
        if sound in self.sounds:   
            await ctx.send(f'playing {self.sounds[sound]}')

            voice = ctx.author.voice.channel

            if ctx.author.voice:
                voice = await voice.connect()
                source = ffmpeg(f'fx/{self.sounds[sound]}')
                voice.play(source)

                while voice.is_playing():
                    await asyncio.sleep(.1)
            else:
                await ctx.send("You must join the voice channel first, nyan")

            await voice.disconnect()

def setup(client):
    client.add_cog(Soundboard(client))