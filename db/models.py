import ormar

from init_db import MainMeta


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    user_id: int = ormar.Integer(primary_key=True, autoincrement=True)
    id: int = ormar.BigInteger(unique=True, nullable=False)
    username: str = ormar.String(max_length=200, nullable=True)
    first_name: str = ormar.String(max_length=200)
    last_name: str = ormar.String(max_length=200, nullable=True)


class Message(ormar.Model):
    class Meta(MainMeta):
        pass

    message_id: int = ormar.Integer(primary_key=True, autoincrement=True)
    id: int = ormar.BigInteger(nullable=False)
    text: str = ormar.String(max_length=4096)
    role: bool = ormar.Boolean()


class Comment(ormar.Model):
    class Meta(MainMeta):
        pass

    comment_id: int = ormar.Integer(primary_key=True, autoincrement=True)
    id: int = ormar.BigInteger(unique=True, nullable=False)
    time: int = ormar.Integer()


class Image(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.BigInteger(primary_key=True, nullable=False)
    count: int = ormar.Integer()

