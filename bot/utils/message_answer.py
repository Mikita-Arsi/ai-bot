from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery


async def do_answer(
        message: Message,
        text: str,
        keyboard: InlineKeyboardMarkup = None,
        parse_mode: str = 'Markdown'
):
    try:
        return await message.answer(text, reply_markup=keyboard, parse_mode=parse_mode)
    except TelegramForbiddenError:
        return False


async def send_message(
        message: Message | CallbackQuery,
        bot: Bot,
        text: str,
        keyboard: InlineKeyboardMarkup = None,
        parse_mode: str | None = 'Markdown'
):
    try:
        return await bot.send_message(
            message.from_user.id,
            text,
            reply_markup=keyboard,
            parse_mode=parse_mode
        )
    except TelegramForbiddenError:
        return False
