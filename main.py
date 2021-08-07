import discord
import os

from utilities.envloader import *
from discord.ext import commands
import time

activity = discord.Activity(
    type=discord.ActivityType.listening, name="your commands")
client = commands.Bot(command_prefix='$', activity=activity,
                      description="This is the unofficial official bot for the Oracle interns server!")


class OraBot(discord.Client):

    def __init__(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{file[:-3]}')
                print(f'Loaded cog: {file[:-3]}')
        client.run(envloader.getToken())

    @client.command()
    async def load(self, ctx, extension):
        client.load_extension(f'cogs.{extension}')

    @client.command()
    async def unload(self, ctx, extension):
        client.unload_extension(f'cogs.{extension}')

    @client.command()
    async def reload(self):
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                client.reload_extension(f'cogs.{file[:-3]}')
                print(f'Reloaded cog: {file[:-3]}')
        channel = client.get_channel(873247206617006160)
        await channel.send("Cogs reloaded!")

    @client.event
    async def on_ready():
        print(f'\nConnected to bot: {client.user.name}')
        print(f'Bot ID: {client.user.id}')
        for guild in client.guilds:
            print(f'Connected to guild: {guild.name}')
        print('Orabot connected!')

    # @client.event
    # async def on_message(message):
    #     if message.channel.name == 'jose-channel':
    #         await client.process_commands(message)


if __name__ == '__main__':
    instance = OraBot()
