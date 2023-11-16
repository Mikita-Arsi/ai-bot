from typing import Union, Dict, Any
from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import CallbackQuery


class SubFilter(Filter):
    async def __call__(self, call: CallbackQuery, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if call.data.split(':')[0] == 'check_sub':
            return True
        return False
