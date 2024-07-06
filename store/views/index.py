from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product
from store.models.collections import Collection

class Index(View):
    def get(self, request):
        # cart = request.session.get('cart')
        # if not cart:
        #     request.session['cart'] = {}
        products = Product.get_all_products()
        collections = Collection.objects.all()
        context = {
            'products': products,
            'collections': collections
        }
        return render(request, 'index.html',context)