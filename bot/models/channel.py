from pydantic import BaseModel, NegativeInt


class Channel(BaseModel):
    id: NegativeInt
    prefix: str
    name: str
