FROM python:3.9-slim-bullseye AS build-stage

# install dependencies

RUN pip install poetry==1.5.0 --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry config installer.max-workers 10

WORKDIR /app

# copy dependencies
COPY pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry lock --no-update \
  && poetry install --no-cache --no-interaction --no-ansi --without dev

# copy local files
COPY app .


# entrypoint
CMD [ "uvicorn", "main:app", "--port", "80", "--host", "0.0.0.0", "--no-access-log"]
