from django.views import View
from django.shortcuts import render

class Compare(View):
    def get(self,request):
        return render(request,'compare.html')