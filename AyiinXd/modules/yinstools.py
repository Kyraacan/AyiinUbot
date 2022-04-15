#
#
#
#

from io import BytesIO


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.utils import ayiin_cmd, edit_delete, edit_or_reply

# Used for Formatting Eval Code, if installed
try:
    import black
except ImportError:
    black = None

from . import *

@ayiin_cmd(pattern="bash(?: |$)(.*)")
async def _(event):
    try:
        cmd = event.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await edit_delete(event, "`Beri perintah yang bener bego...`")
    xx = await edit_or_reply(event, "`Processing tod...`")
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


CMD_HELP.update(
    {
        "yinstools": f"**Plugin :** `yinstools`\
        \n\n  •  **Perintah :** `{cmd}bash <command>`\
        \n  •  **Kegunaan : **__Menjalankan perintah linux di telegram.__\
    "
    }
)
