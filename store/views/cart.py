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
    def post(self,request):
        return render(request, 'cart.html')