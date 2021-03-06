from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""ð **Há´á´Êá´ {message.from_user.mention()}**\n
TÊÉªs Éªs á´Êá´ á´á´Êá´ Êá´á´...!**
âââââââââââââââââââ
â£Â» á´á´ á´á´ê±Éªá´ á´Êá´Êá´Ê Êá´á´. 
â£Â» ÊÉªÉ¢Ê Ç«á´á´ÊÉªá´Ê á´á´ê±Éªá´.
â£Â» á´ Éªá´á´á´ á´Êá´Ê ê±á´á´á´á´Êá´á´á´.
â£Â» á´á´á´ á´É´á´á´á´ ê°á´á´á´á´Êá´ê±.
â£Â» ê±á´á´á´Êê°á´ê±á´ ê±á´á´á´á´.
âââââââââââââââââââ
á´á´ê±ÉªÉ¢É´á´á´ ÊÊ :** [á´á´Êá´ Êá´á´](https://t.me/xender_xd)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("á´á´á´á´á´É´á´ ÊÉªê±á´", callback_data="cbcmds"),
                ],[
                    InlineKeyboardButton(
                        "ê±á´á´á´á´Êá´", url=f"https://t.me/come_and_feel_music"
                    ),
                    InlineKeyboardButton(
                        "á´á´á´á´á´á´ê±", url=f"https://t.me/the_arc_network"
                    ),
                ],[
                    InlineKeyboardButton(
                        "ð á´á´á´  Êá´ÊÊ ð",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ê±á´á´á´á´Êá´", url=f"https://t.me/come_and_feel_music"),
                InlineKeyboardButton(
                    "á´á´á´á´á´á´ê±", url=f"https://t.me/come_and_feel_music"
                ),
            ],[
                InlineKeyboardButton("á´ÊÊ ÉªÉ´ê°á´ Êá´Êá´", url=f"https://t.me/come_and_feel_music"),
            ]
        ]
    )

    alive = f"**Êá´á´Êá´ {message.from_user.mention()}, á´ÊÉªê± Éªê± á´Êá´ á´á´Êá´ Êá´á´.**\n\nÂ» á´¡á´Êá´ÉªÉ´É¢ É´á´Êá´á´ÊÊÊ\nÂ» á´á´ á´á´ê±á´á´Ê : [á´á´Êá´ Êá´á´](https://t.me/xender_xd)\nÂ» Êá´á´ á´ á´Êê±Éªá´É´ : `v{__version__}`\nÂ» á´ÊÊá´ á´ á´Êê±Éªá´É´ : `{pyrover}`\nÂ» á´Êá´Êá´É´ á´ á´Êê±Éªá´É´ : `{__python_version__}`\nÂ» á´Êá´É¢á´á´ÊÊê± : `{pytover.__version__}`\nÂ» á´á´á´Éªá´á´ : `{uptime}`\n\n**á´ÊÉªê± Éªê± á´Êá´ á´á´ á´á´ê±Éªá´ á´Êá´Êá´Ê Êá´á´ á´á´ê±ÉªÉ¢É´á´á´ á´É´á´ á´Êá´á´á´á´á´ ÊÊ xá´É´á´á´Ê xá´  É´á´á´á´¡á´Êá´, á´Êá´É´á´á´ á´ á´ÊÊ á´á´á´Ê ê°á´Ê á´á´á´ÉªÉ´É¢ Êá´Êá´..**\n\nÂ© @come_and_feel_music"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("**Â» á´á´Êá´ Êá´á´ á´á´É´É¢ ê°Êá´á´ á´á´Êá´ á´á´sÉªá´ É´á´á´á´¡á´Êá´ ê±á´Êá´ á´Ê..**\n\nð `PONG!!`\n" f"â¡ï¸ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "**ÊÊá´á´á´ á´á´á´ Êá´á´ ê±á´á´á´á´ê±.**\n\n"
        f"â¢ **á´á´á´Éªá´á´ :** `{uptime}`\n"
        f"â¢ **ê±á´á´Êá´ á´á´ :** `{START_TIME_ISO}`"
    )

@Client.on_message(filters.command("pavan") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**á´ÊÉªê± Éªê± á´Êá´ á´á´ Êá´á´ á´¡ÊÉªá´Ê Éªê± ê±á´á´á´Éªê°Éªá´á´ÊÊÊ á´á´ê±ÉªÉ¢É´á´á´ ÊÊ xá´É´á´á´Ê xá´.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "á´ÊÊ ÉªÉ´ê°á´ Êá´Êá´", url="https://t.me/catmusicworld")
                ]
            ]
        )
   )

@Client.on_message(filters.command("aayuu") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**á´ÊÉªê± Éªê± á´Êá´ á´á´ Êá´á´ á´¡ÊÉªá´Ê Éªê± ê±á´á´á´Éªê°Éªá´á´ÊÊÊ á´á´ê±ÉªÉ¢É´á´á´ ÊÊ xá´É´á´á´Ê xá´.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "á´ÊÊ ÉªÉ´ê°á´ Êá´Êá´", url="https://t.me/come_and_feel_music")
                ]
            ]
        )
   )
