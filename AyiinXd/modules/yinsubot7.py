# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================


from time import sleep
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="cacad(?: |$)(.*)")
async def _(cacad):
    yins = await edit_or_reply(cacad, "**Cacad ๐**")
    sleep(2)
    await yins.edit("**Najis Akunnya Cacad ๐**")
    sleep(1)
    await yins.edit("**Hahahaha Cacad ๐คฃ**")
    sleep(2)
    await yins.edit("**Canda Akun Cacad ๐๐คฃ**")


@ayiin_cmd(pattern="hayo(?: |$)(.*)")
async def _(hylo):
    ayiin = await edit_or_reply(hylo, "**Hayolo ๐**")
    sleep(1)
    await ayiin.edit("**Hayoloo ๐**")
    sleep(1)
    await ayiin.edit("**Hayolooo ๐**")
    sleep(1)
    await ayiin.edit("**Hayoloooo ๐**")
    sleep(3)
    await ayiin.edit("**Hayolooooo ๐คฃ**")
    sleep(2)
    await ayiin.edit("**Haayolooooo ๐คฃ**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya?**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya? kasiaaaan** ๐")


# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================


CMD_HELP.update(
    {
        "yinsubot7": f"**Plugin : **`yinsubot7`\
        \n\n  ยป  **Perintah :** `{cmd}cacad`\
        \n  ยป  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  ยป  **Perintah :** `{cmd}hayolo`\
        \n  ยป  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
