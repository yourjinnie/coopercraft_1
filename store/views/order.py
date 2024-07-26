from django.views import View
from django.shortcuts import render
from store.models.orders import Order


class OrderConfirmationView(View):
    def get(self,request):
        customer = request.session.get('id')
        orders = Order.get_order_by_customer(customer)
        orders = orders.reverse()
        return render(request, 'order.html', {'orders': orders})
