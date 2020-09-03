FROM python:buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /votersparadise

COPY . /votersparadise/
COPY requirements.txt /votersparadise/

WORKDIR /votersparadise
RUN python3 -m pip install -r requirements.txt

CMD [ "python","manage.py","runserver" ]