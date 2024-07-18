# from django.shortcuts import render, redirect
# from django import views
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.http import HttpResponse
#
# class RegisterView(views.View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})
#
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('some_success_url')  # Replace 'some_success_url' with the actual URL or name of the success view
#         else:
#             return render(request, 'register.html', {'form': form})
#
