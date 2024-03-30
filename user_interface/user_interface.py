from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiohttp import ContentTypeError

from keyboards.inline_back_keyboard import Menu
from keyboards.pagination import navigator
from backend.parsing_titles.manga import get_session_for_manga
from dataBase.schemas.genres import AnimeData, MangaData
from user_interface.configuration_interface.Fsmstate import Comics, Waiting
from backend.parsing_titles.anime_parsing import get_session
from backend.accessories.the_forms import manga_right_form, anime_right_form
from keyboards.inline_bd import add_to, user_choice
from user_interface.configuration_interface.text_to_user import HAVE_A_TITLE, NOT_F, NOT_FOUND_THE_TITLE, SUCCESS_, TEXT_HAS
from dataBase.orm_database.orm_sqlalchemy import GetDB, AddInDB

from datetime import datetime, timedelta


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello!")
    await AddInDB().add_user(message.from_user.id, message.from_user.username)


#                                                                                           ***Тайтл***


@router.message(Command('title'))
async def get_title(message: Message):
    await message.answer("Выберите категорию тайлта", reply_markup=await user_choice())


@router.callback_query((F.data == 'Choice_Anime') | (F.data == 'Choice_Comics'))
async def get_anime_title(call: CallbackQuery, state: FSMContext):
    if call.data == 'Choice_Anime':
        await state.set_state(Waiting.user_answer)
        await call.message.answer("Введите название тайтла")
    if call.data == 'Choice_Comics':
        print(1)
        await state.set_state(Comics.comics)
        await call.message.answer("Введите название тайтла")


@router.message(Waiting.user_answer, F.text)
async def get_user_anime(message: Message, state: FSMContext):
    try:
        await state.update_data(title=message.text)
        user_title = await get_session(message.text)
        answer_func = await anime_right_form(user_title)
        user = {'user_id': message.from_user.id}
        answer_func, user = user, answer_func
        answer_func.update(user)

        await message.answer(answer_func['about_title'], parse_mode=ParseMode.HTML, reply_markup=add_to())
        await state.clear()
        await state.update_data(data={'data': answer_func}, kwargs=1)
    except AttributeError:
        await message.answer(
            NOT_F,
            parse_mode=ParseMode.HTML,
        )



@router.message(Comics.comics, F.text)
async def get_user_manga(message: Message, state: FSMContext):
    print(2)
    try:
        await state.update_data(title=message.text)
        user_title = await get_session_for_manga(message.text)
        answer_func = await manga_right_form(user_title)
        user = {'user_id': message.from_user.id}
        answer_func, user = user, answer_func
        answer_func.update(user)

        await message.answer(answer_func['about_title'], parse_mode=ParseMode.HTML, reply_markup=add_to())
        await state.clear()
        await state.update_data(data={'data': answer_func}, kwargs=2)
    except AttributeError:
        await message.answer(
            NOT_F,
            parse_mode=ParseMode.HTML,
        )

    except ContentTypeError:
        await message.answer(
            NOT_F,
            parse_mode=ParseMode.HTML,
        )

@router.callback_query(F.data == 'Add')
async def add_to_bd(call: CallbackQuery,  state: FSMContext):
    data = await state.get_data()
    genre, info_title = data['kwargs'], data['data']
    info_title['title'] = f'{info_title["title"][:21]}...'
    if genre == 1:
        add = await AddInDB().add_title(genre, AnimeData(**info_title))
    else:
        add = await AddInDB().add_title(genre, MangaData(**info_title))

    if add is None:
        await call.message.edit_text(
            HAVE_A_TITLE
        )
    elif add == True:
        await call.message.edit_text(
            SUCCESS_, 
            parse_mode=ParseMode.HTML
        )
    else:
        await call.message.edit_text(
            TEXT_HAS
        )

        
@router.callback_query(F.data == 'Delete')
async def add_to_bd(call: CallbackQuery,  state: FSMContext):
    await call.message.edit_text(NOT_FOUND_THE_TITLE)
    await state.set_state(Waiting.user_answer)


#                                                                                           ***End***


#                                                                                           ***Лист***


@router.message(Command('list'))
async def user_list(message: Message):
    text, kb = await navigator(
        level=0, 
        user_id=message.from_user.id, 
    )

    await message.answer(text, reply_markup=kb)


@router.callback_query(Menu.filter())
async def process_anime_callback(call: CallbackQuery, callback_data: Menu):
    text, kb = await navigator(
        level=callback_data.level,
        user_id=call.from_user.id,
        category=callback_data.category,
        title=callback_data.title,
    )
    print(callback_data)

    await call.message.edit_text(text, reply_markup=kb)


@router.callback_query(F.data.regexp('Delete_'))
async def delete_user_title(call: CallbackQuery):
    new_data = call.data.split('Delete_')[1]
    await GetDB().delete_title(call.from_user.id, new_data)
    await call.message.edit_text(
        'Тайтл убран из вашего списка!'
    )


@router.callback_query(F.data == 'Catalog')



@router.callback_query(F.data == 'Comics')
async def anime_list(call: CallbackQuery):
    await call.message.edit_text(
        """
        Манга/Манхва/Маньхуа📖 📺\n
        """
    )
#                                                                                           ***End***

