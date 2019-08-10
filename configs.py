# Load configuration parameters
from pathlib import Path
from dotenv import load_dotenv
import os, lib.helpers

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

BOT_PREFIX = os.getenv('DISCORD_BOT_PREFIX', '!')

CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

PYTHON_ALIAS = os.getenv('PYTHON_ALIAS', 'python')

DISK_LOGS_ENABLED = os.getenv('DISK_LOGS_ENABLED', True)

initial_display_output = os.getenv('INITIAL_DISPLAY_OUTPUT', True)

initial_path = os.getenv('INITIAL_PATH')

discord_logs_enabled = os.getenv('DISCORD_LOGS_ENABLED', False)

operating_sys = lib.helpers.get_operating()
