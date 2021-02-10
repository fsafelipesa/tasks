from django.contrib import admin
from apps.storage.models import Directory, File

admin.site.register(Directory)
admin.site.register(File)