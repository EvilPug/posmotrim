# syntax=docker/dockerfile:1

FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN sed -i 's/https/http/g' /etc/apk/repositories
RUN apk add g++ jpeg-dev zlib-dev libjpeg make

RUN python -m pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . /code/
WORKDIR /code/src
