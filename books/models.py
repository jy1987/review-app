from categories.models import Category
from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Book(core_models.TimeStampedModel):

    title = models.CharField(max_length=60)
    year = models.DateField()
    genre = models.ForeignKey(
        "categories.Genre", related_name="books", on_delete=CASCADE, default=""
    )
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField()
    writer = models.ForeignKey("people.Person", related_name="books", on_delete=CASCADE)

    def __str__(self):
        return self.title

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        for review in all_reviews:
            all_rating += review.ratings()
        try:
            return all_rating / len(all_reviews)
        except ZeroDivisionError:
            return 0
