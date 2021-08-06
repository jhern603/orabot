import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

activity = discord.Activity(
    type=discord.ActivityType.listening, name="your commands")
bot = commands.Bot(command_prefix='$', activity=activity,
                   description="This is a Helper Bot")


class MyClient(discord.Client):

    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!🏓 {0}s'.format(round(bot.latency, 3)))

    @bot.command()
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

    @bot.command()
    async def giverole(ctx):
      await ctx.send("giverole ran")
      
    @bot.event
    async def on_ready():
        print('Connected to bot: {}'.format(bot.user.name))
        print('Bot ID: {}'.format(bot.user.id))
        print('Orabot connected!')
    
#I don't have this on the Oracle server right now, but can add it
bot.run('TOKEN')
