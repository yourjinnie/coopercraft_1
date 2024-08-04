from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from store.models import Product


class CompareProductsView(View):
    def get(self, request):
        comparison_list = request.session.get('comparison_list', [])
        products = Product.objects.filter(id__in=comparison_list)
        return render(request, 'compare.html', {'products': products})








