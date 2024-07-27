from django.views.generic import TemplateView
# from django.shortcuts import get_object_or_404
from store.models import Category, Collection, Product


class PriceComparisonView(TemplateView):
    template_name = 'compare.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get category and collection IDs from query parameters
        category_ids = self.request.GET.getlist('category_ids')
        collection_ids = self.request.GET.getlist('collection_ids')

        # Convert category_ids and collection_ids to lists of integers
        category_ids = [int(id) for id in category_ids]
        collection_ids = [int(id) for id in collection_ids]

        categories = Category.objects.filter(id__in=category_ids)
        collections = Collection.objects.filter(id__in=collection_ids)

        products = Product.objects.filter(category__in=categories, collection__in=collections).order_by('product_price')

        context['categories'] = categories
        context['collections'] = collections
        context['products'] = products
        return context

# from django.shortcuts import render
# from django.views import View
# from store.models import Product, Compare

# class CompareView(View):
#     def get(self, request, *args, **kwargs):
#
#         return render(request, 'compare.html')
