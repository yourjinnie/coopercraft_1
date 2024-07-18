from django.views import View
from django.shortcuts import render, redirect
from store.models.registrer import Register

class AccountView(View):
    def get(self, request):
        return render(request, 'accounts.html')

    def post(self, request):
        if 'register' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                return render(request, 'accounts.html', {'error': 'Passwords do not match'})

            registration = Register(name=name, email=email, password=password)
            registration.save()
            return redirect('account')  # Redirect to the account page

        elif 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            users = Register.objects.filter(email=email)
            if not users.exists():
                return render(request, 'accounts.html', {'error': 'User does not exist'})

            user = users.first()
            if user.password == password:
                request.session['user'] = user.name
                return redirect('my-account')  # Redirect to the my-account page
            else:
                return render(request, 'accounts.html', {'error': 'Invalid login credentials'})

        return render(request, 'accounts.html')
