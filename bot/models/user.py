from pydantic import BaseModel, PositiveInt
from typing import Optional


class User(BaseModel):
    id: PositiveInt
    prefix: str
    first_name: str
    last_name: Optional[str]
