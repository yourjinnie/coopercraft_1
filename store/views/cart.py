from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product

class Cart(View):
    def get(self, request):
        # Use an empty list as the default value if 'cart' is not in the session
        ids = list(request.session.get('cart', []))
        # Fetch products based on ids
        products = Product.objects.filter(id__in=ids)
        print(products)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('homepage')