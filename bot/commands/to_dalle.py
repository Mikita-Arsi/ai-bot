from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.utils import send_message, dalle_text
from bot.states import FSMUser
from bot.keyboards import generate_dalle_keyboard


async def to_dalle(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(FSMUser.dalle)
    await send_message(call, bot, dalle_text, parse_mode='HTML', keyboard=generate_dalle_keyboard())
