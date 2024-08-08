from store.models.products import Product
from store.models.colour import Color
from store.models.size import Size
from django.db import models

# Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    var_image = models.ImageField(upload_to='var_images/',default='images/default.jpg')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('product', 'color', 'size')

    def __str__(self):
        return f"{self.product.product_title} - {self.color.name} - {self.size.size}"