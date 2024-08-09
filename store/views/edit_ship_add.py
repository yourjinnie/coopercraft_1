from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin,
from store.models import Address,Register

class EditShippingAddressView(View):
    template_name = 'my-account.html'

    def get(self, request):
        customer_id = request.session.get('id')
        user = get_object_or_404(Register, id=customer_id)  # Get the user from the session
        shipping_address = get_object_or_404(Address, user=user, address_type='Shipping')
        context = {'shipping_address': shipping_address}
        return render(request, self.template_name, context)

    def post(self, request):
        customer_id = request.session.get('id')
        user = get_object_or_404(Register, id=customer_id)  # Get the user from the session
        shipping_address = get_object_or_404(Address, user=user, address_type='Shipping')

        shipping_address.address_line_1 = request.POST['address_line_1']
        shipping_address.address_line_2 = request.POST.get('address_line_2', '')
        shipping_address.city = request.POST['city']
        shipping_address.state = request.POST['state']
        shipping_address.postal_code = request.POST['postal_code']
        shipping_address.phone = request.POST['phone']
        shipping_address.email = request.POST['email']
        shipping_address.address_type = 'Shipping'  # Ensure correct value
        shipping_address.save()
        return redirect(reverse('my-account'))