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

    python manage.py makemigrations users
    python manage.py makemigrations tracker
    python manage.py migrate

Затем необходимо заполнить таблицу фильмов

    python tracker/populate_db.py

После этого можно создать суперпользователя

    python manage.py createsuperuser

*Запущенный сервер доступен по адресу 127.0.0.1:8000*

#### Если что-то пошло не так

1)Останавливаем контейнер web (контейнер db должен остаться включенным)

2)Подключаемся к контейнеру db через pgAdmin по следующим реквизитам
    
    Адрес сервера: localhost
    Порт: 5435
    Имя базы данных: postgres
    Имя пользователя: postgres
    Пароль: postgres
 
3)Открываем запросник к указанной базе данных и выполняем следующее

    DROP SCHEMA public CASCADE;
    CREATE SCHEMA public;

    GRANT ALL ON SCHEMA public TO postgres;
    GRANT ALL ON SCHEMA public TO public;

4)Удаляем папки *migrations* в папках *users* и *tracker*

5)Запускаем контейнер web

6)В контейнере web выполняем команды:

    python manage.py makemigrations users
    python manage.py makemigrations tracker
    python manage.py migrate

7)Затем необходимо заполнить таблицу фильмов

    cd ./tracker
    python populate_db.py

8)После этого можно создать суперпользователя

    python manage.py createsuperuser

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
