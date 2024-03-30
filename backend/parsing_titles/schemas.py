from pydantic import BaseModel

class Episode(BaseModel):
    episode: str | None = "Следующего эпизода не существует"
    name: str | None = None
    date: str | None = None


class AnimeTitle(BaseModel):
    name: str
    rating: str | None = "Неизвестно"
    episodes: str
    status: str | None = None
    next_episode: Episode | None = None
    last_episode: Episode | None = None
    url: str | None = None
    

class MangaTitle(BaseModel):
    title: str
    rating: str
    chapters: str
    comics_type: str | None
    comics_format: str | None
    year: str | None
    status: str | None
    url: str
