import sqlalchemy as sa
from constants import RelationStatus, Sex
from src.app.db import metadata

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
    sa.Column("login", sa.String(256), nullable=False),
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
