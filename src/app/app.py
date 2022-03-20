import logging
import logging.config

from fastapi import FastAPI
from fastapi.routing import Request
from src.api.views import health
from src.app.db import db
from src.app.logging_config import LOGGING_CONFIG
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
        status_code=500,
        content={"detail": "Something went wrong!"},
    )


app.include_router(health.router, prefix="/-")
