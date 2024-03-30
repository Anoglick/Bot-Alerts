import asyncio
from sqlalchemy import and_, select, text, insert, func, cast

from dataBase.db import asessionmaker, async_engine, Base
from dataBase.models.models import User, Anime

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

def main():
    create_tables()

if __name__ == '__main__':
    asyncio.run(create_tables())
