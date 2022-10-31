from typing import TYPE_CHECKING

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    url = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField(blank=True, null=True)

    if TYPE_CHECKING:
        objects: models.Manager

    def __str__(self):
        return self.name
