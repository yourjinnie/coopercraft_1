from django.views import View
from django.shortcuts import render, redirect


class Forum(View):
    def get(self, request):
        return render(request, 'forum.html')