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

# Dependency of camera
# from lib.camera_control import CameraControl #commented because of the workaround

# For using commands in different systems
from lib.helpers import get_operating

# Dependency of media
from lib.helpers import MediaControlAdapter

# Dependency of file
from lib.filesystem_control import FileSystemControl
import requests

# Dependency of log
from datetime import datetime

# Platform name
operating_sys = get_operating()

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="A remote administration tool for discord",
             command_prefix="!", pm_help=False)

from lib.helpers import Logger

# Used by !screenshot and !camera commands
import configs as Configs

@client.event
async def on_ready():
    
    print('--------')
    print('Chimera Remote Administration Bot by CedArctic')
    print('--------')
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to ' +
          str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(
        discord.__version__, platform.python_version()))
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
@Logger(client)
async def cmd(cmnd):
    await client.say("Executing in command prompt: " + cmnd)
    cmnd_result = os.popen(cmnd).read()
    if Configs.initial_display_output == True:
        await client.say(cmnd_result)
    await asyncio.sleep(3)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
# Dependencies: time, os
@client.command()
@Logger(client)
async def powershell(cmnd):
    if operating_sys == "Windows":
        await client.say("Executing in powershell: " + cmnd)
        cmnd_result = os.popen("powershell {}".format(cmnd)).read()
        if Configs.initial_display_output == True:
            await client.say(cmnd_result)
    else:
        await client.say("Powershell is only available in Windows")
    await asyncio.sleep(3)


# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os
@client.command()
@Logger(client)
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
@Logger(client)
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
@Logger(client)
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
@Logger(client)
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
@Logger(client)
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
@Logger(client)
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
@client.command(pass_context = True)
@Logger(client)
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
@Logger(client)
async def say(txt):
    if operating_sys == "Windows":
        await client.say("Saying: " + txt)
        os.system("powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
    elif operating_sys == "Linux":
        await client.say("Saying: " + txt)
        os.system('spd-say "{}"'.format(txt))
    else:
        await client.say("Can't use TTS")
    await asyncio.sleep(3)


# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: pynput, time, helpers
@client.command()
@Logger(client)
async def media(command,times=1):
    media_control = MediaControlAdapter(operating_sys)
    switcher = {
        'vol-up':media_control.up_volume,
        'vol-down':media_control.down_volume,
        'vol-mute':media_control.mute_volume,
        'next':media_control.media_next,
        'prev':media_control.media_previous,
        'stop':media_control.media_stop,
        'play':media_control.media_play_pause,
        'pause':media_control.media_play_pause
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
@Logger(client)
async def camera(ctx, command, time=5):
    await client.say('Recording!')
    python_alias = Configs.PYTHON_ALIAS
    
    if command == 'photo':
#         CameraControl.photo_capture()
        os.system("{} lib/camera_control.py photo".format(python_alias))#workaround
        await client.send_file(ctx.message.channel, 'photo.jpg')
        
    if command == 'video':
#         await CameraControl.video_capture(time=time)
        os.system("{} lib/camera_control.py video {}".format(python_alias,time))#workaround
        await client.send_file(ctx.message.channel, 'video.avi')
    
    
    
# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: None
@client.command()
@Logger(client)
async def echo(status):
    if status == "on":
        Configs.initial_display_output = True
        await client.say("!cmd and !powershell output will be displayed in chat. ")
    elif status == "off":
        Configs.initial_display_output = False
        await client.say("!cmd and !powershell output will be hidden from chat. ")
    else:
        await client.say("Parameter of echo can be off or on. ")

# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
# Dependencies: logging, datetime
@client.command()
@Logger(client)
async def log(param, date=None):
    if param == "on":
        Configs.discord_logs_enabled = True
        await client.say("Exceptions log will now be displayed in chat.")
    elif param == "off":
        Configs.discord_logs_enabled = False
        await client.say("Running on silent mode now.")
    elif param == "show":
        date = date if date else (datetime.now()).strftime('%Y-%m-%d')
        file = open('{}/{}.txt'.format(Logger.DIRECTORY,date),'r')
        log_text = file.read()
        await client.say(log_text)
    else:
        await client.say("Parameter of !log can be off or on. ")

# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
# Dependencies: filesystem_control, requests
@client.command(pass_context = True)
@Logger(client)
async def file(ctx, command, *args):
    filesystem_control = FileSystemControl(Configs.initial_path)
    await filesystem_control.load_path_from_memory()
    
    async def set_absolute_path(path):
        new_path = await filesystem_control.set_path(path, False)
        return 'Current location set to {}'.format(new_path)
    
    async def set_relative_path(path):
        new_path = await filesystem_control.set_path(path, True)
        return 'Current location set to {}'.format(new_path)
    
    async def retrive_file(path=None):
        file_path = await filesystem_control.retrieve_file(path)
        await client.send_file(ctx.message.channel, file_path)
        
    async def save_file(path=None):
        filename = ctx.message.attachments[0]['filename']
        url = ctx.message.attachments[0]['url']
        
        r = requests.get(url, allow_redirects=True)
        if r.status_code/100 != 2:
            raise Exception('Download request from Discord returned {}'.r.status_code)
        file = r.content
        
        file_path = await filesystem_control.save_file(file,filename,path)
        return 'File Saved on {}'.format(file_path)
    
    async def list_directory():
        dir_list = await filesystem_control.list_directory()
        result = "Directory items:\n"
        for item in dir_list:
            result += "`{}`\n".format(item.name)
        return result
    
    switcher = {
        'absolute':set_absolute_path,
        'relative':set_relative_path,
        'list':list_directory,
        'retrieve':retrive_file,
        'save':save_file
        }
    
    if len(args)>0:
        message = await switcher[command](*args)
    else:
        message = await switcher[command]()
    if message: await client.say(message)

client.run(Configs.BOT_TOKEN)
