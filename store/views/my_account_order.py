from django.views import View
from django.shortcuts import render, redirect
from store.models.orders import Order


class MyAccountOrder(View):
    def get(self, request):
        customer = request.session.get('id')
        orders = Order.get_order_by_customer(customer)
        orders = orders.reverse()
        return render(request, 'my-account-order.html', {'orders': orders})