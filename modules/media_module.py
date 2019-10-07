# Module: media
# Description: Controls Media Features
# Usage: !media command or !media command times
# Dependencies: pynput, time, helpers

import asyncio, configs
from lib import helpers


async def media(ctx, command, times=1):
    media_control = helpers.MediaControlAdapter(configs.operating_sys)
    switcher = {
        'vol-up': media_control.up_volume,
        'vol-down': media_control.down_volume,
        'vol-mute': media_control.mute_volume,
        'next': media_control.media_next,
        'prev': media_control.media_previous,
        'stop': media_control.media_stop,
        'play': media_control.media_play_pause,
        'pause': media_control.media_play_pause
    }

    for time in range(0, times):
        switcher[command]()
        await asyncio.sleep(0.5)

    await ctx.send('Media Adjusted!')
