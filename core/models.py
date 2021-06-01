from django.db import models
from django.db.models.base import Model


class TimeStampedModel(models.Model):

    """Time Stamped Model(Abstract)"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
