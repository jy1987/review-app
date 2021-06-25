from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """review model definition"""

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField(default="")
    movie = models.ForeignKey(
        "movies.Movie",
        related_name="reviews",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    book = models.ForeignKey(
        "books.Book", related_name="reviews", on_delete=CASCADE, null=True, blank=True
    )
    rating = models.IntegerField()

    def __str__(self):
        return str(self.created_by)

    def ratings(self):
        return int(self.rating)

    class Meta:
        ordering = ("-created",)

    """def movie_rating(self):
        if self.book == "":
            return int(self.rating)

    def book_rating(self):
        if self.movie == "":
            return int(self.rating)"""
