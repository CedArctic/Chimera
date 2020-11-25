# Module: notification
# Description: Sends a notification to the computer
# Usage: !notification "Notification Content"
# Dependencies: plyer

import os
import asyncio
from plyer import notification as notifier
from plyer import utils as plyerUtils

async def notification(ctx, txt):
    await ctx.send("Sending Notification: " + txt)
    # Bypass plyer bug on macosx and use already included applescript
    if plyerUtils.platform == 'macosx':
        os.system("osascript -e 'display notification \"{}\"\'".format(txt))
    else:
        notifier.notify(title='Chimera Notification',
                    message=txt,
                    app_name="Chimera",
                    app_icon="icon.ico",
                    timeout=999999)
    await asyncio.sleep(3)
