from django.views import View
from django.shortcuts import render, redirect


class JuteCrafts(View):
    def get(self, request):
        return render(request, 'jute-crafts.html')