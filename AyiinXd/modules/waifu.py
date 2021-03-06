# imported from ppe-remix by @heyworld & @DeletedUser420
# Based Code by @adekmaulana
# Improve by @aidilaryanto


from secrets import choice

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, deEmojify, edit_delete


@ayiin_cmd(pattern="waifu(?: |$)(.*)")
async def waifu(animu):
    text = animu.pattern_match.group(1)
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await animu.answer("`No text given, hence the waifu ran away.`")
            return
    animus = [15, 30, 32, 33, 40, 41, 42, 48, 55, 58]
    sticcers = await animu.client.inline_query(
        "stickerizerbot", f"#{choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await edit_delete(
            animu,
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`",
        )


CMD_HELP.update(
    {
        "waifu": f"**Plugin : **`waifu`\
        \n\n  »  **Perintah :** `{cmd}waifu <text>`\
        \n  »  **Kegunaan : **Untuk Mengcuston sticer anime dengan text yg di tentukan.\
    "
    }
)
