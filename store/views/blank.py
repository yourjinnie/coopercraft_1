from django.views import View
from django.shortcuts import render


class Blank(View):
    def get(self,request):
        return render(request,'blank.html')




