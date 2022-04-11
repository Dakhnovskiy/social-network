from typing import Dict

from fastapi import APIRouter, Depends
from starlette import status

from constants import RelationStatus
from src.services.auth import get_current_user

router = APIRouter()


@router.post("/relations", response_model=RelationOut, status_code=status.HTTP_201_CREATED)
async def create_client_handler(relation=RelationIn, current_user: Dict = Depends(get_current_user)):
    relation_id = await create_user_relation(
        first_user_id=current_user["id"],
        second_user_id=relation.target_user_id,
        status=RelationStatus.REQUEST,
    )

    return {

    }
