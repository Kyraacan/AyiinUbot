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

@ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    ayiin = await eor(event, get_string("com_1"))
    reply_to_id = await reply_id(event)
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(
            event, "**Teks apa yang harus saya gunakan di pesan button?**"
        )
    text = "Silahkan klik Dibawah Ini Untuk Membuat String Anda"
    buttons = [
        [
           Button.url("String Via Bot", "https://t.me/AyiinStringRobot"),
           Button.url("String Via Web", "https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),
        ]
    ]
    catinput = f"{text} " + buttons
    results = await event.client.inline_query(BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


CMD_HELP.update(
  {
        "stringyins": f"**Plugin :**`stringyins`\
        \n\n  •  **Perintah :** `{cmd}stringyins`\
        \n  •  **Kegunaan :** Mendapatkan Bot String dan Web String.\
  "
  }
)
