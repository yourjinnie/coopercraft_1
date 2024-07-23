from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from store.models.products import Product
from store.models.cart import Cart  # Assuming the Cart model is in store.models.cart

class AddToCart(View):
    def get(self, request, product_id=None):
        cart_items = Cart.objects.filter(user=request.user)
        context = {
            'cart_items': cart_items,
        }
        return render(request, 'cart.html', context)

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('cart')  # Adjust the redirect as needed
