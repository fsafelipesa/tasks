from django.db import models

from apps.artists.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.title
