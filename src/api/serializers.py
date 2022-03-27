import datetime
from typing import List, Optional

from constants import RelationStatus, Sex
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


class UserOut(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str
    age: conint(ge=0)
    sex: Sex
    interests: Optional[List[str]]
    city_id: int
    created_dt: datetime.datetime


class RelatedUser:
    first_name: str
    last_name: str
    relation_status: RelationStatus


class RelatedUsers:
    users: List[RelatedUser]
