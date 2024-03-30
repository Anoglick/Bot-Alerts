from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

from dataBase.orm_database.orm_sqlalchemy import GetDB

from .text_kb import DELETE_USER_TITLE, PULL_TITLES, READ_LIST
from .inline_back_keyboard import backup, reading, back_delete_back, catalog_anime, catalog_comics


async def read_list(level):
    keyboard = await reading(level=level)

    return READ_LIST, keyboard
    

async def pull_titles(level: int, user_id:int, category: str):
    if category == 'Anime':
        kb = await catalog_anime(level=level, user_id=user_id)
    if category == 'Comics':
        kb = await catalog_comics(level=level, user_id=user_id)

    return PULL_TITLES, kb


async def anime_list_handler(level, category, title: str):
    title, kb = (
        await GetDB().get_anime_title_bd(title) 
        if category == 'Anime'
        else await GetDB().get_comics_title_bd(title)
    ), await back_delete_back(level, category, title)

    return title, kb


async def delete_user_title(level, user_id, category, title):
    await GetDB().delete_title(user_id, title, category)
    res = await backup(level=level, category=category)

    return DELETE_USER_TITLE, res


async def navigator(
    *,
    level: int,
    user_id: int | None = None,
    category: str | None = None,
    title: str | None = None,  
):
    if level == 0:
        return await read_list(level=level)
    if level == 1:
        return await pull_titles(level=level, user_id=user_id, category=category)
    if level == 2:
        return await anime_list_handler(level=level, category=category, title=title)
    if level == 3:
        return await delete_user_title(level=level, user_id=user_id, category=category, title=title)
