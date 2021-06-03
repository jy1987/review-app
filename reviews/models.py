from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """review model definition"""

    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField(default="")
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey("books.Book", on_delete=CASCADE, null=True, blank=True)
    rating = models.IntegerField()

    def __str__(self):
        return str(self.created_by)
