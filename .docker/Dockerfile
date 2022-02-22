FROM python:3.10

WORKDIR /home/app

COPY . .

RUN apt-get update -yy \
    && apt-get upgrade -yy \
    && pip install --no-cache-dir pipenv \
    && apt install libyaml-dev

RUN pipenv sync --dev --pre

