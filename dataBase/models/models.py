from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..configuration.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str]
    count_titles: Mapped[int] = mapped_column(default=0)
    limit_count: Mapped[int] = mapped_column(default=10)


    anime_id: Mapped[list['Anime']] = relationship(
        back_populates='user',
    )
    comics_id: Mapped[list['Comics']] = relationship(
        back_populates='user',
    )


class Anime(Base):
    __tablename__ = 'anime'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[list[int]] = mapped_column(
        ForeignKey(
            'users.user_id', 
            ondelete='CASCADE',
        ),
    )
    title: Mapped[str]
    # short_title: Mapped[str] = mapped_column(default=None)
    episodes: Mapped[str] = mapped_column(default=0)
    status: Mapped[str] = mapped_column(default=None)
    about_title: Mapped[str]
    url: Mapped[str]

    user: Mapped[list['User']] = relationship(
        back_populates='anime_id'
    )


class Comics(Base):
    __tablename__ = 'comics'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.user_id', 
            ondelete='CASCADE',
        ),
    )
    title: Mapped[str]
    # short_title: Mapped[str] = mapped_column(default=None)
    chapters: Mapped[str] = mapped_column(default=0)
    comics_type: Mapped[str] = mapped_column(default="Неизвестно")
    comics_format: Mapped[str] = mapped_column(default=None)
    year: Mapped[str] = mapped_column(default=None)
    status: Mapped[str] = mapped_column(default=None)
    about_title: Mapped[str]
    url: Mapped[str]

    user: Mapped[list['User']] = relationship(
        back_populates='comics_id'
    )

