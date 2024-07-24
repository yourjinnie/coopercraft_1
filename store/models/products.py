from django.db import models
from store.models.collections import Collection
from store.models.categories import Category
from store.models.new_arrival import NewArrival
from store.models.top_selling_product import TopSellingProduct


class Product(models.Model):
    product_title = models.CharField(max_length=200)
    url = models.URLField(default="https://example.com")
    # slug = models.CharField(max_length=100,default=1)
    # status = models.BooleanField(default=False,help_text="0=default 1=Hidden")
    product_description=models.TextField(max_length=200)
    product_price=models.DecimalField(max_digits=10,decimal_places=2)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=1)
    top_selling_product = models.ForeignKey(TopSellingProduct, on_delete=models.CASCADE, blank=True, null=True)
    new_arrivals = models.ForeignKey(NewArrival, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.product_title

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


