from django.views import View
from django.shortcuts import render
from store.models import Product

class ProductDetail(View):
    def get(self,request,id):
        prods=Product.objects.filter(id=id).first()
        context={
            'prods':prods,
        }
        return render(request,'product-detail.html',context)



