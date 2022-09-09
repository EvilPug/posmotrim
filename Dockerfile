# syntax=docker/dockerfile:1

FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apk update
RUN apk upgrade
RUN apk add g++ jpeg-dev zlib-dev libjpeg make
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

RUN mkdir ./src/static
RUN mkdir ./src/templates
