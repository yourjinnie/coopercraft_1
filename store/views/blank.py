from django.views import View
from django.shortcuts import render


class Blank(View):
    def get(self,request):
        return render(request,'blank.html')



# from django.views import View
# from django.shortcuts import render, redirect
# from store.models.products import Product
#
# class Cart(View):
#     def get(self, request):
#         cart = request.session.get('cart', {})
#         ids = list(cart.keys())
#         products = Product.get_products_by_id(ids)
#         context = {
#             'products': products,
#             'cart': cart,
#         }
#         return render(request, 'cart.html', context)
#
#     def post(self, request):
#         product_id = request.POST.get('product_id')
#         action = request.POST.get('action')
#         cart = request.session.get('cart', {})
#
#         if action == 'increment':
#             if product_id in cart:
#                 cart[product_id] += 1
#             else:
#                 cart[product_id] = 1
#         elif action == 'decrement':
#             if product_id in cart:
#                 if cart[product_id] > 1:
#                     cart[product_id] -= 1
#                 else:
#                     del cart[product_id]
#
#         request.session['cart'] = cart
#         return redirect('cart')  # Assuming 'cart' is the name of your cart URL pattern





