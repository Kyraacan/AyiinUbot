#
#
#
#

import re
import os

from pprint import pprint
from io import BytesIO
from telethon import Button, custom, events

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOT_USERNAME, CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, bash, eod, eor
from Stringyins import get_string


# Used for Formatting Eval Code, if installed
try:
    import black
except ImportError:
    black = None

p, pp = print, pprint


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


@ayiin_cmd(pattern="bash(?: |$)(.*)")
async def _(event):
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await event.eor(get_string("devs_1"), time=10)
    xx = await event.eor(get_string("com_1"))
    reply_to_id = event.reply_to_msg_id or event.id
    stdout, stderr = await bash(cmd)
    OUT = f"**☞ BASH\n\n• COMMAND:**\n`{cmd}` \n\n"
    if stderr:
        OUT += f"**• ERROR:** \n`{stderr}`\n\n"
    if stdout:
        _o = stdout.split("\n")
        o = "\n".join(_o)
        OUT += f"**• OUTPUT:**\n`{o}`"
    if not stderr and not stdout:
        OUT += "**• OUTPUT:**\n`Success`"
    if len(OUT) > 4096:
        Ayiin = OUT.replace("`", "").replace("**", "").replace("__", "")
        with BytesIO(str.encode(Ayiin)) as out_file:
            out_file.name = "bash_yins.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                thumb="AyiinXd/resources/logo.jpg",
                allow_cache=False,
                caption=f"`{cmd}`" if len(cmd) < 998 else None,
                reply_to=reply_to_id,
            )

            await xx.delete()
    else:
        await xx.edit(OUT)


@ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    ayiin = await eor(event, get_string("com_1"))
    buttons = build_keyboards(Y_BUTTONS)
    if buttons:
        try:
            results = await event.client.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "string",
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
        "yinstools": f"**Plugin :** `yinstools`\
        \n\n  •  **Perintah :** `{cmd}bash <command>`\
        \n  •  **Kegunaan : **__Menjalankan perintah linux di telegram.__\
        \n\n  •  **Perintah :** `{cmd}string`\
        \n  •  **Kegunaan :** Mendapatkan Bot String dan Web String.\
    "
    }
)
