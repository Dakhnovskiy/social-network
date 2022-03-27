from enum import Enum


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class RelationStatus(Enum):
    REQUEST = "REQUEST"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
