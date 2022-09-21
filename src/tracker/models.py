from django.db import models
from django.contrib.postgres.fields import ArrayField


class Film(models.Model):
    kinopoisk_id = models.Field(primary_key=True)
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=800)
    description = models.CharField(max_length=4000)
    genres = ArrayField(models.CharField(max_length=20, blank=True))
    rating_imdb = models.FloatField()
    year = models.IntegerField()
    film_length = models.IntegerField(null=True)
