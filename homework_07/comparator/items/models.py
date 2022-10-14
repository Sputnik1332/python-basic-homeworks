from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField
    description = models.TextField(blank=True, null=False)
    price = models.FloatField

    def __str__(self):
        return self.name
