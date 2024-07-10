from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        print(ids)
        products=Product.get_products_by_id(ids)
        # print(products)
        return render(request,'cart.html',{'products':products})
    def post(self,request):
        return render(request, 'cart.html')