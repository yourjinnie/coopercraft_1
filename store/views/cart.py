from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart', {}).keys())
        products = Product.get_products_by_id(ids)
        context = {
            'products': products,
        }
        return render(request, 'cart.html', context)

    def post(self, request):
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        if product_id and action:
            if action == 'increase':
                cart[product_id] = cart.get(product_id, 0) + 1
            elif action == 'decrease':
                if cart.get(product_id, 0) > 1:
                    cart[product_id] -= 1
                else:
                    cart.pop(product_id)
            elif action == 'remove':
                cart.pop(product_id, None)

        request.session['cart'] = cart
        return redirect('cart')

