from abc import ABC, abstractmethod


class ABCValidation(ABC):
    @abstractmethod
    async def _check_user():
        raise NotImplementedError("Пользователь не найден!")
    
    @abstractmethod
    async def _check_title():
        raise NotImplementedError("Тайтл не найден!")
    
    
class ABCAddInDB(ABC):
    @abstractmethod
    async def add_user():
        raise NotImplementedError("Пользователь не добавлен!")
    
    
class ABCAddTitleInDB(ABC):
    @abstractmethod
    async def add_title():
        raise NotImplementedError("Тайтл не добавлен!")


class ABCGetDB(ABC):
    @abstractmethod    
    async def delete_title():
        raise NotImplementedError("Тайтл не удален!")

    @abstractmethod 
    async def get_anime_titles():
        raise NotImplementedError("Тайтлы не получены!")
        
    @abstractmethod 
    async def get_comics_titles():
        raise NotImplementedError("Тайтлы не получены!")

    @abstractmethod
    async def get_anime_title_bd():
        raise NotImplementedError("Тайтлы не получены!")

    @abstractmethod
    async def get_comics_title_bd():
        raise NotImplementedError("Тайтлы не получены!")

    @abstractmethod
    async def get_episodes_and_url_db():
        raise NotImplementedError("Тайтлы не получены!")
