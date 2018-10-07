@echo off

echo Installing required packages.

pip install -U -r .\requirements.txt

SET configfile="configs.py"

echo Creating %configfile%

echo BOT_TOKEN = 'Enter Token Here' > %configfile%

echo. >> %configfile%

echo CHANNEL_ID = 'Enter Channel ID here' >> %configfile%

echo. >> %configfile%

echo PYTHON_ALIAS = 'python' #only change if you have multiple python installations >> %configfile%

echo. >> %configfile%

echo DISK_LOGS_ENABLED = True >> %configfile%

echo. >> %configfile%

echo initial_display_output = True >> %configfile%

echo. >> %configfile%

echo initial_location = "" >> %configfile%

echo. >> %configfile%

echo discord_logs_enabled = False >> %configfile%

echo Done. Please fill the required field in %configfile%

pause