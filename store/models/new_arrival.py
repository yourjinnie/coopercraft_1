from django.db import models


class NewArrival(models.Model):
    new_arrivals = models.CharField(max_length=100)
    url = models.URLField(default="https://example.com")

    def __str__(self):
        return self.new_arrivals




