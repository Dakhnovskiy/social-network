from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from src.api.serializers import UserIn, UserOut
from src.services.auth import get_current_user, get_user_login_from_token
from src.services.users import create_user, get_user_by_id, get_user_by_login
from starlette import status

router = APIRouter()


@router.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_client_handler(user: UserIn):
    await create_user(
        login=user.login,
        password=user.password,
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        sex=user.sex,
        interests=user.interests,
        city_id=user.city_id,
    )
    user_data = await get_user_by_login(user.login)

    return user_data


@router.get("/users/me", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_my_user_info(current_user: Dict = Depends(get_current_user)):
    return current_user


@router.get("/users/{user_id}", response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_user_info_by_id(user_id: int, login=Depends(get_user_login_from_token)):
    user_data = await get_user_by_id(user_id)
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user_data
