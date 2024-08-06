from django.views import View
from django.shortcuts import render, redirect
from store.models.products import Product
from store.models.orders import Order
from store.models.register import Register
from store.models.address import Address
from django.contrib import messages
import random

class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        customer_id = request.session.get('id')
        user = Register.objects.get(id=customer_id)
        billing_address = Address.objects.filter(user=user, address_type='billing').first()
        shipping_address = Address.objects.filter(user=user, address_type='shipping').first()

        context = {
            'user': user,
            'billing_address': billing_address,
            'shipping_address': shipping_address,
        }
        return render(request, 'checkout.html', context)

    def post(self, request):
        customer_id = request.session.get('id')
        user = Register.objects.get(id=customer_id)

        billing_first_name = request.POST.get('fname')
        billing_last_name = request.POST.get('lname')
        billing_company_name = request.POST.get('cname')
        billing_address1 = request.POST.get('billing_address')
        billing_address2 = request.POST.get('billing_address2', '')
        billing_city = request.POST.get('city')
        billing_state = request.POST.get('state')
        billing_zipcode = request.POST.get('zipcode')
        billing_phone = request.POST.get('phone')
        billing_email = request.POST.get('email')
        billing_payment_option=request.POST.get('payment_option')
        tracno = 'coopcraft' + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=tracno) is None:
            tracno = 'coopcraft' + str(random.randint(1111111, 9999999))
        billing_tracking_no = tracno
        shipping_different = request.POST.get('differentaddress')

        if shipping_different:
            shipping_first_name = request.POST.get('shipping_fname')
            shipping_last_name = request.POST.get('shipping_lname')
            shipping_company_name = request.POST.get('shipping_cname')
            shipping_address1 = request.POST.get('shipping_address')
            shipping_address2 = request.POST.get('shipping_address2', '')
            shipping_city = request.POST.get('shipping_city')
            shipping_state = request.POST.get('shipping_state')
            shipping_zipcode = request.POST.get('shipping_zipcode')
            shipping_phone = request.POST.get('shipping_phone')
        else:
            shipping_first_name = billing_first_name
            shipping_last_name = billing_last_name
            shipping_company_name = billing_company_name
            shipping_address1 = billing_address1
            shipping_address2 = billing_address2
            shipping_city = billing_city
            shipping_state = billing_state
            shipping_zipcode = billing_zipcode
            shipping_phone = billing_phone

        # Save or update billing address
        Address.objects.update_or_create(
            user=user,
            address_type='billing',
            defaults={
                'first_name': billing_first_name,
                'last_name': billing_last_name,
                'company_name': billing_company_name,
                'address_line_1': billing_address1,
                'address_line_2': billing_address2,
                'city': billing_city,
                'state': billing_state,
                'postal_code': billing_zipcode,
                'country': 'Country Placeholder',  # Set the default or get from user input
                'phone': billing_phone,
                'email': billing_email
            }
        )

        # Save or update shipping address
        Address.objects.update_or_create(
            user=user,
            address_type='shipping',
            defaults={
                'first_name': shipping_first_name,
                'last_name': shipping_last_name,
                'company_name': shipping_company_name,
                'address_line_1': shipping_address1,
                'address_line_2': shipping_address2,
                'city': shipping_city,
                'state': shipping_state,
                'postal_code': shipping_zipcode,
                'country': 'Country Placeholder',  # Set the default or get from user input
                'phone': shipping_phone,
            }
        )

        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                customer=user,
                product=product,
                fname=billing_first_name,
                lname=billing_last_name,
                email=billing_email,
                city=billing_city,
                zipcode=billing_zipcode,
                country='Country Placeholder',  # Set the default or get from user input
                price=product.product_price,
                address_line_1=billing_address1,
                address_line_2=billing_address2,
                phone_no=billing_phone,
                payment_option=billing_payment_option,
                tracking_no=billing_tracking_no,
                quantity=cart.get(str(product.id))
            )
            saved_order = order.place_order()


        request.session['cart'] = {}
        messages.success(request, 'Your Order has been Placed Successfully..')
        return redirect('homepage')
