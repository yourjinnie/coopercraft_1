from django.contrib import admin
from store.models.products import Product
from store.models.collections import Collection
from store.models.categories import Category
# 'collection', 'category',

# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_title', 'product_description', 'product_price', 'rating','image']


admin.site.register(Collection)
admin.site.register(Category)
