from django.views import View
from django.shortcuts import render, redirect


class Wishlist(View):
    def get(self, request):
        return render(request, 'wishlist.html')