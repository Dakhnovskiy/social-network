#!/bin/bash

#alembic upgrade head

if [[ ${ENVIRONMENT} = 'LOCAL' ]]; then
    exec uvicorn src.app.app:app --reload --host 0.0.0.0 --port 8080 --log-level info
else
    exec uvicorn src.app.app:app --host 0.0.0.0 --port 8080 --log-level warning
fi