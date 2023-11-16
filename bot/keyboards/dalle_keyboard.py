from aiogram.utils.keyboard import InlineKeyboardBuilder


def generate_dalle_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='Вернуться в меню', callback_data=f'menu')
    builder.adjust(1, 1)
    return builder.as_markup()
