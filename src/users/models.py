from django.db import models
from django.contrib.auth.models import AbstractUser


FILM_STATUS = (
    ('watching', 'Смотрю'),
    ('watched', 'Посмотрел'),
    ('plan', 'Буду смотреть'),
    ('quit', 'Бросил'),
)


def film_default():
    return {308: {"status": "watched", "rated": 10}}


class Spectator(AbstractUser):
    films = models.JSONField("FilmsInfo", default=film_default)

    def __str__(self):
        return self.username
