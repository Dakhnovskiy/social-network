from typing import Dict, List, Optional

import sqlalchemy as sa
from constants import RelationStatus, Sex
from src.app.db import db, metadata

cities = sa.Table(
    "cities",
    metadata,
    sa.Column(
        "id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False
    ),
    sa.Column("name", sa.String(256), nullable=False),
)

users = sa.Table(
    "users",
    metadata,
    sa.Column(
        "id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False
    ),
    sa.Column("login", sa.String(256), nullable=False, unique=True),
    sa.Column("password_hash", sa.String(256), nullable=False),
    sa.Column("first_name", sa.String(256), nullable=False),
    sa.Column("last_name", sa.String(256), nullable=False),
    sa.Column("age", sa.Integer, nullable=False),
    sa.Column("sex", sa.Enum(Sex), nullable=False),
    sa.Column("city_id", sa.BigInteger, sa.ForeignKey("cities.id"), nullable=False),
    sa.Column("created_dt", sa.DateTime, nullable=False, server_default=sa.func.now()),
)


users_interests = sa.Table(
    "users_interests",
    metadata,
    sa.Column(
        "id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False
    ),
    sa.Column("user_id", sa.BigInteger, sa.ForeignKey("users.id"), nullable=False),
    sa.Column("interest", sa.String(256), nullable=False),
)


users_relations = sa.Table(
    "users_relations",
    metadata,
    sa.Column(
        "id", sa.BigInteger, primary_key=True, autoincrement=True, nullable=False
    ),
    sa.Column(
        "first_user_id", sa.BigInteger, sa.ForeignKey("users.id"), nullable=False
    ),
    sa.Column(
        "second_user_id", sa.BigInteger, sa.ForeignKey("users.id"), nullable=False
    ),
    sa.Column("status", sa.Enum(RelationStatus), nullable=False),
    sa.Column("created_dt", sa.DateTime, nullable=False, server_default=sa.func.now()),
)


@db.transaction()
async def create_user_data(
    login: str,
    password_hash: str,
    first_name: str,
    last_name: str,
    age: int,
    sex: Sex,
    interests: Optional[List[str]],
    city_id: int,
) -> int:
    query = (
        "INSERT INTO users (login, password_hash, first_name, last_name, age, sex, city_id) "
        "VALUES (:login, :password_hash, :first_name, :last_name, :age, :sex, :city_id)"
    )

    await db.execute(
        query=query,
        values={
            "login": login,
            "password_hash": password_hash,
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "sex": sex,
            "city_id": city_id,
        },
    )
    row = await db.fetch_one("SELECT LAST_INSERT_ID()")
    user_id = row[0]

    if interests:
        query = "INSERT INTO users_interests (user_id, interest) VALUES (:user_id, :interest)"
        await db.execute_many(
            query=query,
            values=[
                {"user_id": user_id, "interest": interest} for interest in interests
            ],
        )
    return user_id


@db.transaction()
async def get_user_data_by_login(login: str) -> Optional[Dict]:
    query = (
        "SELECT id, login, password_hash, first_name, last_name, age, sex, city_id, created_dt "
        "FROM users WHERE login = :login"
    )
    data = await db.fetch_one(
        query=query,
        values={"login": login},
    )
    return dict(data) if data else None


@db.transaction()
async def get_user_data_by_id(user_id: int) -> Optional[Dict]:
    query = (
        "SELECT id, login, password_hash, first_name, last_name, age, sex, city_id, created_dt "
        "FROM users WHERE id = :user_id"
    )
    data = await db.fetch_one(
        query=query,
        values={"user_id": user_id},
    )
    return dict(data) if data else None


@db.transaction()
async def get_cities_data():
    query = "SELECT id, name FROM cities"
    data = await db.fetch_all(query=query)
    return [dict(row) for row in data]


@db.transaction()
async def get_users_data(
    first_name: Optional[str], last_name: Optional[str]
) -> List[Dict]:
    query = (
        "SELECT id, login, first_name, last_name, age, sex, city_id, created_dt "
        "FROM users "
        "WHERE 1=1"
        "  AND first_name LIKE :first_name" if first_name else "" 
        "  AND last_name LIKE :last_name" if last_name else ""
    )
    values = {}
    if first_name:
        values["first_name"] = f"{first_name}%"
    if last_name:
        values["last_name"] = f"{last_name}%"

    data = await db.fetch_all(query=query, values=values)
    return [dict(row) for row in data]
