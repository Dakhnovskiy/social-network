from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


@router.get("/ping", status_code=200)
def get_ping():
    """
    Health check
    """
    return Response(content='{"ping": "pong"}', media_type="application/json")
