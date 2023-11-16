from typing import Union, Dict, Any
from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message
from bot.const import admins


class AdminFilter(Filter):
    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if message.from_user.id in [admin.id for admin in admins] and message.text in (
            '.info',
            'взлом жопы',
            '.get_info'
        ):
            return True
        return False
