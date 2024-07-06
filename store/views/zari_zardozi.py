from django.views import View
from django.shortcuts import render, redirect


class ZariZardozi(View):
    def get(self, request):
        return render(request, 'zari-zardozi.html')