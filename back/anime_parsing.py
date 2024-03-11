import asyncio
import requests
from bs4 import BeautifulSoup
from lxml import html
from aiohttp import ClientSession

from .data_url_headers import all_components
from .models import Title


async def get_title(session, name: str) -> str:
    async with session.get(url=all_components.url + name, headers=all_components.headers) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')

        first_title = (
            soup
            .find('div', class_='row').find_next()
            .find('div', class_='card border-0').find('a')
            .get('href')
        )

        return await tasker(session, first_title)


async def tasker(session, title_urls: str) -> Title:
    async with session.get(url=title_urls, headers=all_components.headers) as response:
        soup = BeautifulSoup(await response.text(), 'lxml')
        name = soup.find(class_='anime-title').find('h1').text
        rating = soup.find('span', class_='rating-value').text if soup.find('span', class_='rating-value') else 'Неизвестно'
        info_title = (
            soup
            .find(class_='anime-info')
            .find('dl', class_='row')
            .find_all_next()
        )
        for character in info_title:
            match character.text.strip():
                case 'Эпизоды': episodes = character.find_next().text
                
                case 'Статус':
                    try:
                        status = character.find_next('dd').text.strip()
                    except:
                        pass
        abount_episodes = (
            soup
            .find('div', class_='content p-3')
            .find('div', class_='read-more-container scroll')
            .find_all('div', class_='col-12 released-episodes-item')[1:3]
        )
        builder = []
        for about_episode in abount_episodes:
            next_and_last = (
                about_episode
                .div.div.div
                .text)

            name_episodes = (
                about_episode
                .find(class_='row m-0')
                .find_all('div')[1]
                .text.strip())
            
            date_titles = (
                about_episode
                .find(class_='row m-0')
                .find_all('div')[2]
                .text.strip())

            builder.append({
                'episode': next_and_last,
                'name': name_episodes,
                'date': date_titles,
            })
        next_episode, last_episode = builder[0], builder[1]
        
        if status == 'Вышел':
            model = Title(
            name=name,
            rating=rating,
            episodes=episodes,
            status=status,
            )

            return model

        model = Title(
            name=name,
            rating=rating,
            episodes=episodes,
            status=status,
            next_episode=next_episode,
            last_episode=last_episode,
        )

        return model


async def get_session(name: str):
    async with ClientSession() as session:
        task = asyncio.create_task(get_title(session, name))
        await asyncio.gather(task)
    return task.result()
    

# def main() -> None:
#     print(get_title('Поднятие уровня в одиночку'))
    

# if __name__ == '__main__':
#     main()