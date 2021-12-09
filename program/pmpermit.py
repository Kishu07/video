from pyrogram import Client
from driver.veez import user as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@Client.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🔰ᴛʜɪs ɪs ᴀssɪsᴛᴀɴᴛ ᴏғ @Eula_musicbot ᴊᴏɪɴ @come_and_feel_music ғᴏʀ ᴜᴘᴅᴀᴛᴇᴅ🔰")
  return
