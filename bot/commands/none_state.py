import logging

import openai
from aiogram import Router, Bot
from aiogram.types import Message
from openai import InvalidRequestError

from bot.models import LEVEL2
from db import models as m
from bot.utils import do_answer, check, max_memory_error_text, send_message, menu_text
from bot.states import FSMUser
from aiogram.fsm.context import FSMContext
from bot.keyboards import generate_gpt_keyboard, generate_menu_keyboard

none_router = Router()


@none_router.message()
async def gpt_answer(message: Message, bot: Bot, state: FSMContext) -> None:
    if message.from_user and not message.from_user.is_bot and message.chat.id == message.from_user.id:
        user_level = await check(message, bot)
        if user_level == LEVEL2:
            await state.set_state(FSMUser.menu)
            await send_message(message, bot, menu_text, parse_mode='HTML', keyboard=generate_menu_keyboard(user_level))
        elif user_level:
            await state.set_state(FSMUser.gpt)
            msg = await do_answer(message, '<i>Пишу ответ, ожидайте...</i>', parse_mode='HTML')
            if not msg:
                return

            await m.Message.objects.create(**{'id': message.from_user.id, 'text': message.text, 'role': False})
            rows = await m.Message.objects.filter(id=message.from_user.id).all()
            messages = [
                {'role': 'assistant' if row.role else 'user', 'content': row.text} for row in rows
            ]

            try:
                response = await openai.ChatCompletion.acreate(
                    model="gpt-3.5-turbo",
                    messages=messages
                )

                if len(response['choices'][0]['message']['content']) > 4096:
                    response['choices'][0]['message']['content'] = response['choices'][0]['message']['content'][0:4095]

                await bot.edit_message_text(
                    text=response['choices'][0]['message']['content'],
                    parse_mode='Markdown',
                    chat_id=message.chat.id,
                    message_id=msg.message_id,
                    reply_markup=generate_gpt_keyboard(message, user_level)
                )

                if len(rows) > 20:
                    await m.Message.objects.delete(message_id=rows[0].message_id)
                    await m.Message.objects.delete(message_id=rows[1].message_id)

                await m.Message.objects.create(**{
                    'id': message.from_user.id,
                    'text': response['choices'][0]['message']['content'],
                    'role': True
                })

            except InvalidRequestError as e:
                await bot.edit_message_text(
                    text=max_memory_error_text,
                    chat_id=message.from_user.id,
                    reply_markup=generate_gpt_keyboard(message, user_level),
                    message_id=msg.message_id)
                logging.info(e)
