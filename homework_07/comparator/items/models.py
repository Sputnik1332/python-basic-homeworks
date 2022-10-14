from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name
