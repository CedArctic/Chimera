# Module: notification
# Description: Sends a notification to the computer
# Usage: !notification "Notification Content"
# Dependencies: plyer

import asyncio
from plyer import notification as notifier


async def notification(ctx, txt):
    await ctx.send("Sending Notification: " + txt)
    notifier.notify(title='Chimera Notification',
                    message=txt,
                    app_name="Chimera",
                    app_icon="icon.ico",
                    timeout=999999)
    await asyncio.sleep(3)
