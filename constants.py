from enum import Enum


class Sex(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class RelationStatus(Enum):
    REQUEST = "REQUEST"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
