from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class FavList(core_models.TimeStampedModel):

    created_by = models.OneToOneField(
        "users.User", related_name="favs", on_delete=models.CASCADE
    )
    books = models.ManyToManyField("books.Book")
    movies = models.ManyToManyField("movies.Movie")

    def __str__(self):
        return str(self.created_by)
