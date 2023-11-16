from typing import Union, Dict, Any
from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import CallbackQuery


class ResetFilter(Filter):
    async def __call__(self, call: CallbackQuery, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if call.data.split(':')[0] == 'reset' and call.message.chat.id == call.from_user.id:
            return True
        return False
