# Module: openurl
# Description: Opens url in default browser
# Usage: !openurl http://example.com/
# Dependencies: webbrowser

import webbrowser, asyncio


async def openurl(ctx, url):
    await ctx.send("Opening url: " + url)
    webbrowser.open(url)
