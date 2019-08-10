# Module: say
# Description: Uses powershell and a TTS engine to make your computer say something
# Usage: !say "Something to say"
# Dependencies: time, os

import os, asyncio, configs


async def say(ctx, txt):
    if configs.operating_sys == "Windows":
        await ctx.send("Saying: " + txt)
        os.system(
            "powershell Add-Type -AssemblyName System.Speech; $synth = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $synth.Speak('" + txt + "')")
    elif configs.operating_sys == "Linux":
        await ctx.send("Saying: " + txt)
        os.system('spd-say "{}"'.format(txt))
    else:
        await ctx.send("Can't use TTS")
    await asyncio.sleep(3)
