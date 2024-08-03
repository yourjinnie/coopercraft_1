from django.shortcuts import redirect, render
from django.views.generic import DetailView
from store.models.categories import Category
from store.models.products import Product

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        category = self.get_object()
        context['products'] = category.product_set.all()  # Add products to the context
        context['category'] = category
        context['categories'] = categories

        # Add browsing history products
        history = self.request.session.get('browsing_history', [])
        history_products = Product.objects.filter(id__in=history)
        context['history_products'] = history_products

        return context

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  # Adjust this query as needed
        return context



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