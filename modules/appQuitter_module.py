# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os

import os, time, asyncio, configs


async def appquitter(ctx,appName, minutes=0):
    await ctx.send("Quitting {0} App".format(appName.upper()))
    minutes=minutes*60

    if minutes != 0:
        time.sleep(minutes)

    if configs.operating_sys == "Windows":
        os.system("taskkill /F /IM {0}.exe".format(appName))
    elif configs.operating_sys == "Linux":
        os.popen("pkill -f {0}".format(appName))
    else:
        await ctx.send("Can't quit the app.")
        await asyncio.sleep(3)
