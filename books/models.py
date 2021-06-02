from categories.models import Category
from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Book(core_models.TimeStampedModel):

    title = models.CharField(max_length=60)
    year = models.DateField()
    category = models.ForeignKey(
        "categories.Category", related_name="books", on_delete=CASCADE
    )
    cover_image = models.ImageField()
    rating = models.IntegerField()
    writer = models.ForeignKey("people.Person", related_name="books", on_delete=CASCADE)

    def __str__(self):
        return self.title
