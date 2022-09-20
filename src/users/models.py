from django.db import models
from django.contrib.auth.models import AbstractUser


def film_default():
    return {308: {"status": "просмотрен", "rated": 10}}


class Spectator(AbstractUser):
    films = models.JSONField("FilmsInfo", default=film_default)

    def __str__(self):
        return self.username
