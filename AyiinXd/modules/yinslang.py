#
#
#
#

import os

from telethon import Button, custom, events

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import BOT_USERNAME, CMD_HELP, bot
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_languages, language, get_string
from .button import BTN_URL_REGEX, build_keyboard


@ayiin_cmd(pattern=r"lang(?: |$)(.*)")
async def setlang(event):
    await event.eor(get_string("com_1"))
    languages = get_languages()
    if languages:
        try:
            yinslang = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "lang",
            )
            await yinslang[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )


@ayiin_cmd(pattern=r"set( id| en|$)(.*)")
async def settt(event):
    await event.eor(get_string("com_1"))
    lang = event.pattern_match.group(1).strip()
    languages = get_languages()
    language[0] = lang
    if not os.environ.get("lang"):
        os.environ.setdefault("language", "1")

    if lang == "id":
        try:
            os.environ.setdefault("language", lang)
            await event.edit(
                f"Your language has been set to {languages[lang]['asli']} [{lang}].",
            )
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )

    if lang == "en":
        try:
            os.environ.setdefault("language", lang)
            await event.edit(
                f"Your language has been set to {languages[lang]['asli']} [{lang}].",
            )
        except Exception as e:
            await eor(event, get_string("error_1").format(e)
                      )

CMD_HELP.update(
    {
        "yinslang": f"**Plugin :** `yinslang`\
        \n\n  •  **Perintah :** `{cmd}lang`\
        \n  •  **Kegunaan : **__Untuk Melihat Daftar Bahasa Yang Tersedia.__\
        \n\n  •  **Perintah :** `{cmd}set <nama_bahasa>`\
        \n  •  **Kegunaan : **__Untuk Mengubah Bahasa.__\
    "
    }
)
