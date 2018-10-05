echo "Installing Required Packages..."

pip3 install -U -r ./requirements.txt

echo "Creating local_credentials.py..."

touch local_credentials.py

printf "BOT_TOKEN = 'Enter Token Here'\n\n" > local_credentials.py

printf "CHANNEL_ID = 'Enter Channel ID Here\n\n" >> local_credentials.py

printf "PYTHON_ALIAS = 'python' #only change if you have multiple python installations" >> local_credentials.py

echo "Done. Please fill the required fields in local_credentials.py"
