from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "get_cover",
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

    def get_cover(self, obj):
        return mark_safe(f"<img width='35px' src={obj.cover_image.url} />")
