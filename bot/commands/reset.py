from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.states import FSMUser
from db import models as m
from bot.utils import send_message, reset_text


async def reset_dialog(call: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(FSMUser.gpt)
    await m.Message.objects.delete(id=call.from_user.id)
    await send_message(call, bot, reset_text, parse_mode='HTML')
