from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from core import models as core_models

# Create your models here.


class Movie(core_models.TimeStampedModel):

    title = models.CharField(max_length=60)
    year = models.DateField()
    cover_image = models.ImageField(upload_to="movie_photos", blank=True)
    rating = models.IntegerField()
    genre = models.ManyToManyField("categories.Genre", related_name="movie")
    director = models.ForeignKey(
        "people.Person", related_name="movie_director", on_delete=CASCADE
    )
    cast = models.ManyToManyField("people.Person", related_name="movie_cast")

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
