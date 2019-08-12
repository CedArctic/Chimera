<p align="center">
  <img  width="120" height="120" src="https://user-images.githubusercontent.com/11155359/46568982-b4a6c980-c956-11e8-9232-64b64be1369c.png">
</p>



# Chimera
Chimera (not the mythical beast), is a System Remote Control Discord Bot for Windows written in Python discord.py.
Using chimera you can easily control your computer remotely and have it do from simple tasks such as shutdown, sleep and lock to talking or executing powershell commands.
Chimera is a self hosted bot, which means that you have to run the bot on your computer - the machine you want to control via discord commands.
Installing chimera is an easy 3 minute process - you can check the video bellow to see how to do it.

## Requirements:
* Python 3
* discord.py
* mss

## Features List:
* lock
* shutdown
* sleep
* hibernate
* restart
* logoff
* cmd
* powershell
* screenshot
* say
* media
* camera
* echo
* log
* file
* helpme

## Features Documentation:
```
* !lock or !lock seconds
	> locks your computer immediately or with a time delay in seconds, e.g: !lock 30
* !shutdown or !shutdown seconds
	> shuts down your computer immediately or with a time delay in seconds, e.g: !shutdown 30
* !sleep or !sleep seconds
	> sleeps your computer immediately or with a time delay in seconds, e.g: !sleep 30
* !hibernate or !hibernate seconds
	> hibernates your computer immediately or with a time delay in seconds, e.g: !hibernate 30
* !restart or !restart seconds
	> restarts your computer immediately or with a time delay in seconds, e.g: !restart 30
* !logoff or !logoff seconds
	> logs off your user immediately or with a time delay in seconds, e.g: !logoff 30

* !cmd "command"
	> executes cmd prompt command
* !powershell "command"
	> executes powershell command

* !screenshot or !screenshot seconds
	> takes a screenshot of your computer and sends it back to you 
* !say "Something to say"
	> uses powershell commands and a TTS engine to make your computer say something

* !media command or !media command times
	> controls computer media playback and volume once or repeatedly, e.g: !media prev 2
		list of commands:
		- vol-up
		- vol-down
		- vol-mute
		- next
		- prev
		- stop
		- play
		- pause
		
* !camera command or !camera command time
	> controls computer camera for taking photo or filming for a given time in seconds (default is 5 seconds), e.g: !camera video 10
		list of commands:
		- video time
		- photo
		
* !echo status
	> turns on or off !cmd and !powershell command echo in chat. When turned on, the command return will be sent to chat, e.g: !echo on
	
* !log param or !log param date
	> turns on or off chat logging or show log for given date (defaults to today), e.g: !log show 2018-10-16

* !file command or !file command path
	> browses, saves and retrieves files from or to your computer, e.g: !file relative ..
		list of commands:
		- absolute => sets an absolute path
		- relative => sets a relative path
		- list => lists current path
		- retrieve => uploads a file to the chat
		- save => saves a file to the HD from the chat
		- download => saves a file from a direct url to the HD
		
* !helpme or !helpme command
	> shows Chimera help, listing commands of shows help for a specific command, e.g: !helpme screenshot

* EOF
```
Note: Some commands may require elevated privileges on linux.

## Installation:
Follow this video tutorial

[![Video Tutorial](https://j.gifs.com/l5m85j.gif)](https://www.youtube.com/watch?v=Q5gkddzSCgA)

Text Instructions:
1. Download & Install Python
2. Create a bot and get its token and then get your channel ID by following these instructions: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord
3. Download the repository, run setup.bat(Windows) or setup.sh(Linux) and put your Bot Token in the newly created local_credentials.py. 
4. Launch Chimera.py and visit the URL printed to the console to add Chimera to a personal channel
5. Enjoy!



## Contributing:
Chimera was written to be modular so one can easily modify the code and enchance it. I welcome and greatly appreciate anyone who wishes to contribute a module of their own.
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

## Changelog:
* April 1st 2018: Initial Release
* April 28th 2018: Added Screenshot feature

## Credits:
* [Habchy](https://github.com/Habchy) for writing BasicBot which was the base for chimera
* jestemkioskiem for his great [tutorial](https://steemit.com/utopian-io/@jestemkioskiem/build-your-own-discord-bot-with-python-1-basicbot)

## Contributors:
* [Zachman61](https://github.com/Zachman61)
* [vfcoelho](https://github.com/vfcoelho)
* [DragosPopse](https://github.com/DragosPopse)
* [TGlide](https://github.com/TGlide)
* [vlad4him](https://github.com/vlad4him)
* [sn0wmanmj](https://github.com/sn0wmanmj)
* [cominixo01](https://github.com/cominixo01)
* [medusalix](https://github.com/medusalix)
