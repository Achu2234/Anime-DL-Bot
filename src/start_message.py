# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/63f34269d6293f55f1798.jpg"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Welcome to Aɳιɱҽ X DL Bσƚ, Here you can Download all Anime for FREE 😁!!!

__Please read all the instructions about the bot before surfing on...__

Join @Animemusicarchive6 for updates and @Yeageristbots for support

See /whats_new to know about latest updates...""", reply_markup=reply_markup, parse_mode="markdown")
