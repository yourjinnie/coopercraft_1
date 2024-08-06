from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.register import Register
from store.models.address import Address

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

        elif 'update_address' in request.POST:
            user_id = request.session.get('id')
            address_type = request.POST.get('address_type')
            address_line_1 = request.POST.get('address_line_1')
            address_line_2 = request.POST.get('address_line_2', '')
            city = request.POST.get('city')
            state = request.POST.get('state')
            postal_code = request.POST.get('postal_code')
            country = request.POST.get('country')

            user = Register.objects.get(id=user_id)
            Address.objects.update_or_create(
                user=user,
                address_type=address_type,
                defaults={
                    'address_line_1': address_line_1,
                    'address_line_2': address_line_2,
                    'city': city,
                    'state': state,
                    'postal_code': postal_code,
                    'country': country
                }
            )

            return redirect('my-account')

        return render(request, 'accounts.html')

        # return render(request, 'accounts.html')

    # def account_redirect(request):
    #     if request.session.get('user'):
    #         return redirect('/my-account')
    #     else:
    #         return redirect('/account')
