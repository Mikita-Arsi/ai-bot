from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.models import UserLevel, LEVEL2


def generate_menu_keyboard(user_level: UserLevel):
    builder = InlineKeyboardBuilder()
    builder.button(text='ChatGPT', callback_data='gpt')
    if user_level == LEVEL2:
        builder.button(text='DALL-E 2', callback_data='dalle')
    else:
        builder.button(text='D̶A̶L̶L̶-̶E̶ ̶2̶', callback_data='dalle_blocked')
    return builder.as_markup()
