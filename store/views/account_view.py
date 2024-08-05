from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.registrer import Register

class AccountView(View):
    def get(self, request):
        return_Url = request.GET.get('return_Url', '')
        return render(request, 'accounts.html', {'return_Url': return_Url})

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
            return_Url = request.POST.get('return_Url')

            users = Register.objects.filter(email=email)
            if not users.exists():
                return render(request, 'accounts.html', {'error': 'User does not exist'})

            user = users.first()
            if user.password == password:
                request.session['user'] = user.name
                request.session['id'] = user.id
                if return_Url:
                    return HttpResponseRedirect(return_Url)
                else:
                    return redirect('my-account')
            else:
                return render(request, 'accounts.html', {'error': 'Invalid login credentials'})

        return render(request, 'accounts.html')

    # def account_redirect(request):
    #     if request.session.get('user'):
    #         return redirect('/my-account')
    #     else:
    #         return redirect('/account')
