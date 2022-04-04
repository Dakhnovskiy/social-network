from fastapi import APIRouter, Depends
from src.api.serializers import CitiesOut
from src.services.auth import get_user_login_from_token
from src.services.cities import get_cities
from starlette import status

router = APIRouter()


@router.get(
    "/cities",
    dependencies=[Depends(get_user_login_from_token)],
    response_model=CitiesOut,
    status_code=status.HTTP_200_OK,
)
async def get_user_info_by_id():
    cities = await get_cities()
    return {"data": cities}
