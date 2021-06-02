from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Movie(core_models.TimeStampedModel):

    title = models.CharField(max_length=60)
    year = models.DateField()
    cover_image = models.ImageField()
    rating = models.IntegerField()
    category = models.ManyToManyField("categories.Category", related_name="movie")
    director = models.ForeignKey(
        "people.Person", related_name="movie_director", on_delete=CASCADE
    )
    cast = models.ManyToManyField("people.Person", related_name="movie_cast")

    def __str__(self):
        return self.title
