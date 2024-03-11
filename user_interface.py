from aiogram import  F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from Fsmstate import Waiting
from back.anime_parsing import get_session
from back.the_form import right_form
from keyboards.inline_bd import add_to, reading
from dataBase.ormka import add_title

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello!")

#                                                                                           ***Лист***
@router.message(Command('list'))
async def read_list(message: Message):
    await message.answer("Категории:", reply_markup=reading())


@router.callback_query(F.data == 'Anime')
async def anime_list(call: CallbackQuery):
    await call.message.edit_text(
        """
        Аниме 📺\n
        """
    )


@router.callback_query(F.data == 'Comics')
async def anime_list(call: CallbackQuery):
    await call.message.edit_text(
        """
        Манга/Манхва/Маньхуа📖 📺\n
        """
    )



#                                                                                           ***Тайтл***
@router.message(Command('title'))
async def get_title(message: Message, state: FSMContext):
    await state.set_state(Waiting.user_answer)
    await message.answer("Введите название тайтла")


@router.message(Waiting.user_answer, F.text)
async def get_user_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    user_title = await get_session(message.text)
    answer_func = await right_form(user_title)

    await message.answer(answer_func, parse_mode=ParseMode.HTML, reply_markup=add_to())
    await state.clear()
    await state.update_data(title=message.text, data={'data': answer_func})


@router.callback_query(F.data == 'Add')
async def add_to_bd(call: CallbackQuery,  state: FSMContext):
    info_title = await state.get_data()
    # print(type(info_title['data']))
    await add_title(call.from_user.id, call.from_user.username, info_title['title'], info_title['data'])
    await call.message.edit_text(
        """
        Done✅\n
/list - посмотреть Ваш пул тайтлов!
        """,
        )


