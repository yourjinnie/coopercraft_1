from django.views import View
from django.shortcuts import render, redirect


class MyAccountOrder(View):
    def get(self, request):
        return render(request, 'my-account-order.html')