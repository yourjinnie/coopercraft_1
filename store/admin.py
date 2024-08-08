from django.contrib import admin
from store.models.products import Product
from store.models.collections import Collection
from store.models.categories import Category
from store.models.orders import Order
from store.models.order_item import OrderItem
from store.models.register import Register
from store.models.cart import Cart
from store.models.cart_item import CartItem
from store.models.wishlist import Wishlist
from store.models.compare import Compare
from store.models.banner import Banner
from store.models.new_arrival import NewArrival
from store.models.address import Address
from store.models.size import Size
from store.models.colour import Color
from store.models.product_attr import ProductAttribute


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product_title','collection', 'category', 'product_description', 'product_price','sale_price','sales', 'rating','image']


admin.site.register(Collection)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(Compare)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Register)
admin.site.register(Banner)
admin.site.register(NewArrival)
admin.site.register(Address)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductAttribute)



