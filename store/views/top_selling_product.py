from django.views.generic import ListView
from django.shortcuts import render,redirect
from store.models import Product

class TopSellingProductsView(ListView):
    model = Product
    template_name = 'top_selling_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all().order_by('-sales')[:5]


