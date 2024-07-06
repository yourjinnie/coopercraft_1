from django.views import View
from django.shortcuts import render, redirect


class ForgotPassword(View):
    def get(self, request):
        return render(request, 'forgot-password.html')