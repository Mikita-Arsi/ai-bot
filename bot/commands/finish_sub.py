from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from bot.models import LEVEL2
from bot.states import FSMUser
from bot.utils import check, send_message, gpt_text, do_answer, start_text
from bot.keyboards import generate_menu_keyboard, generate_gpt_keyboard


async def sub_finish(call: types.CallbackQuery, bot: Bot, state: FSMContext) -> None:
    user_level = await check(call, bot)
    if not call.from_user.is_bot:
        if user_level == LEVEL2:
            await state.set_state(FSMUser.menu)
            await send_message(call, bot, start_text, keyboard=generate_menu_keyboard(user_level))
        elif user_level:
            await state.set_state(FSMUser.gpt)
            await send_message(call, bot, gpt_text, keyboard=generate_gpt_keyboard(call, user_level))
