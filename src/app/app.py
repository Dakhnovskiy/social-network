import logging
import logging.config

from fastapi import FastAPI
from fastapi.routing import Request
from src.api.views import auth, health, users
from src.app.db import db
from src.app.logging_config import LOGGING_CONFIG
from starlette import status
from starlette.responses import JSONResponse

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.exception_handler(500)
async def on_500(request: Request, exc: Exception):
    logging.exception(exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Something went wrong!"},
    )


app.include_router(health.router, prefix="/-")
app.include_router(users.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
