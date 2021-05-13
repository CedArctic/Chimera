# Module: powershell
# Description: Executes powershell command
# Usage: !powershell "command"
# Dependencies: time, os

import os, asyncio, configs


async def powershell(ctx, cmnd):
    if configs.operating_sys == "Windows":
        await ctx.send("Executing in powershell: " + cmnd)
        cmnd_result = os.popen(f"powershell {cmnd}").read()
        if configs.initial_display_output:
            await ctx.say(cmnd_result)
    else:
        await ctx.send("Powershell is only available in Windows")
    await asyncio.sleep(3)
