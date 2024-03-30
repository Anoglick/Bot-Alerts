from aiogram import Bot
from aiogram.enums import ParseMode
from dotenv import load_dotenv

import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)

# DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT