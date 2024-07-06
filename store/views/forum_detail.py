from django.views import View
from django.shortcuts import render, redirect


class ForumDetail(View):
    def get(self, request):
        return render(request, 'forum-detail.html')