from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

router = APIRouter()


@router.get("/ping", status_code=status.HTTP_200_OK)
def get_ping():
    """
    Health check
    """
    return Response(content='{"ping": "pong"}', media_type="application/json")
