from django import views
from django.shortcuts import render,redirect


class Remove(views.View):
    def get(self,request,item_id):
        cart = request.session.get('cart', {})
        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session['cart'] = cart
        return redirect('cart')




