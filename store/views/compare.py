# from django.shortcuts import get_object_or_404, redirect, render
# from django.views import View
# from store.models import Product
#
#
# class CompareProductsView(View):
#     def get(self, request):
#         comparison_list = request.session.get('comparison_list', [])
#         products = Product.objects.filter(id__in=comparison_list)
#         return render(request, 'compare.html', {'products': products})

from django.shortcuts import get_object_or_404, render
from django.views import View
from store.models import Product

class CompareProductsView(View):
    template_name = 'compare.html'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        same_category_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
        same_collection_products = Product.objects.filter(collection=product.collection).exclude(pk=pk)[:4]
        context = {
            'product': product,
            'same_category_products': same_category_products,
            'same_collection_products': same_collection_products
        }
        return render(request, self.template_name, context)







