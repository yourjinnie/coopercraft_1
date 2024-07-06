from django.views import View
from django.shortcuts import render, redirect


class Terracotta(View):
    def get(self, request):
        return render(request, 'terracotta.html')