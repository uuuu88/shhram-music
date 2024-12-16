from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic import app

@app.on_message(filters.regex("^مطور السورس$"))
def show_developer_info(client, message):
    developer_id = "1854384004"
    user = app.get_users(developer_id)

    if user.photo:
        photo_file = app.download_media(user.photo.big_file_id)
    else:
        photo_file = None

    bio = getattr(user, "bio", "No Bio")
    username = getattr(user, "username", "No Username")

    caption = f"Name: {user.first_name}\nID: {user.id}\nBio: {bio}\nUsername: @{username}"

    inline_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("⦗ ожидании ⦘", url=f"https://t.me/{username}")]]
    )

    # Send photo to the user who sent the command
    if photo_file:
        client.send_photo(
            chat_id=message.chat.id,
            photo=photo_file,
            caption=caption,
            reply_markup=inline_keyboard
        )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text=caption,
            reply_markup=inline_keyboard
        )
