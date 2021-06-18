from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):

    """Custom User Model"""

    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = ((PREF_BOOKS, "Books"), (PREF_MOVIES, "Movies"))

    LANGUAGE_EN = "english"
    LANGUAGE_KR = "korean"

    LANGUAGE_CHOICE = (
        (LANGUAGE_EN, "Engilsh"),
        (LANGUAGE_KR, "Korean"),
    )

    bio = models.TextField(default="", null=True)
    preference = models.CharField(choices=PREF_CHOICES, max_length=20, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICE, max_length=20, null=True)
    favorite_book_genre = models.ManyToManyField(
        "categories.Genre", related_name="users_book"
    )
    favorite_movie_genre = models.ManyToManyField(
        "categories.Genre", related_name="users_movie"
    )
    superhost = models.BooleanField(default=False)

    def get_absolute_url(self):

        return reverse("users:profile", kwargs={"pk": self.pk})
