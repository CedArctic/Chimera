# Basic Bot Dependencies
import discord
from discord.ext.commands import Bot
import platform

# Import configurations
import configs

# Modules import
from modules import cmd_module, powershell_module, lock_module, sleep_module, shutdown_module, restart_module
from modules import hibernate_module, logoff_module, screenshot_module, say_module, media_module, camera_module
from modules import echo_module, log_module, file_module, helpme_module


# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="A remote administration bot for Discord", command_prefix=configs.BOT_PREFIX)

from lib.helpers import Logger


@client.event
async def on_ready():
    print('--------')
    print('Chimera Remote Administration Bot by CedArctic')
    print('--------')
    print('Logged in as ' + client.user.name + ' (ID:' + str(client.user.id) + ') | Connected to '
          + str(len(client.guilds)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(
        discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Github Link: https://github.com/CedArctic/Chimera')
    print('--------')
    return await client.change_presence(activity=discord.Game(name='with your PC'))


# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
@client.command()
@Logger(client)
async def cmd(ctx, cmnd):
    await cmd_module.cmd(ctx, cmnd)


# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
@client.command()
@Logger(client)
async def powershell(ctx, cmnd):
    await powershell_module.powershell(ctx, cmnd)


# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
@client.command()
@Logger(client)
async def lock(ctx, seconds=0):
    await lock_module.lock(ctx, seconds)


# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
@client.command()
@Logger(client)
async def sleep(ctx, seconds=0):
    await sleep_module.sleep(ctx, seconds)


# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
@client.command()
@Logger(client)
async def shutdown(ctx, seconds=0):
    await shutdown_module.shutdown(ctx, seconds)


# Module: restart
# Description: Restarts system
# Usage: !restart or !restart secondsToRestart
@client.command()
@Logger(client)
async def restart(ctx, seconds=0):
    await restart_module.restart(ctx, seconds)


# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
@client.command()
@Logger(client)
async def hibernate(ctx, seconds=0):
    await hibernate_module.hibernate(ctx, seconds)


# Module: logoff
# Description: Logs the user out of the system
# Usage: !logoff or !logoff secondsToLogoff
@client.command()
@Logger(client)
async def logoff(ctx, seconds=0):
    await logoff_module.logoff(ctx, seconds)


# Module: screenshot
# Description: Takes a screenshot and sends it back
# Usage: !screenshot or !screenshot secondsToScreenshot
@client.command()
@Logger(client)
async def screenshot(ctx, seconds=0):
    await screenshot_module.screenshot(ctx, seconds)


# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os
@client.command()
@Logger(client)
async def say(ctx, txt):
    await say_module.say(ctx, txt)


# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
@client.command()
@Logger(client)
async def media(ctx, command, times=1):
    await media_module.media(ctx, command, times)


# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
@client.command()
@Logger(client)
async def camera(ctx, command, time=5):
    await camera_module.camera(ctx, command, time)


# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
@client.command()
@Logger(client)
async def echo(ctx, status):
    await echo_module.echo(ctx, status)


# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
@client.command()
@Logger(client)
async def log(ctx, param, date=None):
    await log_module.log(ctx, param, date)


# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
@client.command()
@Logger(client)
async def file(ctx, command, *args):
    await file_module.file(ctx, command, *args)


# Module: helpme
# Description: Allows file download, upload and system navigation
# Usage: !file [command]
@client.command()
@Logger(client)
async def helpme(ctx, command=None):
    await helpme_module.helpme(ctx, command)


# Application Entry Point
client.run(configs.BOT_TOKEN)
