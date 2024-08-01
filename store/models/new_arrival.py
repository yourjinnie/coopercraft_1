from django.db import models
from store.models.products import Product

class NewArrival(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    arrival_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New Arrival: {self.product.product_title} on {self.arrival_date.strftime('%Y-%m-%d')}"