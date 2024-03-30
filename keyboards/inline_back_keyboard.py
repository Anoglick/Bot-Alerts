from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

from dataBase.orm_database.orm_sqlalchemy import GetDB


class Menu(CallbackData, prefix="menu"):
    level: int
    category: str | None = None
    title: str | None = None
    something: str | None = None


async def reading(level: int):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Аниме📺', callback_data=Menu(level=level+1, category='Anime').pack()),
        InlineKeyboardButton(text='Манга/Манхва/Маньхуа📖', callback_data=Menu(level=level+1, category='Comics').pack()),
    )
    
    return builder.as_markup(resize_keyboard=True)


async def catalog_anime(level, user_id: int):
    keyb = (await GetDB().get_anime_titles(user_id))
    builder = InlineKeyboardBuilder()
    for anime in keyb:
        builder.button(text=anime, callback_data=Menu(level=level+1, category='Anime', title=(f'{anime}')))
    builder.button(text='⬅', callback_data=Menu(level=level-1, something=(f'Back')))  
    builder.adjust(2, 1)
    
    return builder.as_markup(resize_keyboard=True)


async def catalog_comics(level, user_id: int):
    keyb = (await GetDB().get_comics_titles(user_id))
    builder = InlineKeyboardBuilder()
    for comics in keyb:
        builder.button(text=comics, callback_data=Menu(level=level+1, category='Comics', title=(f'{comics}')))
    builder.button(text='⬅', callback_data=Menu(level=level-1, something=(f'Back')) )
    builder.adjust(2, 1)
    
    return builder.as_markup(resize_keyboard=True)


async def back_delete_back(level: int, category: str, title: str):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='⬅', callback_data=Menu(level=level-1, category=category, title='Back').pack()),
        InlineKeyboardButton(text='❌', callback_data=Menu(level=level+1, category=category, title=f'{title}').pack()),
        InlineKeyboardButton(text='Каталог', callback_data=Menu(level=0, title='Catalog').pack()),
    ).adjust(2)
    
    return builder.as_markup(resize_keyboard=True)


async def backup(level, category):
    builder = InlineKeyboardBuilder()
    builder.button(text='⬅', callback_data=Menu(level=level-2, category=category, something='Back')) 
    builder.adjust(2, 1)
    
    return builder.as_markup(resize_keyboard=True)