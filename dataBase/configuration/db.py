from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .config_bd import settings


async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg, 
    echo=False)

asessionmaker = async_sessionmaker(
    async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False)


class Base(DeclarativeBase):
    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f'{col}={getattr(self, col)}')
        return f'<{self.__class__.__name__} {", ".join(cols)}>'
    