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
from driver.veez import user
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
        f"""👋 **Hallo {message.from_user.mention()} !**\n
⛧ **Saya adalah [{BOT_NAME}](https://t.me/{BOT_USERNAME}) Saya bisa membantu Anda memutar musik dan video di grup melalui obrolan video Telegram baru!**

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke Grup Anda ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("📚 CMD", callback_data="cbcmds"),
                    InlineKeyboardButton("👨‍💻 Owner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [InlineKeyboardButton("❓ Panduan Dasar", callback_data="cbhowtouse")],
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
                InlineKeyboardButton("👥 Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hallo {message.from_user.mention()}, Saya adalah {BOT_NAME}**\n\n⛧ Bot is working normally\n⛧ My Master: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n⛧ Bot Version: `v{__version__}`\n⛧ Pyrogram Versi: `{pyrover}`\n⛧ Python Versi: `{__python_version__}`\n⛧ PyTgCalls Versi: `{pytover.__version__}`\n⛧ Status Aktif: `{uptime}`\n\n**Terima kasih telah Menambahkan saya di sini, untuk memutar video & musik di obrolan video Grup Anda** "

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
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **waktu aktif:** `{uptime}`\n"
        f"• **waktu mulai:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "❤️ **Terima kasih telah menambahkan saya ke Grup !**\n\n"
                 "**Promosikan saya sebagai administrator Grup, jika tidak saya tidak akan dapat bekerja dengan baik, dan jangan lupa ketik /userbotjoin untuk mengundang asisten.**\n\n"
                 "**Setelah selesai, ketik** /reload",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("💭 Group", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("👤 Assistant", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
