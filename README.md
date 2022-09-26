# Сервис трекинга фильмов "Посмотрим"

## Описание

Социальная сеть - трекер фильмов. Позволяет пользователю присвоить фильму из каталога одно из состояний: **`смотрю`**, **`забросил`**, **`посмотрел`**, **`хочу посмотреть`**. 
Пользователю доступны списки фильмов, находящихся в том или ином состоянии, а также возможность поменять это состояние, ознакомиться с текстовым описанием фильма, поставить ему собственную оценку от 0 до 10. 

Пользователь может добавлять в друзья других пользователей, сопоставлять свои фильмы с фильмами друга, сравнивать выставленные фильмам оценки.  
Помимо этого, в приложении также предусмотрена функция рекомендательной системы content-based типа. 
На главной странице пользователя ждет поисковая строка и возможность ознакомиться с фильмами/сериалами, схожими с теми, что он уже посмотрел или смотрит. Также, на странице каждого из фильмов/сериалов можно увидеть перечень из 5 похожих.

## Скриншоты

#### Главная

<p align="center">
  <img src="https://github.com/EvilPug/posmotrim/blob/e063f65dfccdb82248386df7a8138712b25b9d82/screenshots/main.png?raw=true" />
</p>

#### Описание фильма

<p align="center">
  <img src="https://github.com/EvilPug/posmotrim/blob/e063f65dfccdb82248386df7a8138712b25b9d82/screenshots/film_detail.png?raw=true" />
</p>

#### Профиль пользователя

<p align="center">
  <img src="https://github.com/EvilPug/posmotrim/blob/e063f65dfccdb82248386df7a8138712b25b9d82/screenshots/profile.png?raw=true" />
</p>

## Как развернуть проект?

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

### Если что-то пошло не так

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

    python tracker/populate_db.py

8)После этого можно создать суперпользователя

    python manage.py createsuperuser
