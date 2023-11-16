from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.utils import send_message, gpt_text
from bot.states import FSMUser
from bot.keyboards import generate_gpt_keyboard
from bot.models import LEVEL2


async def to_gpt(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(FSMUser.gpt)
    await send_message(call, bot, gpt_text, parse_mode='HTML', keyboard=generate_gpt_keyboard(call, LEVEL2))
