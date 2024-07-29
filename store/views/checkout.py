from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product
from store.models.orders import Order
from store.models.registrer import Register
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/account/')
class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        # Fetch products from the cart session or database
        # products = self.get_cart_products(request), {'products': products}
        return render(request, 'checkout.html')
    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        billing_address = request.POST.get('billing_address')
        city = request.POST.get('city')
        phone_no = request.POST.get('phone_no')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')
        customer = request.session.get('id')

        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                customer=Register(id=customer),
                product=product,
                fname=fname,
                lname=lname,
                email=email,
                city=city,
                zipcode=zipcode,
                country=country,
                price=product.product_price,
                address=billing_address,
                phone_no=phone_no,
                quantity=cart.get(str(product.id))

            )
            saved_order = order.place_order()
        request.session['cart']={}
        messages.success(request, 'Order successfully placed')
        # return render(request, 'index.html')
        return redirect('homepage')
