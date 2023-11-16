from aiogram import Bot
from aiogram.types import CallbackQuery
from bot.utils import send_message, dalle_blocked_text, check
from bot.keyboards import generate_dalle_keyboard


async def block_dalle(call: CallbackQuery, bot: Bot):

    user_level = await check(call, bot)

    if user_level:
        await send_message(
            call, bot, dalle_blocked_text, parse_mode='HTML', keyboard=generate_dalle_keyboard()
        )
