# The builder image, used to build the virtual environment
FROM python:3.10-buster as builder

RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=0 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

ADD . .

RUN poetry install --without dev && \
    rm -rf $POETRY_CACHE_DIR && \
    eodm version
