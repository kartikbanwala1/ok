import discord
from discord.ext import commands
#varibles
YuoPic = "https://cdn.discordapp.com/attachments/825389028345511937/844973979160674340/image0.gif"
class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pong(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(description=f"Ping! `{round(self.client.latency * 1000)}ms`", color=ctx.author.color)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def nsfwcog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Belle_delphine", value="\nPic/gif of bell delphine", inline=False)
        embed.add_field(name="Hentai_gif", value="\nGif of hentai", inline=False)
        embed.add_field(name="Lesc", value="\nShows lesbian gifs", inline=False)
        embed.add_field(name="Titsc", value="\nShows anime tits", inline=False)
        embed.add_field(name="Boobsc", value="\nShows boobs", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)

    @commands.command()
    async def misccog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="About", value="\nShows info about the selfbot", inline=False)
        embed.add_field(name="Uptime", value="\nShows how long the bot been up hentai", inline=False)
        embed.add_field(name="Ping", value="\nShows the bots ping", inline=False)
        embed.add_field(name="Invite", value="\nInvite you to the server", inline=False)
        embed.add_field(name="Bots", value="\nShows how many bots are in the server", inline=False)
        embed.add_field(name="Urban", value="\nSearch word on google", inline=False)
        embed.add_field(name="Members", value="\nShows how many members are in a server", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)

    @commands.command()
    async def helpcog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="BasicCog", value="\nBasic commands", inline=False)
        embed.add_field(name="FunCog", value="\nFun commands", inline=False)
        embed.add_field(name="ImageCog", value="\nImage commands", inline=False)
        embed.add_field(name="FactCog", value="\nFact commands", inline=False)
        embed.add_field(name="NsfwCog", value="\nNsfw commands", inline=False)
        embed.add_field(name="DevCog", value="\nDev commands", inline=False)
        embed.add_field(name="MiscCog", value="\nMisc commands", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def funcog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Magic_Ball", value="\nAnswers your question", inline=False)
        embed.add_field(name="Dic", value="\nDick", inline=False)
        embed.add_field(name="Say", value="\nSays whatever you say", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def imagecog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dog_img", value="\nImage of dog", inline=False)
        embed.add_field(name="Cat_img", value="\nImage of cat", inline=False)
        embed.add_field(name="Meme", value="\nImage of meme", inline=False)
        embed.add_field(name="Oreo_img", value="\nImage of an oreo", inline=False)
        embed.add_field(name="Jam_img", value="\nImage of bot dev", inline=False)
        embed.add_field(name="Noodle_img", value="\nImage of noodle", inline=False)
        embed.add_field(name="Memes", value="\nSends random a hot meme from r/memes", inline=False)
        embed.add_field(name="Dankmemes", value="\nSends a random hot meme from r/dankmemes", inline=False)
        embed.add_field(name="Cavepost", value="\nSends a random hot submission from r/chatcave", inline=False)
        embed.add_field(name="Foodporn", value="\nSends a random hot submission from r/FoodPorn", inline=False)
        embed.add_field(name="Webcomics", value="\nSends a random hot webcomic from r/webcomics", inline=False)
        embed.add_field(name="Showerthoughts", value="\nSends a random hot submission from r/showerthoughts", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def factcog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dog_fact", value="\nDog fact", inline=False)
        embed.add_field(name="Cat_fact", value="\nCat fact", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)

    @commands.command()
    async def devcog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Botdev", value="\nBot developer", inline=False)
        embed.add_field(name="BotInvite", value="\nInvite of bot", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)
    @commands.command()
    async def nukecog(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name="Dm_clear", value="\nClear schat with white space", inline=False)
        embed.add_field(name="Channel_delete", value="\nDelets all channels", inline=False)
        embed.add_field(name="Role_spam", value="\nSpams roles", inline=False)
        embed.add_field(name="Role_delete", value="\ndeletes all roles", inline=False)
        embed.add_field(name="Ban_all", value="\nBans_all", inline=False)
        embed.add_field(name="Destroy", value="\nDeletes everything", inline=False)
        embed.set_thumbnail(url=YuoPic)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(basic(client))