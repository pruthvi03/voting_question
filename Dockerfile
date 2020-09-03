FROM python:buster

ENV PYTHONUNBUFFERED 1

COPY . /votersparadise/
COPY requirements.txt /votersparadise/

WORKDIR /votersparadise/
RUN python3 -m pip install -r requirements.txt

