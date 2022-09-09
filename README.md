# Сервис трекинга фильмов "Посмотрим"

#### Как развернуть проект?

Создать .env файл в корне проекта со следующим содержимым:

    DEBUG=True
    SECRET_KEY='your_secret_key'

    POSTGRES_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres

Поднять проект с помощью Docker

    docker-compose build
    docker-compose up -d

В контейнере web выполнить команды:

    cd src
    python3 manage.py migrate

*Запущенный сервер доступен по адресу 127.0.0.1:8000*


## Скриншоты

<p align="center">
  <img src="" />
</p>

<p align="center">
  <img src="" />
</p>

<p align="center">
  <img src="" />
</p>

<p align="center">
  <img src="" />
</p>
