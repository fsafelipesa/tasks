from django.db import models


class Directory(models.Model):
    parent = models.ForeignKey('Directory', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def path(self):
        return f'{self.parent.path()}/{self.name}' if self.parent else f'/{self.name}'

    def __str__(self):
        return self.path()
