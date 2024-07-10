from django.views import View
from django.shortcuts import render,redirect,HttpResponseRedirect
from store.models.sign_up import SignUp

class Login(View):
    return_Url = None

    def get(self, request):
        Login.return_Url = request.GET.get('return_Url')
        return render(request, 'login.html')

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = SignUp.objects.get(email=email)
        if (user.password == password):
            request.session['user'] = user.name
            request.session['id'] = user.id

        if Login.return_Url:
            return HttpResponseRedirect(Login.return_Url)
        else:
            Login.return_Url = None
            return redirect('homepage')

        return render(request, 'login.html')