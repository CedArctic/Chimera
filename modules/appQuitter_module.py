# Module: appQuitter
# Description: Quits the application
# Usage: !appquitter "Application Name" or !appquitter "Application Name" minutesToQuit
# Dependencies: time, os

import os, time, asyncio, configs


async def appquitter(ctx,appName, minutes=0):
    await ctx.send(f"Quitting {appName.upper()} App")
    minutes=minutes*60

    if minutes != 0:
        await asyncio.sleep(minutes)

    if configs.operating_sys == "Windows":
        os.system(f"taskkill /F /IM {appName}.exe")
    elif configs.operating_sys == "Linux":
        os.popen(f"pkill -f {appName}")
    else:
        await ctx.send("Can't quit the app.")
        await asyncio.sleep(3)
