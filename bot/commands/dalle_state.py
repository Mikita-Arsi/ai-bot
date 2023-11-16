import logging
import langid
import openai

from aiogram import Bot, Router
from aiogram.exceptions import TelegramForbiddenError
from aiogram.types import Message
from openai import InvalidRequestError
from openai.error import ServiceUnavailableError

from bot.utils import check, do_answer
from bot.states import FSMUser
from bot.keyboards import generate_dalle_keyboard
from .none_state import none_router


dalle_router = Router()
dalle_router.include_router(none_router)


@dalle_router.message(FSMUser.dalle)
async def dalle_answer(message: Message, bot: Bot):
    is_check = await check(message, bot)

    if is_check and not message.from_user.is_bot and message.text is not None and message.chat.id == message.from_user.id:
        msg = await do_answer(message, '<i>Генерирую изображение, ожидайте...</i>', parse_mode='HTML')
        if not msg:
            return
        if langid.classify(message.text)[0] != 'en':
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": "Переведи на английский:\n\n" + message.text
                    }
                ]
            )

            prompt = ''.join(response['choices'][0]['message']['content'])
        else:
            prompt = message.text

        try:
            response = await openai.Image.acreate(
                prompt=prompt,
                n=1,
                size="512x512",
            )
            await bot.edit_message_text(
                text=f"""
                    <a href="{response["data"][0]["url"]}">{message.text}</a>                
                """,
                chat_id=message.from_user.id,
                reply_markup=generate_dalle_keyboard(),
                message_id=msg.message_id,
                parse_mode='HTML'
                )

        except InvalidRequestError as e:
            logging.info(e)
            await bot.edit_message_text(
                text="""<i>Пожалуйста, укажите другой запрос</i>""",
                chat_id=message.from_user.id,
                reply_markup=generate_dalle_keyboard(),
                message_id=msg.message_id,
                parse_mode='HTML'
            )
        except ServiceUnavailableError as e:
            logging.info(e)
            response = await openai.Image.acreate(
                prompt=prompt[0],
                n=1,
                size="512x512",
            )
            await bot.edit_message_text(
                text=f"""
                                <a href="{response["data"][0]["url"]}">{message.text}</a>                
                            """,
                chat_id=message.from_user.id,
                reply_markup=generate_dalle_keyboard(),
                message_id=msg.message_id,
                parse_mode='HTML'
            )

