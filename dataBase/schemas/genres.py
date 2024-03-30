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
