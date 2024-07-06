from django.views import View
from django.shortcuts import render, redirect


class Account(View):
    def get(self, request):
        return render(request, 'account.html')