import logging

import openai

from aiogram import types, Bot, Router
from openai import InvalidRequestError

from bot.utils import check, do_answer, max_memory_error_text
from bot.keyboards import generate_gpt_keyboard
from db import models as m
from bot.states import FSMUser
from .dalle_state import dalle_router

gpt_router = Router()
gpt_router.include_router(dalle_router)


@gpt_router.message(FSMUser.gpt)
async def gpt_answer(message: types.Message, bot: Bot) -> None:
    user_level = await check(message, bot)

    if user_level and not message.from_user.is_bot and message.text is not None and message.chat.id == message.from_user.id:
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
