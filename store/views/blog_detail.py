from django.views import View
from django.shortcuts import render, redirect


class BlogDetail(View):
    def get(self, request):
        return render(request, 'blog-detail.html')