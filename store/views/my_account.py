from django.views import View
from django.shortcuts import render
from store.models import Address
from store.models.orders import Order
from store.models.register import Register

class MyAccount(View):
    def get(self,request):
        customer_id = request.session.get('id')
        user = Register.objects.get(id=customer_id)
        try:
            billing_address = Address.objects.get(user=user, address_type='billing')
        except Address.DoesNotExist:
            billing_address = None

        try:
            shipping_address = Address.objects.get(user=user, address_type='shipping')
        except Address.DoesNotExist:
            shipping_address = None

        orders = Order.get_order_by_customer(customer_id)
        orders = orders.reverse()

        context = {
            'billing_address': billing_address,
            'shipping_address': shipping_address,
            'orders': orders
        }

        return render(request, 'my-accounts.html', context)


# from django.views import View
# from django.shortcuts import render
# from store.models.orders import Order

# class MyAccount(View):
#     def get(self, request):
#         customer = request.session.get('id')
#         orders = Order.get_order_by_customer(customer)
#         orders = orders.reverse()
#         return render(request, 'my-accounts.html', {'orders': orders})

