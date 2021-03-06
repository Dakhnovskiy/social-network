import datetime
from typing import List, Optional

from constants import RelationStatus, Sex
from pydantic import BaseModel, conint


class City(BaseModel):
    id: int
    name: str


class CitiesOut(BaseModel):
    data: List[City]


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
    city_id: int
    created_dt: datetime.datetime


class UsersOut(BaseModel):
    data: List[UserOut]


class RelatedUser:
    first_name: str
    last_name: str
    relation_status: RelationStatus


class RelatedUsers:
    users: List[RelatedUser]


class AuthIn(BaseModel):
    login: str
    password: str


class AuthOut(BaseModel):
    token: str
