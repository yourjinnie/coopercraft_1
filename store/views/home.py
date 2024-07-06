from django.views import View
from django.shortcuts import render, redirect


class Home(View):
    def get(self, request):
        return redirect('homepage')