ARG PYTHON_VERSION=3.8.10
FROM python:${PYTHON_VERSION}-slim

RUN apt-get update && pip install poetry && poetry config virtualenvs.create false

WORKDIR /jwt

COPY ./pyproject.toml /jwt/
COPY ./poetry.lock /jwt/
COPY ./jwt_service /jwt/jwt_service

RUN poetry install

ENTRYPOINT uvicorn jwt_service.main:app --host 0.0.0.0 --port 8082 --reload
