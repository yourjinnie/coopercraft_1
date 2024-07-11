from django.views import View
from django.shortcuts import render

class Category(View):
    def get(self,request):
        return render(request,'category.html')







