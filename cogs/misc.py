from discord.ext import commands
import discord
import datetime
import json
import os
import requests

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command()
async def about(self, ctx):
    servers = self.bot.guilds
    guilds = len(self.bot.guilds)
    servers.sort(key=lambda x: x.member_count, reverse=True)
    y = 0
    for x in self.bot.guilds:
        y += x.member_count
    embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f"Yuo Information!")
    embed.add_field(name="**General Statistics**", value=f"`Current Users` — {y}\n`Current Guilds` — {guilds}\n`Created Date` — 11/5/20\n`Creator` — <@781761427664142345>", inline=False)
    embed.add_field(name=f"**Prefix:**", value=f"`— >`\n", inline=False)
    embed.add_field(name=f"**Credits**", value=f"`— sny\n— who ever eles needs Credits\n — Myrax/Myrayuo`", inline=False)
    embed.set_footer(text="Requested by {}".format(ctx.message.author))
    await ctx.send(embed=embed)

@commands.command()
async def uptime(self, ctx):
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f"`Current Uptime:` "+''+uptime+'')

@commands.command()
async def ping(self, ctx):
    message = await ctx.send(content="`Pinging...`")
    await message.edit(content=f"`PONG!` - Latency is {round(self.bot.latency * 1000)}ms")

@commands.command()
async def invite(self, ctx):
    try:
      embed = discord.Embed(description=f"thank you for using me", color=0x2f3136, timestamp=datetime.datetime.utcnow())
      embed.add_field(name=f"**Support Server**", value=f"[Server Invite](https://discord.gg/At2zhuHX)\n", inline=False)
      embed.set_author(name=f"Links!", icon_url=ctx.guild.icon_url)
      embed.set_footer(text=f"{ctx.guild.name}")
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.author.send(embed=embed)
      await ctx.channel.send(f"I have sent you an invite, Check your DM! {ctx.author.mention}")
    except:
      await ctx.channel.send(embed=embed)

@commands.command()
async def bots(self, ctx):
      bots = []
      for member in ctx.guild.members:
          if member.bot:
              bots.append(
                  str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
      bottiez = discord.Embed(description=f"**Bots ({len(bots)})**\n{', '.join(bots)} - {ctx.bot.user.id}", color=0x2f3136)
      await ctx.send(embed=bottiez)

@commands.command(name='urban')
async def urban(self, ctx, *args,  user: discord.Member = None):
      if user is None:
          user = ctx.author   
      url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

      querystring = {"term":' '.join(map(str,args))}

      headers = {
      'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
      'x-rapidapi-key': URBAN_API_KEY
      }

      response = requests.request("GET", url, headers=headers, params=querystring)
      urbanObject = json.loads(response.content)

      Embed = discord.Embed(title=f"{' '.join(map(str,args))} | Urban", color=0x2f3136)
      Embed.add_field(name='Definition', value=str(urbanObject['list'][0]['definition']), inline=False)
      Embed.add_field(name='Example', value=str(urbanObject['list'][0]['example']), inline=False)
      Embed.add_field(name='URL', value=str(urbanObject['list'][0]['permalink']), inline=False)
      Embed.set_thumbnail(url=user.avatar_url)
      Embed.set_footer(text="Requested by {}".format(ctx.message.author))
      await ctx.send(embed=Embed)


@commands.command()
async def members(self, ctx):
      guild = ctx.guild
      embed = discord.Embed(color=0x2f3136, timestamp=datetime.datetime.utcnow())
      embed.set_author(name=f"Links!", icon_url=ctx.guild.icon_url)
      embed.add_field(name=f"Member Count:", value=f"> {len(guild.members)}")
      embed.set_footer(text=f"{ctx.guild.name}")
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(misc(client))