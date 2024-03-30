from abc import ABC, abstractmethod
import asyncio
from sqlalchemy import and_, delete, select, text, insert, func, cast, update
from sqlalchemy.orm import joinedload

from ..configuration.abstractions import ABCAddInDB, ABCGetDB
from ..configuration.db import asessionmaker, async_engine, Base
from ..configuration.property_class import  ModelValidation,  Validation
from ..models.models import Comics, User, Anime
from ..schemas.genres import AnimeData, MangaData


class AddInDB(ABCAddInDB): 
    @staticmethod
    async def add_user(user_id: int, username: str) -> None:
        async with asessionmaker() as session:
            stmt = User(user_id=user_id, username=username)
            session.add(stmt)
            await session.commit()


    @staticmethod
    async def add_title(
        genre: int,
        data: AnimeData | MangaData
    ) -> None:
        async with asessionmaker() as session:
            user = await ModelValidation(User).check_user(session, data.user_id)
            if user:
                if genre == 1:
                    not_found = await ModelValidation(Anime).check_title(session, data.user_id, data.title)
                    if not_found:
                            query = (
                                update(User)
                                    .filter_by(user_id=data.user_id)
                                    .values(count_titles=User.count_titles + 1)
                            )
                            await session.execute(query)
                            anime_stmt = Anime(
                                user_id=data.user_id, title=data.title,
                                episodes=data.episodes, status=data.status,
                                about_title=data.about_title, url=data.url,
                            )
                            session.add(anime_stmt)
                            await session.commit()

                            return True
                    else:
                        return 'Тайтл есть'
                if genre == 2:
                    not_found = await ModelValidation(Comics).check_title(session, data.user_id, data.title)
                    if not_found:
                        query = (
                            update(User)
                                .filter_by(user_id=data.user_id)
                                .values(count_titles=User.count_titles + 1)
                        )
                        await session.execute(query)
                        manga_stmt = Comics(
                            user_id=data.user_id, title=data.title,
                            chapters=data.chapters, comics_type=data.comics_type,
                            comics_format=data.comics_format, year=data.year,
                            status=data.status, about_title=data.about_title, 
                            url=data.url,
                        )
                        session.add(manga_stmt)
                        await session.commit()     

                        return True
                    else:
                        return 'Тайтл есть'
            else:
                return None
    

class GetDB(ABCGetDB):
    @staticmethod
    async def get_anime_titles(user_id: int) -> list[str]:
        async with asessionmaker() as session:
            query = (
                select(Anime.title)
                    .filter_by(user_id=user_id)
                    .select_from(Anime)
            )
            result = await session.execute(query)

            return result.scalars().all()
    

    @staticmethod
    async def get_comics_titles(user_id: int) -> list[str]:
        async with asessionmaker() as session:
            query = (
                select(Comics.title)
                    .filter_by(user_id=user_id)
                    .select_from(Comics)
            )
            result = await session.execute(query)

            return result.scalars().all()


    @staticmethod
    async def get_anime_title_bd(title: str):
        async with asessionmaker() as session:
            query = (
                select(Anime.about_title)
                .filter_by(title=title)
                .select_from(Anime)
            )

            result = await session.scalar(query)
            return (result)
        

    @staticmethod
    async def get_comics_title_bd(title: str):
        async with asessionmaker() as session:
            query = (
                select(Comics.about_title)
                .filter_by(title=title)
                .select_from(Comics)
            )

            result = await session.scalar(query)
            return (result)
        


    @staticmethod
    async def get_episodes_and_url_db():
        async with asessionmaker() as session:
            query = (
                select(Anime.episodes, Anime.url)
                .select_from(Anime)
            )
            result = await session.execute(query)
            
            return result.all()
        

    @staticmethod
    async def update_episodes_and_url_db(title, data: dict):
        async with asessionmaker() as session:
            query = (
                update(Anime)
                .filter_by(title=title)
                .values(**data)
                
            )
            await session.execute(query)
            await session.commit()  

    
    @staticmethod
    async def user_alert(title):
        async with asessionmaker() as session:
            query = (
                select(Anime.user_id)
                .filter_by(title=title)
                .select_from(Anime)
            )
            result = await session.scalars(query)
            return result.all()


    @staticmethod
    async def delete_title(user_id: int, title: str, category: str) -> None:
        async with asessionmaker() as session:
            query = (
                update(User)
                    .filter_by(user_id=user_id)
                    .values(count_titles=User.count_titles - 1)
            )
            await session.execute(query)

            if category == 'Anime':
                stmt = (
                    delete(Anime)
                    .filter_by(user_id=user_id, title=title)
                )
            if category == 'Comics':
                stmt = (
                    delete(Comics)
                    .filter_by(user_id=user_id, title=title)
                )
            await session.execute(stmt)
            await session.commit()

