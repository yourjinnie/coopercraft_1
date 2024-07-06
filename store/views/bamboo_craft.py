from django.views import View
from django.shortcuts import render, redirect


class BambooCraft(View):
    def get(self, request):
        return render(request, 'bamboo-craft.html')