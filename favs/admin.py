from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.FavList)
class FavAdmin(admin.ModelAdmin):

    list_display = ("created_by",)

    list_filter = ("created_by",)
