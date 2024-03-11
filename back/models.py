from pydantic import BaseModel

class Episode(BaseModel):
    episode: str | None = 'Следующего эпизода не существует'
    name: str | None = None
    date: str | None = None


class Title(BaseModel):
    name: str
    rating: str | None = 'Неизвестно'
    episodes: str
    status: str | None = None
    next_episode: Episode | None = None
    last_episode: Episode | None = None
    