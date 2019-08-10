# Module: sleep
# Description: Puts system to sleep
# Usage: !sleep or !sleep secondsToSleep
# Dependencies: time, os

import time, os, asyncio
import configs as Configs

async def sleep(ctx, seconds=0):
    if Configs.operating_sys == "Windows":
        await ctx.send("Putting system to sleep.")
        if time != 0:
            time.sleep(seconds)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        await ctx.send("Can't put system to sleep.")
        await asyncio.sleep(3)