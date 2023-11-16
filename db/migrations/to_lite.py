from db.tables import *
from db import models as m


async def do_migration():

    users = await m.User.objects.filter().all()
    messages = await m.Message.objects.filter().all()
    comments = await m.Comment.objects.filter().all()
    for user in users:
        await Users().add_new(**user.dict())
    for message in messages:
        await Messages().add_new(**{
            'user_id': message.id,
            'text': message.text,
            'role': message.role
        })
    for comment in comments:
        await Comments().add_new(**{
            'user_id': comment.id,
            'time': comment.time
        })

