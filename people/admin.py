from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Person)
class PeopleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "kind",
        "photo",
    )

    list_filter = (
        "name",
        "kind",
    )
