#
#
#
#

from telethon import Button

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd import tgbot
from AyiinXd.utils import ayiin_cmd, edit_or_reply
from Stringyins import get_languages, language, get_string, set_key


@ayiin_cmd(pattern=r"lang(?: |$)(.*)")
async def setlang(event):
    await edit_or_reply(event, (get_string("com_1")))
    languages = get_languages()
    tutud = [
        Button.inline(
            f"{languages[yins]['natively']} [{yins.lower()}]",
            data=f"set_{yins}",
        )
        for yins in languages
    ]
    buttons = list(zip(tutud[::2], tutud[1::2]))
    if len(tutud) % 2 == 1:
        buttons.append((tutud[-1],))
    buttons.append([Button.inline("« Back", data="langs_yins")])
    await event.edit("List Of Available Languages.", buttons=buttons)


@ayiin_cmd(pattern=r"set(?: |$)(.*)")
async def settt(event):
    await edit_or_reply(event, (get_string("com_1")))
    lang = event.pattern_match.group(1).strip()
    languages = get_languages()
    language[0] = lang
    tgbot.del_key("language") if lang == "id" else tgbot.set_key("language", lang)
    await event.edit(
        f"Your language has been set to {languages[lang]['natively']} [{lang}].",
        buttons=[Button.inline("Back", data="lang")],
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
