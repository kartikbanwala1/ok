import discord
import random
from discord.ext import commands
import time
#varibles
copycat = 'True'
class selfbotcmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_message(ctx, message):
        if copycat == 'True':
            await ctx.send_message(message.channel, message.content)

    @commands.command()
    async def dm_clear(self, ctx):
        await ctx.message.delete()
        await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')

    @commands.command()
    async def channel_delete(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Nuking server", delete_after=3)
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except:
                pass

    @commands.command()
    async def ban_all(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Banning all users", delete_after=3)
        for user in list(ctx.guild.members):
            try:
               await user.ban()
            except:
                pass   

    @commands.command()
    async def role_delete(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Deleting all roles", delete_after=3)
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass

    @commands.command()
    async def role_spam(self, ctx, name):
        await ctx.message.delete()
        await ctx.send(f"Spamming roles", delete_after=3)
        for _i in range(250):
            await ctx.guild.create_role(name=f"{name}")

    @commands.command()
    async def channel_spam(self, ctx, name):
        await ctx.message.delete()
        await ctx.send(f"Spamming channels", delete_after=3)
        for _i in range(250):
            await ctx.guild.create_text_channel(name=f"{name}")


def setup(client):
    client.add_cog(selfbotcmd(client))