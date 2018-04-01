# Basic Bot Dependencies
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Dependency of: lock, shutdown, sleep, hibernate, say, restart
import os

# Dependency of: lock, shutdown, sleep, hibernate, say, restart
import time

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="A remote administration tool for discord", command_prefix="!", pm_help = False)

# Enter Discord Bot Token:
BOT_TOKEN = 'Enter Token Here'

@client.event
async def on_ready():
	print('--------')
	print('Chimera Remote Administration Bot by CedArctic')
	print('--------')
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Based on Habchy\'s BasicBot')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	return await client.change_presence(game=discord.Game(name='with your PC'))


# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
# Dependencies: time, os
@client.command()
async def cmd(cmnd):
	await client.say("Executing in command prompt: " + cmnd)
	os.system(cmnd)
	await asyncio.sleep(3)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
# Dependencies: time, os
@client.command()
async def powershell(cmnd):
	await client.say("Executing in powershell: " + cmnd)
	os.system(cmnd)
	await asyncio.sleep(3)


# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os
@client.command()
async def lock(seconds = 0):
	await client.say("Locking system.")
	if time != 0:
		time.sleep(seconds)
	os.system("rundll32.exe user32.dll,LockWorkStation")


# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
# Dependencies: time, os
@client.command()
async def sleep(seconds = 0):
	await client.say("Putting system to sleep.")
	if time != 0:
		time.sleep(seconds)
	os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
# Dependencies: time, os
@client.command()
async def shutdown(seconds = 0):
	await client.say("Shutting system down.")
	if time != 0:
		time.sleep(seconds)
	os.system("Shutdown.exe -s -t 0")


# Module: restart
# Description: Restarts system
# Usage: !restart or !restart secondsToRestart
# Dependencies: time, os
@client.command()
async def restart(seconds = 0):
	await client.say("Restarting system.")
	if time != 0:
		time.sleep(seconds)
	os.system("Shutdown.exe -r")


# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
# Dependencies: time, os
@client.command()
async def hibernate(seconds = 0):
	await client.say("Hibernating system.")
	if time != 0:
		time.sleep(seconds)
	os.system("rundll32.exe PowrProf.dll,SetSuspendState")


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os
@client.command()
async def say(txt):
	await client.say("Saying: " + txt)
	os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
	await asyncio.sleep(3)

client.run(BOT_TOKEN)
