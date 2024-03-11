import asyncio
from sqlalchemy import and_, select, text, insert, func, cast, update

from .db import asessionmaker, async_engine, Base
from .models import User, Anime


async def check_count(user_id):
    async with asessionmaker() as session:
        query = (
            select(User)
            .filter_by(user_id=user_id)
        )
        
        res = await session.execute(query)
        print(res.all())
        return True


async def add_title(user_id, username, title, about_anime):
    async with asessionmaker() as session:
        # user = await check_count(user_id)
        # if user:
            # print('Такой пользователь уже есть')
            query = (
                 update(User)
                 .filter_by(user_id=user_id)
                 .values(count_titles=User.count_titles + 1)
            )
            # await session.refresh(query)
            await session.execute(query)
            await session.commit()

            
            # print(user.count_titles)
            # anime_stmt = Anime(user_ids=user_id, title=title, about_title=about_anime)
            # session.add(anime_stmt)
            # await session.refresh(user)
            # await session.commit()
        # else:
        #     stmt = User(user_id=user_id,username=username)
        #     anime_stmt = Anime(user_ids=user_id, title=title, about_title=about_anime)
        #     session.add(stmt)
        #     session.add(anime_stmt)
        #     await session.commit()