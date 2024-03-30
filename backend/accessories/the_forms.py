from .config_for_the_forms import ANIME_SHORT_FORM, ANIME_LONG_FORM, MANGA_FORM
from ..parsing_titles.schemas import AnimeTitle, MangaTitle


async def anime_right_form(data: AnimeTitle) -> dict:
    title = data.name
    rating = data.rating
    episodes = data.episodes
    status = data.status
    url = data.url

    if data.next_episode is None and data.last_episode is None:
        return {
            "title": title,
            "episodes": episodes,
            "status": status,
            "about_title": ANIME_SHORT_FORM.format(
                title=title, rating=rating, 
                episodes=episodes, status=status,
            ),
            "url": url,
        }
    else:    
        dict_next_episode = data.next_episode
        next_episode = dict_next_episode.episode
        next_name = dict_next_episode.name
        next_date = dict_next_episode.date

        dict_last_episode = data.last_episode
        last_episode = dict_last_episode.episode
        last_name = dict_last_episode.name
        last_date = dict_last_episode.date

        return {
            "title": title,
            "episodes": episodes,
            "status": status,
            "about_title": ANIME_LONG_FORM.format(
                title=title, rating=rating, 
                episodes=episodes, status=status,
                next_episode=next_episode, next_name=next_name, next_date=next_date,
                last_episode=last_episode, last_name=last_name, last_date=last_date,
            ),
            "url": url,
        }
    

async def manga_right_form(data: MangaTitle) -> dict:
    title = data.title
    rating = data.rating
    chapters = data.chapters
    comics_type = data.comics_type
    comics_format = data.comics_format
    year = data.year
    status = data.status
    url = data.url
    
    return {
            "title": title,
            "chapters": chapters,
            "comics_type": comics_type,
            "comics_format": comics_format,
            "year": year,
            "status": status,
            "about_title": MANGA_FORM.format(
                title=title, rating=rating,
                manga_type=comics_type, format_at=comics_format,
                charters=chapters, status=status,
                year=year,
            ),
            "url": url,
        }