from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        context={
            'products':products,
        }
        return render(request,'cart.html',context)
    def post(self, request):
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('cart')  # Assuming 'cart' is the name of your cart URL pattern