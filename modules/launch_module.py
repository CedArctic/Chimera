# Module: launch
# Description: Lauches a custom shortcut in the shortcuts directory
# Usage: !launch [shortcut]
# Dependencies: os, configs

import os, configs

async def launch(ctx, shortcut):

    if configs.operating_sys == "Windows":
        if (shortcut==None) or not (os.path.isfile("shortcuts/" + shortcut + ".lnk")):
            await ctx.send("No such shortcut in your shortcuts folder")
        else:
            await ctx.send("Starting " + shortcut)
            os.startfile("shortcuts\\" + shortcut + ".lnk")
    else:
        await ctx.send("Module not yet supported on Linux and macOS")