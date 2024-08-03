from django.views import View
from django.shortcuts import render,redirect
from store.models.products import Product
from store.models.collections import Collection
from store.models.banner import Banner
from store.models import NewArrival

class Index(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = Product.get_all_products()
        collections = Collection.objects.all()
        banners=Banner.objects.all()
        new_arrivals = NewArrival.objects.select_related('product').order_by('-arrival_date')[:10]  # Limit to 10 new arrivals
        context = {
            'products': products,
            'collections': collections,
            'banners':banners,
            'new_arrivals':new_arrivals,

        }
        return render(request, 'index.html',context)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1
        obj.save()
        return obj

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('homepage')