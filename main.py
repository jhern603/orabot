import discord
import os
import datetime
import aiohttp
import re

from utilities.envloader import *
from urllib import parse, request
from discord.ext import commands

activity = discord.Activity(
    type=discord.ActivityType.listening, name="your commands")
client = commands.Bot(command_prefix='$', activity=activity,
                   description="This is a Helper Bot")


class OraBot(discord.Client):

    def __init__(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{file[:-3]}')
                print(f'Loaded cog: {file[:-3]}')
        client.run(envloader.getToken())

        
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        
    @client.event
    async def on_ready():
        print('Connected to bot: {}'.format(client.user.name))
        print('Bot ID: {}'.format(client.user.id))
        print('Orabot connected!')
    @client.command()
    async def info(ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description=f"{ctx.guild.description}",
                              timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at",
                        value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(
            url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

        await ctx.send(embed=embed)

    @client.command()
    async def giverole(self, ctx):
        await ctx.send("giverole ran")






if __name__ == '__main__':
    instance = OraBot()
