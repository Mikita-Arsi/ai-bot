from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import Message, CallbackQuery

from bot.keyboards import (
    generate_for_sub_keyboard,
    generate_for_comment_keyboard,
    generate_check_keyboard
)
from bot.utils import check_sub, check_comment
from bot.utils.bot_texts import (
    check_text,
    check_sub_text,
    check_comment_text
)
from bot.utils.message_answer import send_message
from bot.utils.check_level import check_user_level
from bot.models import UserLevel, LEVEL0


async def check(message: Message | CallbackQuery, bot: Bot) -> bool | UserLevel:
    try:
        is_sub = await check_sub(message, bot)
        is_comment = await check_comment(message)
        user_level = await check_user_level(message, bot)
        if user_level == LEVEL0:
            if is_sub and is_comment:
                return user_level
            if not is_sub and is_comment:
                await send_message(
                    message,
                    bot,
                    text=check_sub_text,
                    keyboard=generate_for_sub_keyboard(message, is_sub=False),
                    parse_mode=None
                )
            elif is_sub and not is_comment:
                await send_message(
                    message,
                    bot,
                    text=check_comment_text,
                    keyboard=generate_for_comment_keyboard(message),
                    parse_mode=None
                )
            elif not is_sub and not is_comment:
                await send_message(
                    message,
                    bot,
                    text=check_text,
                    keyboard=generate_check_keyboard(message),
                    parse_mode=None
                )
            return False
        else:
            return user_level
    except TelegramForbiddenError:
        return False
