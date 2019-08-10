# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os

import os, time, asyncio, configs


async def lock(ctx, seconds=0):
    await ctx.send("Locking system.")

    if seconds != 0:
        time.sleep(seconds)

    if configs.operating_sys == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif configs.operating_sys == "Linux":
        os.popen('gnome-screensaver-command --lock')
    else:
        await ctx.send("Can't lock system.")
        await asyncio.sleep(3)
