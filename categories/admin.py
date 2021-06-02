from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("kind",)

    list_filter = ("kind",)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):

    list_display = ("name",)

    list_filter = ("name",)
