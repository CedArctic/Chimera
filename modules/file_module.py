# Module: file
# Description: Allows file download, upload and system navigation
# Usage: !file [command] [[path]|[times]]
# Dependencies: filesystem_control, requests

import configs, requests, discord
from lib.filesystem_control import FileSystemControl


async def file(ctx, command, *args):
    filesystem_control = FileSystemControl(configs.initial_path)
    await filesystem_control.load_path_from_memory()

    async def set_absolute_path(path):
        new_path = await filesystem_control.set_path(path, False)
        return f'Current location set to {new_path}'

    async def set_relative_path(path):
        new_path = await filesystem_control.set_path(path, True)
        return f'Current location set to {new_path}'

    async def retrive_file(path=None):
        file_path = await filesystem_control.retrieve_file(path)
        await ctx.send(file=discord.File(file_path))

    async def save_file(path=None):

        filename = ctx.message.attachments[0].filename
        url = ctx.message.attachments[0].url

        r = requests.get(url, allow_redirects=True)
        if r.status_code / 100 != 2:
            raise Exception('Download request from Discord returned {}'.r.status_code)
        file = r.content

        file_path = await filesystem_control.save_file(file, filename, path)
        return f'File Saved on {file_path}'

    async def download_file(url=None, path=None):

        if url == None:
            return 'No direct file URL was provided'

        filename = url[url.rfind("/") + 1:]

        r = requests.get(url, allow_redirects=True)
        if r.status_code / 100 != 2:
            raise Exception('Download request from Discord returned {}'.r.status_code)
        file = r.content

        file_path = await filesystem_control.save_file(file, filename, path)
        return f'File Saved on {file_path}'

    async def list_directory():
        dir_list = await filesystem_control.list_directory()
        result = "Directory items:\n"
        for item in dir_list:
            result += f"`{item.name}`\n"
        return result

    switcher = {
        'absolute': set_absolute_path,
        'relative': set_relative_path,
        'list': list_directory,
        'retrieve': retrive_file,
        'save': save_file,
        'download': download_file
    }

    if len(args) > 0:
        message = await switcher[command](*args)
    else:
        message = await switcher[command]()
    if message:
        await ctx.send(message)
