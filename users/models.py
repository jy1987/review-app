from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Custom User Model"""

    LANGUAGE_EN = "english"
    LANGUAGE_KR = "korean"

    LANGUAGE_CHOICE = (
        (LANGUAGE_EN, "Engilsh"),
        (LANGUAGE_KR, "Korean"),
    )

    PREFER_BOOK = "book"
    PREFER_MOVIE = "movie"

    PREFER_CHOICE = (
        (PREFER_BOOK, "Book"),
        (PREFER_MOVIE, "Movie"),
    )

    bio = models.TextField(default="", null=True)
    preference = models.CharField(choices=PREFER_CHOICE, max_length=10, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICE, max_length=10, null=True)
    favorite_book_genre = models.CharField(max_length=40, null=True)
    favorite_movie_genre = models.CharField(max_length=40, null=True)
    superhost = models.BooleanField(default=False)
