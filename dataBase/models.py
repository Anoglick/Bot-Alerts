from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str]
    count_titles: Mapped[int] = mapped_column(default=0)
    limit_count: Mapped[int] = mapped_column(default=10)


    anime_id: Mapped['Anime'] = relationship(
        back_populates='user',
    )
    # comics_id: Mapped[list['Comics']] = relationship(
    #     back_populates='user',
    # )


class Anime(Base):
    __tablename__ = 'anime'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_ids: Mapped[int] = mapped_column(
        ForeignKey(
            'users.user_id', 
            ondelete='CASCADE',
        ),
    )
    title: Mapped[str]
    about_title: Mapped[str]

    user: Mapped['User'] = relationship(
        back_populates='anime_id'
    )


# class Comics(Base):
#     __tablename__ = 'comics'

#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(
#         ForeignKey(
#             'users.user_id', 
#             ondelete='CASCADE',
#         )
#     )
#     title: Mapped[str]
#     count_titles: Mapped[int] = mapped_column(default=0)
#     limit_count: Mapped[int] = mapped_column(default=10)

#     user: Mapped['User'] = relationship(
#         'User',
#         back_populates='comics_id'
#     )

