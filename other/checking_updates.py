import asyncio
from aiogram import Router
from aiogram.enums import ParseMode

from backend.accessories.the_forms import anime_right_form
from dataBase.orm_database.orm_sqlalchemy import GetDB
from backend.parsing_titles.anime_parsing import get_session

#! This is a bad implementation. 
#! Needs to be update

router = Router()


@router.message()
async def checking(bot):
    result = await GetDB().get_episodes_and_url_db()
    for i in range(len(result)):
        print(1)
        last_episode, url = result[i][0], result[i][1]
        info_title = await get_session(url)
        if info_title.episodes != last_episode:
            print(f'{url} - прошлый эпизод {last_episode} - новый эпизод {info_title.episodes}')
            answer_func = await anime_right_form(info_title)


            await GetDB().update_episodes_and_url_db(answer_func["title"], answer_func)
            alerts = await GetDB().user_alert(answer_func["title"])
            for i in alerts:
                w = f'У тайлта <b>{answer_func["title"]}"</b> вышла <b>новая {answer_func["episodes"]}</b> серия!'
                await bot.send_message(i, w, parse_mode=ParseMode.HTML)
        print(f'{url} - нет изменений')

