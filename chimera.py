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

# Dependency of media
from lib.input_commands import InputCommands

# Dependency of camera
#from lib.camera_control import CameraControl #commented because of the workaround

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="A remote administration tool for discord", command_prefix="!", pm_help = False)

# Enter Discord Bot Token & Channel ID:

import local_credentials as LocalCredentials

#Create a local_credentials (added to .gitignore) file with the very same variables so there is no risk to commit credentials by mistake
BOT_TOKEN = LocalCredentials.BOT_TOKEN
CHANNEL_ID = LocalCredentials.CHANNEL_ID


# Used by !echo(set) and !cmd / !powershell(get)
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
@client.command(pass_context = True)
async def screenshot(ctx, seconds = 0):
	if os.path.isfile('screenshot.png'):  # Check if a screenshot.png exists, if yes, delete it so it can be replaced
		os.remove('screenshot.png')
	await client.say("Taking a screenshot.")
	if time != 0:
		time.sleep(seconds)
	with mss() as sct:
		filename = sct.shot(mon=-1, output='screenshot.png')
	await client.send_file(ctx.message.channel, 'screenshot.png')


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os
@client.command()
async def say(txt):
	await client.say("Saying: " + txt)
	os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
	await asyncio.sleep(3)


# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: ctypes, time
@client.command()
async def media(command,times=1):
	switcher = {
		'vol-up':InputCommands.up_volume,
		'vol-down':InputCommands.down_volume,
		'vol-mute':InputCommands.mute_volume,
		'next':InputCommands.media_next,
		'prev':InputCommands.media_previous,
		'stop':InputCommands.media_stop,
		'play':InputCommands.media_play_pause,
		'pause':InputCommands.media_play_pause
		}
	
	for time in range(0,times):
		switcher[command]()
		await asyncio.sleep(0.5)
	
	await client.say('Media Adjusted!')


# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
# Dependencies: cv2, datetime, timedelta
@client.command(pass_context = True)
async def camera(ctx, command, time=5):
	await client.say('Recording!')
	python_alias = LocalCredentials.PYTHON_ALIAS
	
	if command == 'photo':
# 		CameraControl.photo_capture()
		os.system("{} lib/camera_control.py photo".format(python_alias))#workaround
		await client.send_file(ctx.message.channel, 'photo.jpg')
		
	if command == 'video':
# 		await CameraControl.video_capture(time=time)
		os.system("{} lib/camera_control.py video {}".format(python_alias,time))#workaround
		await client.send_file(ctx.message.channel, 'video.avi')
	
	

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
