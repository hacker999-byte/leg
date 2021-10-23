import os
import sys
import json
import discord
from os import system
from discord.ext import commands

if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls")


token = input(f"\x1b[38;5;196m[DOXXSCRAPER] \x1b[96mToken : \x1b[38;5;196m")
Bot = True
intents = discord.Intents.all()
intents.members = True
if Bot == True:
    client = commands.Bot(command_prefix="d!", case_insensitive=False, self_bot=True, intents=intents)
else:
    client = commands.Bot(command_prefix="d!", case_insensitive=False, intents=intents)

@client.event
async def on_connect():
    clear()
    print(f'''
        \033[38;5;196m\t\t██████╗░░█████╗░██╗░░██╗██╗░░██╗
        \033[38;5;196m\t\t██╔══██╗██╔══██╗╚██╗██╔╝╚██╗██╔╝
        \033[38;5;196m\t\t██║░░██║██║░░██║░╚███╔╝░░╚███╔╝░
        \033[96m\t\t██║░░██║██║░░██║░██╔██╗░░██╔██╗░
        \033[96m\t\t██████╔╝╚█████╔╝██╔╝╚██╗██╔╝╚██╗ 
        \033[96m\t\t╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
        
        ''')
    print(f"     \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mTOKEN Authenticated\x1b[38;5;196m ")
    try:
        os.remove("Scraped/members.txt")
        os.remove("Scraped/channels.txt")
        os.remove("Scraped/roles.txt")
        os.remove("Scraped/emojis.txt")
    except:
        pass

    guild = input(f"     \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mGUILD ID\x1b[38;5;196m ")
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()

    members_ = 0
    f = open("Scraped/members.txt", "a+")
    for member in members:
        f.write(f"{member.id}\n")
        members_ += 1
    print(f"        \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mScraped {members_} Members\x1b[38;5;")

    channels = 0
    f = open("Scraped/channels.txt", "a+")
    for channel in guildOBJ.channels:
        f.write(f"{channel.id}\n")
        channels += 1
    print(f"         \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mScraped {channels} Channels!\x1b[38;5;")

    roles = 0
    f = open("Scraped/roles.txt", "a+")
    for role in guildOBJ.roles:
        f.write(f"{role.id}\n")
        roles += 1
    print(f"         \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mScraped {roles} Roles!\x1b[38;5;")

    emojis = 0
    f = open("Scraped/emojis.txt", "a+")
    for emoji in guildOBJ.emojis:
        f.write(f"{emoji.id}\n")
        roles += 1
    print(f"         \x1b[38;5;196m[DOXXSCRAPER] \x1b[96mScraped {emojis} Emojis!\x1b[38;5;")


try:
    client.run(token, bot=Bot)
except:
    print(f"        \x1b[38;5;196m[DOXXSCRAPER] \x1b[96m UR TOKEN IS INVAILD!\x1b[38;5;")
    input()
    exit()
