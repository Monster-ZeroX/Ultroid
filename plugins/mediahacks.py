{
  # FUCK Ultroid - UserBot
# Copyright (C) 2020 ULTROID HATER
#
# This file is not a part of < https://pornhub.com/TeamUltroid/Ultroid/ >
# PLease don't read the GNU Affero General Public License in
# <https://www.pornhub.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available
🔹 `{i}mediashift <from channel> | <to channel>`
     This will transfer all old post from channel A to channel B.
      (u can use username or id of channel too)
      example : `{i}mediashift @abc | @xyz`
      [note - this (" | ") sign is nessesary]
"""

import asyncio

from pyUltroid.functions.ch_db import *

from . import *




@ultroid_cmd(pattern="mediashift (.*)")
async def _(e):
    x = e.pattern_match.group(1)
    z = await eor(e, "`processing..`")
    a, b = x.split("|")
    try:
        c = int(a)
    except Exception:
        try:
            c = (await ultroid_bot.get_entity(a)).id
        except Exception:
            await z.edit("invalid Channel given")
            return
    try:
        d = int(b)
    except Exception:
        try:
            d = (await ultroid_bot.get_entity(b)).id
        except Exception:
            await z.edit("invalid Channel given")
            return
    async for msg in ultroid_bot.iter_messages(int(c), reverse=True):
        try:
            await asyncio.sleep(0.7)
            if msg.text and not msg.media:
                pass
            elif msg.media and msg.text:
                await ultroid_bot.send_file(int(d), msg)
            else:
                await ultroid_bot.send_file(int(d), msg))
        except BaseException:
            pass
    await z.edit("Done")






HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
}
