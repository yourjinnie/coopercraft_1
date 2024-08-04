from django.views import View
from django.shortcuts import render


class Blank(View):
    def get(self,request):
        return render(request,'blank.html')


# from django.shortcuts import redirect, render
# from django.views.generic import DetailView
# from store.models.collections import Collection
# from store.models.products import Product
#
#
# class CollectionDetailView(DetailView):
#     model = Collection
#     template_name = 'collection_detail.html'
#     context_object_name = 'collection'
#
#     def dispatch(self, request, *args, **kwargs):
#         # Ensure cart is initialized in session
#         if 'cart' not in request.session:
#             request.session['cart'] = {}
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         collection = self.get_object()
#
#         # Add filtered products to the context (products in the current collection)
#         context['products'] = collection.product_set.all()
#         context['collection'] = collection
#
#         # Add browsing history products
#         history = self.request.session.get('browsing_history', [])
#         history_products = Product.objects.filter(id__in=history)
#         context['history_products'] = history_products
#
#         # Add cart information to the context
#         context['cart'] = self.request.session.get('cart', {})
#
#         return context

# from django.shortcuts import redirect, render
# from django.views.generic import DetailView
# from store.models.collections import Collection
# from store.models.products import Product
#
#
# class CollectionDetailView(DetailView):
#     model = Collection
#     template_name = 'collection_detail.html'
#     context_object_name = 'collection'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Add all products to the context
#         context['products'] = Product.objects.all()
#
#         # Add browsing history products
#         history = self.request.session.get('browsing_history', [])
#         history_products = Product.objects.filter(id__in=history)
#         context['history_products'] = history_products
#
#         # Add cart products with details
#         cart = self.request.session.get('cart', {})
#         cart_product_ids = cart.keys()
#         cart_products = Product.objects.filter(id__in=cart_product_ids)
#         cart_products_with_details = []
#         for product in cart_products:
#             cart_products_with_details.append({
#                 'product': product,
#                 'quantity': cart[str(product.id)]
#             })
#         context['cart_products'] = cart_products_with_details
#
#         return context
#
#     def get(self, request, *args, **kwargs):
#         cart = request.session.get('cart')
#         if not cart:
#             request.session['cart'] = {}
#         return super().get(request, *args, **kwargs)






