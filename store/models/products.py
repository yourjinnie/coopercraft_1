from django.db import models
from store.models.collections import Collection
from store.models.categories import Category
from store.models.size import Size
from store.models.colour import Color


class Product(models.Model):
    product_title = models.CharField(max_length=200)
    url = models.URLField(default="https://example.com")
    # slug = models.CharField(max_length=100,default=1)
    # status = models.BooleanField(default=False,help_text="0=default 1=Hidden")
    product_description=models.TextField(max_length=200)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=1)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    sales = models.IntegerField(default=0)  # Number of times the product has been sold
    type = models.CharField(max_length=255,default=1)  # Add this field to specify the product type
    colors = models.ManyToManyField(Color, related_name='products', blank=True)
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_title

    class Meta:
        ordering = ['-sales']  # Sort products by sales in descending order

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    # @staticmethod
    # def get_product_by_collection_id(collection_id):
    #     if collection_id:
    #         return Product.objects.filter(collection=collection_id)
    #     else:
    #         return Product.objects.all()

    @staticmethod
    def get_product_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


