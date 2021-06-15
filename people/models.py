from django.db import models
from django.urls import reverse
from core import models as core_models

# Create your models here.


class Person(core_models.TimeStampedModel):

    Actor = "actor"
    Director = "director"
    Writer = "writer"

    KIND_CHOICE = (
        (Actor, "Actor"),
        (Director, "Director"),
        (Writer, "Writer"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=20, choices=KIND_CHOICE, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("people:detail", kwargs={"pk": self.pk})
