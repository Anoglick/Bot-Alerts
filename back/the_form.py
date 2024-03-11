from .models import Title

async def right_form(data: Title) -> str:
    name = data.name
    rating = data.rating
    episodes = data.episodes
    status = data.status

    if data.next_episode is None and data.last_episode is None:
        return (
        f"""
        <b>☀{name}☀</b>
        <b>Рейтинг</b>🌈: {rating}

        <b>Количество серий</b>🍒: {episodes}
        <b>Статус</b>🌆: {status}
        """
        )
    else:    
        dict_next_episode = data.next_episode
        next_episode = dict_next_episode.episode
        next_name = dict_next_episode.name
        next_date = dict_next_episode.date

        dict_last_episode = data.last_episode
        last_episode = dict_last_episode.episode
        last_name = dict_last_episode.name
        last_date = dict_last_episode.date

        return (
        f"""
        <b>☀{name}☀</b>
        <b>Рейтинг</b>🌈: {rating}

        <b>Количество серий</b>🍒: {episodes}
        <b>Статус</b>🌆: {status}
        
        <b>Следующая серия</b>🥰: 
            Серия: {next_episode} 
            Название серии: {next_name} 
            Дата выхода: {next_date}

        <b>Прошлая серия</b>😫: 
            Серия: {last_episode}
            Название серии: {last_name} 
            Дата выхода: {last_date}
        """
        )