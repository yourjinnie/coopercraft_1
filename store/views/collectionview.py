from django.shortcuts import redirect,render
from django.views.generic import DetailView
from store.models.collections import Collection
from store.models.categories import Category
from store.models.products import Product
class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        collection = self. get_object()
        context['products'] = collection.product_set.all() # Add products to the context
        context['collection'] = collection
        context['categories'] = categories
        return context

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
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
        return redirect(request.path)

        # return render(request,'collection_detail.html')

