# Module: echo
# Description: Turns command output display to discord chat on and off (works for !cmd and !powershell)
# Usage: !echo off or !echo on
# Dependencies: None

import configs, asyncio


async def echo(ctx, status):
    if status == "on":
        configs.initial_display_output = True
        await ctx.send("!cmd and !powershell output will be displayed in chat. ")
    elif status == "off":
        configs.initial_display_output = False
        await ctx.send("!cmd and !powershell output will be hidden from chat. ")
    else:
        await ctx.send("Parameter of echo can be off or on. ")
