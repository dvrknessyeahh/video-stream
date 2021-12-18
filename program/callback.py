# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋 **Hallo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
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


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Panduan Dasar untuk menggunakan bot ini:**

1.) **Pertama, tambahkan saya ke grup Anda.**
2.) **Kemudian, promosikan saya sebagai administrator dan berikan semua izin kecuali Admin Anonim.**
3.) **Setelah mempromosikan saya, ketik /reload di grup untuk me-refresh data admin.**
3.) **Tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /userbotjoin untuk mengundangnya.**
4.) **Aktifkan obrolan video terlebih dahulu sebelum mulai memutar video/musik.**
5.) **Terkadang, memuat ulang bot dengan menggunakan perintah /reload dapat membantu Anda memperbaiki beberapa masalah.**

⛧ **Jika userbot tidak join ke video chat, pastikan video chat sudah aktif, atau ketik /userbotleave lalu ketik /userbotjoin lagi.**

⛧ **Jika Anda memiliki pertanyaan lanjutan tentang bot ini, Anda dapat menceritakannya pada obrolan dukungan saya di sini: @{GROUP_SUPPORT}**

⛧ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""👋 **Hallo [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

⛧ **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

⛧ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Kembali", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 di sini adalah perintah dasar:

⛧ /play (nama lagu/tautan) - putar musik di obrolan video
⛧ /vplay (nama video/tautan) - putar video di obrolan video
⛧ /vstream - putar video langsung dari yt live/m3u8
⛧ /playlist - menampilkan daftar putar
⛧ /video (permintaan) - unduh video dari youtube
⛧ /song (query) - unduh lagu dari youtube
⛧ /lyric (query) - memo lirik lagu
⛧ /search (query) - cari link video youtube

⛧ /ping - tampilkan status bot ping
⛧ /uptime - tampilkan status uptime bot
⛧ /alive - tampilkan info bot hidup (dalam grup)

⛧ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 ini perintah adminnya:

⛧ /pause - jeda streaming
⛧ /resume - lanjutkan streaming
⛧ /skip - beralih ke berikutnya
⛧ /stop - stop streaming
⛧ /vmute - bisukan userbot di obrolan suara
⛧ /vunmute - membunyikan userbot di obrolan suara
⛧ /volume `1-200` - sesuaikan volume musik (userbot harus admin)
⛧ /reload - muat ulang bot dan segarkan data admin
⛧ /userbotjoin - undang userbot untuk bergabung dengan grup
⛧ /userbotleave - perintahkan userbot keluar dari grup

⛧ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 di sini adalah perintah sudo:

⛧ /rmw - bersihkan semua file mentah
⛧ /rmd - bersihkan semua file yang diunduh
⛧ /sysinfo - tampilkan informasi sistem
⛧ /update  - perbarui bot Anda ke versi terbaru
⛧ /restart - mulai ulang bot Anda
⛧ /leaveall - perintahkan userbot keluar dari semua grup

⛧ __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("Anda adalah Admin Anonim !\n\n» kembali ke akun pengguna dari hak admin.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⛧ hanya admin dengan izin mengelola obrolan suara yang dapat mengetuk tombol ini !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **pengaturan dari** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ tidak ada yang sedang streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("⛧ hanya admin dengan izin mengelola obrolan suara yang dapat mengetuk tombol ini !", show_alert=True)
    await query.message.delete()
