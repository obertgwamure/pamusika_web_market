from django.contrib import admin

#regestering models
from . import models

admin.site.register(models.Category)
admin.site.register(models.Item)
