from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = (
        "username",
        "language",
        "bio",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
        "language",
    )

    list_filter = (
        "language",
        "preference",
        "favorite_book_genre",
        "favorite_movie_genre",
        "language",
        "superhost",
    )

    fieldsets = (
        (
            "custom profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                    "superhost",
                )
            },
        ),
    ) + UserAdmin.fieldsets
