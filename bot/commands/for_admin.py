from aiogram import Bot
from aiogram.types import Message
from db import models as m
from bot.const import admins
from bot.utils import send_message


async def get_info(message: Message, bot: Bot):
    await send_message(message, bot, f"""
users: {len(await m.User.objects.filter().all())}
messages: {len(await m.Message.objects.filter().all())}
comments: {len(await m.Comment.objects.filter().all())}
    """)


async def call_admin_consol(message: Message, bot: Bot):
    if message.from_user.id == admins[1].id and message.text == '.get_info':
        await get_info(message, bot)
    elif message.from_user.id == admins[0].id and message.text in ['.info', 'взлом жопы']:
        await get_info(message, bot)

