from sqlalchemy import select

from .abstractions import ABCValidation


class Validation(ABCValidation):
    model = None

    
    async def _check_user(self, session, user_id: int) -> bool | None:
        query = (
            select(self.model)
            .filter_by(user_id=user_id)
            .filter(self.model.count_titles < self.model.limit_count)
        )
        return True if await session.scalar(query) is not None else False


    async def _check_title(self, session, user_id: int, title: str) -> bool | None:
        query = (
            select(self.model)
            .filter_by(user_id=user_id, title=title)
        )
        return True if await session.scalar(query) is None else False


class ModelValidation(Validation):
    def __init__(self, model) -> None:
        self.model = model
    

    async def check_user(self, session, user_id: int) -> bool:
        return await self._check_user(session, user_id)
    
    
    async def check_title(self, session, user_id: int, title: str) -> bool:
        return await self._check_title(session, user_id, title)

    # async def check_limit_count(self, session, user_id: int) -> bool:
    #     query = (
    #         select(self.model)
    #         .filter_by(user_id=user_id)
    #     )
    #     return True if await session.scalar(query) is not None else False
    
    # async def check_limit_count_titles(self, session, user_id: int) -> bool:
    #     query = (
    #         select(self.model)
    #         .filter_by(user_id=user_id)
    #     )
    #     return True if await session.scalar(query) is not None else False
