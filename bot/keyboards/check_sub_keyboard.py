from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.const import channels


def generate_for_sub_keyboard(message: types.Message | types.CallbackQuery, is_sub: bool):
    builder = InlineKeyboardBuilder()
    for channel in channels:
        builder.button(text=channel.name, url=f'https://t.me/{channel.prefix}')
    text = 'Проверить подписку'
    if len(channels) > 1:
        text = 'Проверить подписки'
    builder.button(text=text, callback_data=f'check_sub:id{message.from_user.id}:{is_sub}')
    builder.adjust(1, 1)
    return builder.as_markup()
