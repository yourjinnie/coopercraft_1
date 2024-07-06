from django.views import View
from django.shortcuts import render, redirect


class MyAccount(View):
    def get(self, request):
        return render(request, 'my-account.html')