# Module: cmd
# Description: Executes cmd command
# Usage: !cmd "command"
# Dependencies: time, os

import os, asyncio, configs


async def cmd(ctx, cmnd):
    await ctx.send("Executing in command prompt: " + cmnd)
    cmnd_result = os.popen(cmnd).read()
    if configs.initial_display_output:
        await ctx.send(cmnd_result)
    await asyncio.sleep(3)
