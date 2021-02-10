from django.contrib import admin
from apps.artists.models import Artist, Album

admin.site.register(Artist)
admin.site.register(Album)