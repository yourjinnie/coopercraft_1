from django.views import View
from django.shortcuts import render, redirect


class StoneCarving(View):
    def get(self, request):
        return render(request, 'stone-carving.html')