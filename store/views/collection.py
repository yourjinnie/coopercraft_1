from django.views import View
from django.shortcuts import render

class Collection(View):
    def get(self,request):
        return render(request,'collection_detal.html')






