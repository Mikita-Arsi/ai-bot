from aiogram import types, Bot
from asyncpg import UniqueViolationError
from db import models as m
from aiogram.fsm.context import FSMContext
from bot.states import FSMUser
from bot.utils import check, do_answer, start_text, gpt_text
from bot.keyboards import generate_menu_keyboard, generate_gpt_keyboard
from bot.models import LEVEL2


async def hello(message: types.Message, bot: Bot, state: FSMContext) -> None:
    try:
        await m.User.objects.create(**{
            'id': message.from_user.id,
            'username': message.from_user.username,
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name
        })
    except UniqueViolationError:
        pass

    user_level = await check(message, bot)

    if not message.from_user.is_bot and message.text is not None and message.chat.id == message.from_user.id:
        if user_level == LEVEL2:
            await state.set_state(FSMUser.menu)
            await do_answer(message, start_text, keyboard=generate_menu_keyboard(user_level))
        elif user_level:
            await state.set_state(FSMUser.gpt)
            await do_answer(message, gpt_text, keyboard=generate_gpt_keyboard(message, user_level))
    else:
        return

