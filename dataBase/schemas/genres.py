from pydantic import BaseModel


class AnimeData(BaseModel):
    user_id: int
    title: str
    episodes: str
    status: str
    about_title: str
    url: str


class MangaData(BaseModel):
    user_id: int
    title: str
    chapters: str
    comics_type: str | None
    comics_format: str | None
    year: str | None
    status: str
    about_title: str
    url: str 


# class DifferentModel(AnimeData, MangaData):
#     def __init__(self, data: AnimeData | MangaData):
#         if isinstance(data, AnimeData):
#             self.__class__ = AnimeData
#         elif isinstance(data, MangaData):
#             self.__class__ = MangaData