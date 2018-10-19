from django.contrib import admin
from . import models

admin.site.register(models.RealObject)
admin.site.register(models.Abbreviation)
admin.site.register(models.IllegalLetter)

# Register your models here.
