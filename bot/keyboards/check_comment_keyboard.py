from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.const import channels


def generate_for_comment_keyboard(message: types.Message | types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for channel in channels:
        builder.button(text=channel.name, url=f'https://t.me/{channel.prefix}')
    text = 'Проверить комментарий'
    builder.button(text=text, callback_data=f'check_comment:{message.from_user.id}')
    builder.adjust(1, 1)
    return builder.as_markup()
