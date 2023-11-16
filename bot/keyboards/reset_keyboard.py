from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.models import LEVEL2, UserLevel


def generate_gpt_keyboard(message: types.Message | types.CallbackQuery, user_level: UserLevel):
    builder = InlineKeyboardBuilder()
    builder.button(text='Сброс текущего диалога', callback_data=f'reset:id{message.from_user.id}')
    if user_level == LEVEL2:
        builder.button(text='Вернуться в меню', callback_data=f'menu')
    builder.adjust(1, 1)
    return builder.as_markup()
