from django.views import View
from django.shortcuts import render,redirect

class ProductDetail(View):
    def get(self,request):

        return render(request,'product-detail.html',context)
