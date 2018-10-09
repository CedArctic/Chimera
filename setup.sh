echo "Installing Required Packages..."

pip3 install -U -r ./requirements.txt

configfile="configs.py"

echo "Creating $configfile ..."

touch $configfile

printf "BOT_TOKEN = 'Enter Token Here'\n\n" > $configfile

printf "CHANNEL_ID = 'Enter Channel ID Here'\n\n" >> $configfile

printf "PYTHON_ALIAS = 'python' #only change if you have multiple python installations\n\n" >> $configfile

printf "DISK_LOGS_ENABLED = True\n\n" >> $configfile

printf "initial_display_output = True\n\n" >> $configfile

printf "initial_path = ''\n\n" >> $configfile

printf "discord_logs_enabled = False\n\n" >> $configfile

echo "Done. Please fill the required fields in local_credentials.py"

