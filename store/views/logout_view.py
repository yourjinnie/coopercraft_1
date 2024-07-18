from django.shortcuts import render,redirect
from django import views

class LogoutView(views.View):
    def get(self,request):
        return redirect('homepage')
