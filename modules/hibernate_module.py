# Module: hibernate
# Description: Hibernates the system
# Usage: !hibernate or !hibernate secondsToHibernation
# Dependencies: time, os

import time, os, asyncio, configs


async def hibernate(ctx, seconds=0):
    await ctx.send("Hibernating system.")
    if configs.operating_sys == "Windows":
        if time != 0:
            time.sleep(seconds)
        os.system("rundll32.exe PowrProf.dll,SetSuspendState")
    else:
        await ctx.send("Can't hibernate system.")
        await asyncio.sleep(3)
