# Basic Bot Dependencies
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Dependency of: lock, shutdown, sleep, hibernate, logoff, say, restart, screenshot
import os

# Dependency of: lock, shutdown, sleep, hibernate, logoff, say, restart
import time

# Dependency of screenshot
from mss import mss

# For using commands in different systems
from helpers import get_operating

# Platform name 
operating_sys = get_operating()

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="A remote administration tool for discord", command_prefix="!", pm_help = False)

# Enter Discord Bot Token & Channel ID:
BOT_TOKEN = 'Enter Token Here'
CHANNEL_ID = 'Enter Channel ID'

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
	if operating_sys == "Windows":
		await client.say("Executing in powershell: " + cmnd)
		os.system("powershell {}".format(cmnd))
	else:
		await client.say("Powershell is only available in Windows")
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
	if operating_sys == "Windows":
		os.system("rundll32.exe user32.dll,LockWorkStation")
	elif operating_sys == "Linux":
		os.popen('gnome-screensaver-command --lock')
	else:
		await client.say("Can't lock system.")
		await asyncio.sleep(3)


# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
# Dependencies: time, os
@client.command()
async def sleep(seconds = 0):
	if operating_sys == "Windows":
		await client.say("Putting system to sleep.")
		if time != 0:
			time.sleep(seconds)
		os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
	else:
		await client.say("Can't put system to sleep.")
		await asyncio.sleep(3)


# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
# Dependencies: time, os
@client.command()
async def shutdown(seconds = 0):
	await client.say("Shutting system down.")
	if operating_sys == "Windows":
		if time != 0:
			time.sleep(seconds)
		os.system("Shutdown.exe -s -t 0")
	elif operating_sys == "Linux":
		if time != 0:
			time.sleep(seconds)
		os.system("shutdown")
	else:
		await client.say("Can't shutdown system.")
		await asyncio.sleep(3)



# Module: restart
# Description: Restarts system
# Usage: !restart or !restart secondsToRestart
# Dependencies: time, os
@client.command()
async def restart(seconds = 0):
	await client.say("Restarting system.")
	if operating_sys == "Windows":
		if time != 0:
			time.sleep(seconds)
		os.system("Shutdown.exe -r")
	elif operating_sys == "Linux":
		if time != 0:
			time.sleep(seconds)
		os.system("reboot")
	else:
		await client.say("Can't restart system.")
		await asyncio.sleep(3)


# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
# Dependencies: time, os
@client.command()
async def hibernate(seconds = 0):
	await client.say("Hibernating system.")
	if operating_sys == "Windows":
		if time != 0:
			time.sleep(seconds)
		os.system("rundll32.exe PowrProf.dll,SetSuspendState")
	else:
		await client.say("Can't hibernate system.")
		await asyncio.sleep(3)


# Module: logoff
# Description: Logs the user out of the system
# Usage: !logoff or !logoff secondsToLogoff
# Dependencies: time, os
@client.command()
async def logoff(seconds = 0):
	await client.say("Logging out of system.")
	if operating_sys == "Windows":
		if time != 0:
			time.sleep(seconds)
		os.system("Shutdown.exe -l")
	else:
		await client.say("Can't logoff system.")
		await asyncio.sleep(3)
	


# Module: screenshot
# Description: Takes a screenshot and sends it back
# Usage: !screenshot or !screenshot secondsToScreenshot
# Dependencies: time, os, mss
@client.command()
async def screenshot(seconds = 0):
	if os.path.isfile('screenshot.png'):  # Check if a screenshot.png exists, if yes, delete it so it can be replaced
		os.remove('screenshot.png')
	await client.say("Taking a screenshot.")
	if time != 0:
		time.sleep(seconds)
	with mss() as sct:
		filename = sct.shot(mon=-1, output='screenshot.png')
	try:
		await client.send_file(client.get_channel(CHANNEL_ID),'screenshot.png')
	except:
		await client.say("An error occurred.")


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os
@client.command()
async def say(txt):
	if operating_sys == "Windows":
		await client.say("Saying: " + txt)
		os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
	else:
		await client.say("Can't use TTS")
	await asyncio.sleep(3)

client.run(BOT_TOKEN)
