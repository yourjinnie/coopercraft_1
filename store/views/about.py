from django.views import View
from django.shortcuts import render, redirect


class About(View):
    def get(self, request):
        return render(request, 'about.html')