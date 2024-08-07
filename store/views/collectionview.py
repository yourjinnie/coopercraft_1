from django.shortcuts import redirect,render
from django.views.generic import DetailView
from store.models.collections import Collection
from store.models.products import Product

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection = self. get_object()
        # Get the price range from the request
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        # Filter products by the collection and price range
        products = collection.product_set.all()
        if min_price and max_price:
            products = products.filter(sale_price__gte=min_price, sale_price__lte=max_price)

        context['products'] = products
        context['collection'] = collection

        # Add browsing history products
        history = self.request.session.get('browsing_history', [])
        history_products = Product.objects.filter(id__in=history)
        context['history_products'] = history_products

        # Fetch cart products
        cart = self.request.session.get('cart', {})
        cart_product_ids = cart.keys()
        cart_products = Product.objects.filter(id__in=cart_product_ids)
        context['cart_products'] = cart_products

        return context

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()  # Adjust this query as needed
    #     return context





    # def get(self, request, *args, **kwargs):
    #     cart = request.session.get('cart')
    #     if not cart:
    #         request.session['cart'] = {}
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     product = request.POST.get('product')
    #     remove = request.POST.get('remove')
    #     cart = request.session.get('cart')
    #
    #     if cart:
    #         quantity = cart.get(product)
    #         if quantity:
    #             if remove:
    #                 if quantity <= 1:
    #                     cart.pop(product)
    #                 else:
    #                     cart[product] = quantity - 1
    #             else:
    #                 cart[product] = quantity + 1
    #         else:
    #             cart[product] = 1
    #     else:
    #         cart = {}
    #         cart[product] = 1
    #     request.session['cart'] = cart
    #     return redirect(request.path)
    #
    #     # return render(request,'collection_detail.html')

