import discord
from discord.ext import commands
import datetime


class utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!🏓 {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description=f"{ctx.guild.description}",
                              timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at",
                        value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(
            url=ctx.guild.icon_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(utilities(client))
