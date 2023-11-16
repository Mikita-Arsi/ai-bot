from aiogram.types import Message, CallbackQuery
from db import models as m


async def check_comment(message: Message | CallbackQuery):
    row = await m.Comment.objects.get_or_none(id=message.from_user.id)
    print(message.from_user.id, row)
    if row is not None:
        return True
    return True  # False
