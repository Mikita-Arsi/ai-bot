from aiogram.fsm.state import State, StatesGroup


class FSMUser(StatesGroup):
    menu = State()
    gpt = State()
    dalle = State()
