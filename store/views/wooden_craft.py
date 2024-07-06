from django.views import View
from django.shortcuts import render, redirect


class WoodenCraft(View):
    def get(self, request):
        return render(request, 'wooden-craft.html')