from django.views import View
from django.shortcuts import render,redirect
# from store.models.products import Product
# from store.models.orders import Order
# from store.models.sign_up import SignUp


class Checkout(View):
    def get(self,request):
        return render(request, 'checkout.html')

    def post(self, request):
        # address = request.POST.get('address')
        # numbers = request.POST.get('number')
        # customer = request.session.get('id')
        # cart = request.session.get('cart')
        # products = Product.get_products_by_id(list(cart.keys()))
        #
        # for product in products:
        #     order = Order(
        #         customer=SignUp(id=customer),
        #         product=product,
        #         price=product.price,
        #         address=address,
        #         phone_no=numbers,
        #         quantity=cart.get(str(product.id))
        #
        #     )
        #     order.save()
        # request.session['cart']={}
        # return redirect('cart')
        return render(request,'checkout.html')