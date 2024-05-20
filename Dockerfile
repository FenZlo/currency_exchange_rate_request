ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

COPY pdm.lock pyproject.toml /app/
RUN pip install pdm
RUN pdm install -d --no-self #эта команда говорит, что не нужно устанавливать модуль src, так как мы его копируем из нашей файловой системы
COPY src /app/src
CMD pdm run uvicorn src.server:app --host=0.0.0.0
