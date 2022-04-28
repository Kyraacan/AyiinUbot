#
#
#

import re
import os

from telethon import Button, custom, events

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, INLINE_PIC, bot
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string
from .button import BTN_URL_REGEX, build_keyboard

@bot.on(ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)"))
async def test_string(stringyins):
    ayiin = await eor(stringyins, get_string("com_1"))
    text = "Silahkan klik Dibawah Ini Untuk Membuat String Anda"
    buttons = [
        [
           (custom.Button.url("String Via Bot", "https://t.me/AyiinStringRobot"),),
           (custom.Button.url("String Via Web", "https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),),
        ]
    ]
    if INLINE_PIC:
        logoyins = INLINE_PIC
    await ayiin.edit(
           text,
           file=logoyins,
           link_preview=True,
           buttons=buttons,
    )


CMD_HELP.update(
  {
        "stringyins": f"**Plugin :**`stringyins`\
        \n\n  •  **Perintah :** `{cmd}stringyins`\
        \n  •  **Kegunaan :** Mendapatkan Bot String dan Web String.\
  "
  }
)
