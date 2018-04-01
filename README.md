# Chimera
Chimera (not the mythical beast), is a System Remote Control Discord Bot for Windows written in Python discord.py.
Using chimera you can easily control your computer remotely and have it do from simple tasks such as shutdown, sleep and lock to talking or executing powershell commands.
Chimera is a self hosted bot, which means that you have to run the bot on your computer - the machine you want to control via discord commands.
Installing chimera is an easy 3 minute process - you can check the video bellow to see how to do it.

## Requirements:
* Python 3
* discord.py

## Features:
```
* !lock or !lock seconds - locks your computer immediately or with a time delay in seconds
* !shutdown or !shutdown seconds
* !sleep or !sleep seconds
* !hibernate or !hibernate seconds
* !restart or !restart seconds

* !cmd "command" - executes cmd prompt command
* !powershell "command" - executes powershell command

* !say "Something to say" - uses powershell commands and a TTS engine to make your computer say something
```

## Installation:
Follow this video tutorial: -coming soon-

Alternatively follow Habchy's [instructions](https://github.com/Habchy/BasicBot/wiki) of how to setup BasicBot, but use chimera.py instead.

## Contributing:
Chimera was written to be modular so one can easily modify the code and enchance it. I welcome and greatly appreciate anyone who wished to contribute a module of their own.
To keep things tidy if you need to import a python module do so on the top of the file in this fashion e.g:

```
# Dependency of: lock, shutdown, sleep, hibernate, say, restart
import time
```
and for your command function:

```
# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
# Dependencies: time, os
@client.command()
async def cmd(cmnd):
	await client.say("Executing in command prompt: " + cmnd)
	os.system(cmnd)
	await asyncio.sleep(3)
```
