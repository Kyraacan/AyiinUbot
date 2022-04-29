#
#
#

import re
import os

from telethon import Button, custom, events

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOT_USERNAME, CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


def build_keyboards(buttons):
    keyb = []
    for btn in buttons:
        if btn[0] and keyb:
            keyb[0].append(Button.url(btn[0], btn[0]))
        else:
            keyb.append([Button.url(btn[0], btn[0])])
    return keyb


Y_BUTTONS = [
        [
           custom.Button.url("Bᴏᴛ Sᴛʀɪɴɢ", "https://t.me/AyiinStringRobot"),
           custom.Button.url("Rᴇᴘʟɪᴛ Sᴛʀɪɴɢ", "https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),
        ],
        [
           custom.Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/AyiinXdSupport"),
        ],
    ]


@ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    ayiin = await eor(event, get_string("com_1"))
    yins = build_keyboards(Y_BUTTONS)
    if yins:
            texts = "Silahkan klik Dibawah Ini Untuk Membuat String Anda"
            await eor(event, f"{texts(yins)}")
    else:
        try:
            results = await event.client.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@AyiinXdSupport",
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )


CMD_HELP.update(
  {
        "stringyins": f"**Plugin :**`stringyins`\
        \n\n  •  **Perintah :** `{cmd}stringyins`\
        \n  •  **Kegunaan :** Mendapatkan Bot String dan Web String.\
  "
  }
)
