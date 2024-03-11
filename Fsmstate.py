from aiogram.fsm.state import StatesGroup, State

class Waiting(StatesGroup):
    user_answer = State()