from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup

def add_to():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Добавить', callback_data='Add'),
    )

    return builder.as_markup()


def reading():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Аниме📺', callback_data='Anime'),
        InlineKeyboardButton(text='Манга/Манхва/Маньхуа📖', callback_data='Comics'),
    )
    
    return builder.as_markup(resize_keyboard=True)