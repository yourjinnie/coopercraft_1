from django.views import View
from django.shortcuts import render, redirect


class Compare(View):
    def get(self, request):
        return render(request, 'compare.html')