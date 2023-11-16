import logging

import openai
from aiogram import Bot
from aiogram.types import Message
from openai import InvalidRequestError
from bot.utils import do_answer


async def generate(message: Message, bot: Bot):
    msg = await do_answer(message, '<i>Генерирую изображение, ожидайте...</i>', parse_mode='HTML')
    if not msg:
        return
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "Переведи на английский:\n\n" + message.text.split('\n')[1]
                }
            ]
        )

        prompt = ''.join(response['choices'][0]['message']['content']),

        response = openai.Image.create(
            prompt=prompt[0],
            n=1,
            size="256x256",
        )
        await bot.edit_message_text(response["data"][0]["url"])

    except InvalidRequestError as e:
        logging.info(e)
