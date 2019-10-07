# Module: logoff
# Description: Logs the user out of the system
# Usage: !logoff or !logoff secondsToLogoff
# Dependencies: time, os

import time, os, asyncio, configs


async def logoff(ctx, seconds=0):
    await ctx.send("Logging out of system.")
    if configs.operating_sys == "Windows":
        if time != 0:
            time.sleep(seconds)
        os.system("Shutdown.exe -l")
    else:
        await ctx.send("Can't logoff system.")
        await asyncio.sleep(3)
