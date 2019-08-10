# Module: log
# Description: Turns on of off logs in chat. Also can be used to retrieve Chimera execution logs
# Usage: !log [off|on] | [show] [date (format: YYYY-MM-DD)]
# Dependencies: logging, datetime

import configs, discord
from datetime import datetime
from lib.helpers import Logger


async def log(ctx, param, date=None):
    if param == "on":
        configs.discord_logs_enabled = True
        await ctx.send("Exceptions log will now be displayed in chat.")
    elif param == "off":
        configs.discord_logs_enabled = False
        await ctx.send("Running on silent mode now.")
    elif param == "show":
        date = date if date else (datetime.now()).strftime('%Y-%m-%d')
        await ctx.send(file=discord.File('{}/{}.txt'.format(Logger.DIRECTORY, date)))
    else:
        await ctx.send("Parameter of !log can be off or on. ")
