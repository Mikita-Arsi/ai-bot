import time

from aiogram.types import Message
from db import models as m


async def register_comment(message: Message):
    print("registration", message.from_user.id)
    if await m.Comment.objects.get_or_none(id=message.from_user.id) is not None:
        await m.Comment.objects.delete(id=message.from_user.id)
    await m.Comment.objects.create(**{'id': message.from_user.id, 'time': int(time.time())})
