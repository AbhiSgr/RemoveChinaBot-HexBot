import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Name Set Karna Padta Hai BC"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Félicitations! RemoveChinaBot Is Onto Destroying Sluts!`"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot kanged by:` [AbhiSagar](https://t.me/AbhiSagar)\n"
                     f"`99.99% of the Credits To:` [Akashi](https://t.me/emperor_akashi)")
