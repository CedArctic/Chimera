# Module: helpme
# Description: Allows file download, upload and system navigation
# Usage: !helpme [command]
# Dependencies: None


async def helpme(ctx, command=None):
    readme = open('readme.md', 'r')
    readme = readme.read()
    readme = readme.split('## ')

    if command:
        features = [x for x in readme if x.split('\n', 1)[0] == 'Features Documentation:']
        features = features[0]

        message = features

        features = features.split('* ')
        feature = [x for x in features[1:] if x.replace("!", "").split(' ', 1)[0] == command]
        feature = feature[0]

        message = "```{}```".format(feature)
    else:
        features = [x for x in readme if x.split('\n', 1)[0] == 'Features List:']
        features = features[0]

        message = "```{}```".format(features)

    await ctx.send(message)
