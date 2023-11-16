from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.utils import send_message, menu_text, check
from bot.states import FSMUser
from bot.keyboards import generate_menu_keyboard


async def back_to_menu(call: CallbackQuery, bot: Bot, state: FSMContext):

    user_level = await check(call, bot)

    if user_level:
        await state.set_state(FSMUser.menu)
        await send_message(call, bot, menu_text, parse_mode='HTML', keyboard=generate_menu_keyboard(user_level))
