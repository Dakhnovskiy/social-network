from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.api.serializers import AuthOut
from src.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from src.services.auth import authenticate_user, create_access_token
from starlette import status

router = APIRouter()


@router.post("/token", response_model=AuthOut)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["login"]}, expires_delta=access_token_expires
    )
    return {"token": access_token}
