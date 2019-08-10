# Module: lock
# Description: Locks system
# Usage: !lock or !lock secondsToLock
# Dependencies: time, os

import os, time, asyncio
import configs as Configs

async def lock(ctx, seconds=0):
    await ctx.send("Locking system.")

    if seconds != 0:
        time.sleep(seconds)

    if Configs.operating_sys == "Windows":
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif Configs.operating_sys == "Linux":
        os.popen('gnome-screensaver-command --lock')
    else:
        await ctx.send("Can't lock system.")
        await asyncio.sleep(3)