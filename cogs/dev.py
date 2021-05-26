import discord
import random
from discord.ext import commands
import time
#varibles

class dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def botdev(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"Myrayuo made this bot, if any devs also help this message will be updated with there profiles", color=ctx.author.color)
        await ctx.send(embed=embed)
        time.sleep(1)
        embed1 = discord.Embed(description=f"myrayuo#1574", color=ctx.author.color)
        await ctx.send(embed=embed1)

    @commands.command()
    async def botinvite(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"https://discord.com/api/oauth2/authorize?client_id=827065812270579719&permissions=8&scope=bot", color=ctx.author.color)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(dev(client))