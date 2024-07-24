from django.db import models


class TopSellingProduct(models.Model):
    top_selling_product = models.CharField(max_length=100)
    url = models.URLField(default="https://example.com")

    def __str__(self):
        return self.new_arrivals




