import logging

from asyncpg import UniqueViolationError

from db.tables import *
from db import models as m


async def do_migration():
    users = await Users().select_all()
    messages = await Messages().select_all()
    comments = await Comments().select_all()
    for user in users:
        try:
            await m.User.objects.create(**{
                'id': user[1],
                'username': user[2],
                'first_name': user[3],
                'last_name': user[4]
            })
        except UniqueViolationError as e:
            logging.info('user in db')
    for message in messages:
        await m.Message.objects.create(**{
            'id': message[1],
            'text': message[2],
            'role': message[3],
        })
    for comment in comments:
        try:
            await m.Comment.objects.create(**{
                'id': comment[1],
                'time': comment[2],
            })
        except UniqueViolationError as e:
            logging.info('comment in db')

