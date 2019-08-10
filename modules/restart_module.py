# Module: restart
# Description: Restarts system
# Usage: !restart or !restart secondsToRestart
# Dependencies: time, os

import time, os, asyncio, configs


async def restart(ctx, seconds=0):
    await ctx.send("Restarting system.")
    if configs.operating_sys == "Windows":
        if time != 0:
            time.sleep(seconds)
        os.system("Shutdown.exe -r")
    elif configs.operating_sys == "Linux":
        if time != 0:
            time.sleep(seconds)
        os.system("reboot")
    else:
        await ctx.send("Can't restart system.")
        await asyncio.sleep(3)
