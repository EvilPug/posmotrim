from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


def film_default():
    return {"films": [{"kinopoiskId": 308, "status": "watched", "rated": 10}]}


class FilmUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    films = models.JSONField("FilmsInfo", default=film_default)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(FilmUser, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(FilmUser, related_name='to_user', on_delete=models.CASCADE)


class Film(models.Model):
    kinopoisk_id = models.Field(primary_key=True)
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=800)
    description = models.CharField(max_length=4000)
    genres = ArrayField(models.CharField(max_length=20, blank=True))
    rating_imdb = models.FloatField()
    year = models.IntegerField()
    film_length = models.IntegerField(null=True)
