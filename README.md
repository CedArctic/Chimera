<p align="center">
  <img  width="120" height="120" src="https://user-images.githubusercontent.com/11155359/46568982-b4a6c980-c956-11e8-9232-64b64be1369c.png">
</p>



# Chimera
Chimera (not the mythical beast), is a cross platform System Remote Control Discord Bot written in Python discord.py.
Using Chimera you can easily control your computer remotely and have it do from simple tasks such as shutdown, sleep and lock to talking or executing powershell commands.
Chimera is a self hosted bot, which means that you have to run the bot on your computer - the machine you want to control via discord commands.
Installing Chimera is an easy 3 minute process - you can check the instructions bellow to see how to do it.

## Requirements:
* Python 3
* discord.py
* mss
* opencv-python
* pynput
* requests
* python-dotenv
* pystray
* Pillow

## Features List:
* openurl
* lock
* appquitter
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
* launch
* notification
* helpme

## Features Documentation:

* !helpme or !helpme *command*
	> shows Chimera help, listing commands of shows help for a specific command, e.g: !helpme screenshot
* !openurl *url*
	> opens url in default browser, e.g: !openurl https://example.com
* !lock or !lock *seconds*
	> locks your computer immediately or with a time delay in seconds, e.g: !lock 30
* !appquitter *Application_Name* or !appquitter *Application_Name* *minutes*
	> quits the specified application immediately or with a time delay in minutes, e.g: !appquitter chrome 30
* !shutdown or !shutdown *seconds*
	> shuts down your computer immediately or with a time delay in seconds, e.g: !shutdown 30
* !sleep or !sleep *seconds*
	> sleeps your computer immediately or with a time delay in seconds, e.g: !sleep 30
* !hibernate or !hibernate *seconds*
	> hibernates your computer immediately or with a time delay in seconds, e.g: !hibernate 30
* !restart or !restart *seconds*
	> restarts your computer immediately or with a time delay in seconds, e.g: !restart 30
* !logoff or !logoff *seconds*
	> logs off your user immediately or with a time delay in seconds, e.g: !logoff 30

* !cmd "*command*"
	> executes *command* in cmd.exe
* !powershell "*command*"
	> executes *command* in Powershell

* !screenshot or !screenshot *seconds*
	> takes a screenshot of your computer and sends it back to you 
* !say "*text*"
	> uses powershell commands and a TTS engine to make your computer say something

* !media *command* or !media *command* *repeat_n_times*
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
		
* !camera *command* or !camera *command* *time*
	> controls computer camera for taking photo or filming for a given *time* in seconds (default is 5 seconds), e.g: !camera video 10
		list of commands:
		- video time
		- photo
		
* !echo *status*
	> turns on or off !cmd and !powershell command echo in chat. When turned on, the command return will be sent to chat, e.g: !echo on / !echo off
	
* !log *param* or !log *param* *date*
	> turns on or off chat logging or show log for given date (defaults to today), e.g: !log show 2018-10-16

* !file *command* or !file *command* *path*
	> browses, saves and retrieves files from or to your computer, e.g: !file relative ..
		list of commands:
		- absolute => sets an absolute path
		- relative => sets a relative path
		- list => lists current path
		- retrieve => uploads a file to the chat
		- save => saves a file to the HD from the chat
		- download => saves a file from a direct url to the HD

* !launch *shortcut*
    > launches a custom shortcut you placed in the shortcuts folder
    
* !notification "*message*"
    > sends a notification to the computer

Note: Some commands may require elevated privileges on Linux.

## Installation:

### Text Instructions:
1. Download & Install Python
2. Create a bot and get its token and then get your channel ID by following these instructions: https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord
3. Download the repository, run setup.bat on Windows or setup.sh on Linux and put your Bot Token in the newly created .env file. 
4. Launch chimera.pyw, right click on the system tray icon and hit Connect to invite chimera to your server
5. Enjoy!

### Video tutorial:

[![Video Tutorial](https://j.gifs.com/l5m85j.gif)](https://www.youtube.com/watch?v=JXqS3WaTOB4)





## Contributing:
Chimera was written to be modular so one can easily modify the code and enhance it. I welcome and greatly appreciate anyone who wishes to contribute a module of their own.
Here's how to create a Chimera module:

1. Create your *_module.py under the modules directory. See lock_module.py for a good example on how to structure yours
2. Create an entry for your modules in chimera.py. The file is full of examples.
3. Test Chimera with your changes and make a pull request if everything works well
4. Update the README.md file to include your new module and your github profile under Contributors


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
* [kostino](https://github.com/kostino)
* [GAK](https://github.com/Arvinth-Krishna)
* [BlazerYoo](https://github.com/BlazerYoo)
* [Aethese](https://github.com/Aethese)
