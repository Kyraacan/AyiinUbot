#
#
#
#

from telethon import Button

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd import BTN_URL_REGEX, ibuild_keyboard, tgbot
from AyiinXd.utils import ayiin_cmd, edit_delete, edit_or_reply
from Stringyins import get_languages, get_string, language


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"lang")))
async def setlang(event):
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


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"set_")))
async def settt(event):
    lang = event.data_match.group(1).decode("UTF-8")
    languages = get_languages()
    language[0] = lang
    tgbot.del_key("language") if lang == "en" else tgbot.set_key("language", lang)
    await event.edit(
        f"Your language has been set to {languages[lang]['natively']} [{lang}].",
        buttons=[Button.inline("Back", data="lang")],
    )
