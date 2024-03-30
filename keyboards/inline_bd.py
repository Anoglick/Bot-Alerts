from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup


def add_to():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Добавить', callback_data='Add'),
        InlineKeyboardButton(text='Убрать', callback_data='Delete'),
    )

    return builder.as_markup(resize_keyboard=True)


async def user_choice():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Аниме🙌', callback_data='Choice_Anime'),
        InlineKeyboardButton(text='Манга🌹/Манхва🐱‍🐉/Маньхуа🏴‍☠️', callback_data='Choice_Comics'),
    )
    
    return builder.as_markup(resize_keyboard=True)
