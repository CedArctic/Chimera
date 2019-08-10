# Module: shutdown
# Description: Shuts system down
# Usage: !shutdown or !shutdown secondsToShutdown
# Dependencies: time, os

import time, os, asyncio, configs


async def shutdown(ctx, seconds=0):
    await ctx.send("Shutting system down.")
    if configs.operating_sys == "Windows":
        if time != 0:
            time.sleep(seconds)
        os.system("Shutdown.exe -s -t 0")
    elif configs.operating_sys == "Linux":
        if time != 0:
            time.sleep(seconds)
        os.system("shutdown")
    else:
        await ctx.send("Can't shutdown system.")
        await asyncio.sleep(3)
