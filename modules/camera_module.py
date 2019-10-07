# Module: camera
# Description: Records a video or takes a photo (no audio)
# Usage: !camera command time
# Dependencies: cv2, datetime, timedelta

import os, asyncio, configs, discord

async def camera(ctx, command, time=5):
    await ctx.send('Recording!')
    python_alias = configs.PYTHON_ALIAS

    if command == 'photo':
        # CameraControl.photo_capture()
        os.system("{} lib/camera_control.py photo".format(python_alias))  # workaround
        await ctx.send(file=discord.File('photo.jpg'))

    if command == 'video':
        # await CameraControl.video_capture(time=time)
        os.system("{} lib/camera_control.py video {}".format(python_alias, time))  # workaround
        await ctx.send(file=discord.File('video.avi'))