from django.views import View
from django.shortcuts import render, redirect


class Policy(View):
    def get(self, request):
        return render(request, 'policy.html')