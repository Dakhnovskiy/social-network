from typing import List, Optional

from constants import Sex
from pydantic import BaseModel, conint


class UserIn(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    age: conint(ge=0)
    sex: Sex
    interests: Optional[List[str]]
    city_id: int
