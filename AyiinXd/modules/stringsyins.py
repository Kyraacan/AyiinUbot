#
#
#

import re
import os

from telethon import Button, custom, events

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOT_USERNAME, CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor, reply_id
from Stringyins import get_string
from .button import BTN_URL_REGEX, build_keyboard


Y_BUTTONS = [
        [
           custom.Button.url("String Via Bot", "https://t.me/AyiinStringRobot"),
           custom.Button.url("String Via Web", "https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),
        ]
    ]


@ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    ayiin = await eor(event, get_string("com_1"))
    args = build_keyboard(Y_BUTTONS)
    if args:
            await eor(event, f"Silahkan klik Dibawah Ini Untuk Membuat String Anda\n\n {Y_BUTTONS[args]}")
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
