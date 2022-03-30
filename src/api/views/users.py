from fastapi import APIRouter
from src.api.serializers import UserIn, UserOut
from src.services.users import create_user, get_user_by_login

router = APIRouter()


@router.post("/users", response_model=UserOut, status_code=201)
async def create_client_handler(user: UserIn):
    user_id = await create_user(
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

    return {
        "id": user_id,
        "login": user.login,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "age": user.age,
        "sex": user.sex,
        "interests": user.interests,
        "city_id": user.city_id,
        "created_dt": user_data["created_dt"],
    }
