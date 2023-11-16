from typing import Union, Dict, Any
from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message, CallbackQuery
from bot.const import channels


class NewCommentFilter(Filter):
    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if message.chat.id == -1001917301570 and message.reply_to_message is not None:
            if message.reply_to_message.sender_chat is not None:
                if message.reply_to_message.sender_chat.id == -1001985843105:
                    return True
        return False


class CheckCommentFilter(Filter):
    async def __call__(self, call: CallbackQuery, bot: Bot) -> Union[bool, Dict[str, Any]]:
        if call.data.split(':')[0] == 'check_comment':
            return True
        return False
