# pull official base image
FROM python:3.9.2

# set work directory
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update -y && apt-get -y install postgresql gcc python3-dev musl-dev redis-server

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /home/app/webstatic


# copy project
COPY . .
