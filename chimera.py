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

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="A remote administration tool for discord", command_prefix="!", pm_help = False)

# Enter Discord Bot Token & Channel ID:
BOT_TOKEN = 'Enter Token Here'
CHANNEL_ID = 'Enter Channel ID here'

#Used by !echo(set) and !cmd/!powershell(get)
display_output = True

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
	cmnd_result = os.popen(cmnd).read()
	if display_output == True:
		await client.say(cmnd_result)
	await asyncio.sleep(3)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
# Dependencies: time, os
@client.command()
async def powershell(cmnd):
	await client.say("Executing in powershell: " + cmnd)
	cmnd_result = os.popen("powershell {}".format(cmnd)).read()
	if display_output == True:
		await client.say(cmnd_result)
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


# Module: logoff
# Description: Logs the user out of the system
# Usage: !logoff or !logoff secondsToLogoff
# Dependencies: time, os
@client.command()
async def logoff(seconds = 0):
	await client.say("Logging out of system.")
	if time != 0:
		time.sleep(seconds)
	os.system("Shutdown.exe -l")


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
	await client.send_file(client.get_channel(CHANNEL_ID),'screenshot.png')


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os
@client.command()
async def say(txt):
	await client.say("Saying: " + txt)
	os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
	await asyncio.sleep(3)

	
# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: None
@client.command()
async def echo(status):
	global display_output
	if status == "on":
		display_output = True
		await client.say("!cmd and !powershell output will be displayed in chat. ")
	elif status == "off":
		display_output = False
		await client.say("!cmd and !powershell output will be hidden from chat. ")
	else:
		await client.say("Parameter of echo can be off or on. ")

client.run(BOT_TOKEN)
