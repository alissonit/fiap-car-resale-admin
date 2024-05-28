FROM python:3.10

LABEL VENDOR="FIAP"
LABEL NAME="Fiap"
LABEL VERSION="1.0"
LABEL MAINTAINER="alissoncastroskt@gmail.com"

ENV APP_HOME "/opt/app"
ENV PATH="${PATH}:/root/.local/bin"

# ENV FOR PYTEST
ENV DB_USER=postgres
ENV DB_PASSWORD=""
ENV DB_HOST=""
ENV DB_PORT=5432
ENV DB_NAME=fiapdbadmin
ENV DB_URI=""
ENV DB_MAX_POOL_SIZE=10


WORKDIR ${APP_HOME}

COPY . ./

RUN export $(grep -v '^#' .env | xargs)

RUN python -m pip install -r requirements.txt --user

RUN python -m pytest --cov=.

ENV PORT 8000
EXPOSE $PORT

WORKDIR $APP_HOME

USER root

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 --log-level info
