FROM python:3.10

ENV PROJECT_ROOT="/usr/src/app"
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PROJECT_ROOT

RUN pip install poetry

WORKDIR $PROJECT_ROOT

ADD poetry.lock pyproject.toml $PROJECT_ROOT
RUN poetry config virtualenvs.create false
RUN poetry install

ADD . $PROJECT_ROOT

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
