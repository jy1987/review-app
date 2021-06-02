from datetime import timezone
from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=60)

    class Meta:
        abstract: True

    def __str__(self):
        return self.name


class Genre(AbstractItem):

    pass


class Category(core_models.TimeStampedModel):

    Book = "book"
    Movie = "movie"
    Total = "all"

    KIND_CHOICE = (
        (Book, "Book"),
        (Movie, "Movie"),
        (Total, "All"),
    )

    kind = models.CharField(max_length=20, choices=KIND_CHOICE, default="All")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.kind)
