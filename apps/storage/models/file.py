from django.db import models

from apps.storage.models import Directory


class File(models.Model):
    parent = models.ForeignKey(Directory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contents = models.BinaryField()

    def path(self):
        return f'{self.parent.path()}/{self.name}'

    def __str__(self):
        return self.path()
