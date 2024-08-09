from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin,
from store.models import Address,Register

class EditBillingAddressView(View):
    template_name = 'my-account.html'

    def get(self, request):
        customer_id = request.session.get('id')
        user = get_object_or_404(Register, id=customer_id)  # Get the user from the session
        billing_address = get_object_or_404(Address, user=user, address_type='Billing')
        context = {'billing_address': billing_address}
        return render(request, self.template_name, context)

    def post(self, request):
        customer_id = request.session.get('id')
        user = get_object_or_404(Register, id=customer_id)  # Get the user from the session
        billing_address = get_object_or_404(Address, user=user, address_type='Billing')


        billing_address.address_line_1 = request.POST['address_line_1']
        billing_address.address_line_2 = request.POST.get('address_line_2', '')
        billing_address.city = request.POST['city']
        billing_address.state = request.POST['state']
        billing_address.postal_code = request.POST['postal_code']
        billing_address.phone = request.POST['phone']
        billing_address.email = request.POST['email']
        billing_address.address_type = 'Billing'  # Ensure correct value
        billing_address.save()
        return redirect(reverse('my-account'))