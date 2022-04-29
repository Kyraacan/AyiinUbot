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


async def inline_query(
        self: 'TelegramClient',
        bot: 'hints.DialogLike',
        query: str,
        *,
        dialog: 'hints.DialogLike' = None,
        offset: str = None,
        geo_point: '_tl.GeoPoint' = None) -> _custom.InlineResults:
    bot = await self._get_input_peer(bot)
    if dialog:
        peer = await self._get_input_peer(dialog)
    else:
        peer = _tl.InputPeerEmpty()

    try:
        result = await self(_tl.fn.messages.GetInlineBotResults(
            bot=bot,
            peer=peer,
            query=query,
            offset=offset or '',
            geo_point=geo_point
        ))
    except errors.BotResponseTimeoutError:
        raise asyncio.TimeoutError from None

    return _custom.InlineResults(self, result, entity=peer if dialog else None)


@ayiin_cmd(pattern="string(?:\\s|$)([\\s\\S]*)")
async def test_string(event):
    ayiin = await eor(event, get_string("com_1"))
    reply_to_id = await reply_id(event)
    buttons = "Silahkan klik Dibawah Ini Untuk Membuat String Anda"
    buttons = [
        [
           Button.url("String Via Bot", "https://t.me/AyiinStringRobot"),
           Button.url("String Via Web", "https://repl.it/@AyiinXd/AyiinString?lite=1&outputonly=1"),
        ]
    ]
    results = await event.client.inline_query(BOT_USERNAME, buttons)
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
