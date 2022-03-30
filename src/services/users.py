from typing import Dict, List, Optional

from constants import Sex
from src.models import create_user_data, get_user_data_by_login
from src.services.crypto import get_password_hash


async def create_user(
    login: str,
    password: str,
    first_name: str,
    last_name: str,
    age: int,
    sex: Sex,
    interests: Optional[List[str]],
    city_id: int,
) -> int:
    password_hash = get_password_hash(password)
    return await create_user_data(
        login=login,
        password_hash=password_hash,
        first_name=first_name,
        last_name=last_name,
        age=age,
        sex=sex,
        interests=interests,
        city_id=city_id,
    )


async def get_user_by_login(login: str) -> Optional[Dict]:
    return await get_user_data_by_login(login)
