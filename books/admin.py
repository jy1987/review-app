from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "genre",
        "rating",
        "writer",
        "total_rating",
    )

    list_filter = (
        "genre",
        "rating",
        "writer",
    )
