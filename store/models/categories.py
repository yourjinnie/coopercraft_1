from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)
    url = models.URLField(default="https://example.com")

    def __str__(self):
        return self.category




