from django.contrib import admin
from store.models.products import Product
from store.models.collections import Collection
from store.models.categories import Category
from store.models.orders import Order
from store.models.registrer import Register
from store.models.cart import Cart
from store.models.cart_item import CartItem
from store.models.wishlist import Wishlist
from store.models.compare import Compare


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_title','collection', 'category', 'product_description', 'product_price', 'rating','image']


admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Compare)
admin.site.register(Order)
admin.site.register(Register)


