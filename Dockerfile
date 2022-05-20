# pull official base image
FROM python:3.9.2

WORKDIR /home/app/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get -y install postgresql gcc python3-dev musl-dev redis-server

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /home/app/web/static

COPY . .
