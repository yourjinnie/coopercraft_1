from django.views import View
from django.shortcuts import render


class Blank(View):
    def get(self,request):
        return render(request,'blank.html')



# from django.views import View
# from django.shortcuts import render,redirect,HttpResponseRedirect
# from store.models.registrer import Register
#
# class AccountView(View):
#     return_Url = None
#     def get(self, request):
#         AccountView.return_Url = request.GET.get('return_Url')
#         return render(request, 'accounts.html')
#
#     def post(self, request):
#         if 'register' in request.POST:
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')
#
#             if password != confirm_password:
#                 return render(request, 'accounts.html', {'error': 'Passwords do not match'})
#
#             registration = Register(name=name, email=email, password=password)
#             registration.save()
#             return redirect('account')  # Redirect to the account page
#
#         elif 'login' in request.POST:
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#
#             users = Register.objects.filter(email=email)
#             if not users.exists():
#                 return render(request, 'accounts.html', {'error': 'User does not exist'})
#
#             user = users.first()
#             if (user.password == password):
#                 request.session['user'] = user.name
#                 request.session['id'] = user.id
#                 # return redirect('homepage')  # Redirect to the homepage page
#             if AccountView.return_Url:
#                 return HttpResponseRedirect(AccountView.return_Url)
#             else:
#                 AccountView.return_Url = None
#                 return redirect('my-account')
#
#             # else:
#             #     return render(request, 'accounts.html', {'error': 'Invalid login credentials'})
#
#         return render(request, 'accounts.html')






# from django.views import View
# from django.shortcuts import render, redirect
# from store.models.products import Product
#
# class Cart(View):
#     def get(self, request):
#         cart = request.session.get('cart', {})
#         ids = list(cart.keys())
#         products = Product.get_products_by_id(ids)
#         context = {
#             'products': products,
#             'cart': cart,
#         }
#         return render(request, 'cart.html', context)
#
#     def post(self, request):
#         product_id = request.POST.get('product_id')
#         action = request.POST.get('action')
#         cart = request.session.get('cart', {})
#
#         if action == 'increment':
#             if product_id in cart:
#                 cart[product_id] += 1
#             else:
#                 cart[product_id] = 1
#         elif action == 'decrement':
#             if product_id in cart:
#                 if cart[product_id] > 1:
#                     cart[product_id] -= 1
#                 else:
#                     del cart[product_id]
#
#         request.session['cart'] = cart
#         return redirect('cart')  # Assuming 'cart' is the name of your cart URL pattern





