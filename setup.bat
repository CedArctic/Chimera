@echo off

echo Installing required packages.

pip install -U -r .\requirements.txt

echo Creating local_credentials.py

echo BOT_TOKEN = 'Enter Token Here' > local_credentials.py

echo. >> local_credentials.py

echo CHANNEL_ID = 'Enter Channel ID here' >> local_credentials.py

echo. >> local_credentials.py

echo PYTHON_ALIAS = 'python' #only change if you have multiple python installations >> local_credentials.py

echo Done. Please fill the required field in local_credentials.py