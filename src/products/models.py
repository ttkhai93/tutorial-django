from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25)
    info = models.JSONField(default=dict)

    def __str__(self) -> str:
        return self.name
