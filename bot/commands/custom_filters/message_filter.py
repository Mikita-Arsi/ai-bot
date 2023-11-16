from typing import Union, Dict, Any
from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message

from bot.const import admins
from bot.utils import bot_commands


class MessageFilter(Filter):
    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if message.text in [('/' + cmd[0]) for cmd in bot_commands] or message.chat.type == 'supergroup':
            return False
        if message.from_user.id in [admin.id for admin in admins]:
            return False
        return True
