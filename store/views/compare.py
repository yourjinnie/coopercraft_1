from django.shortcuts import render,get_object_or_404
from django.views import View
from store.models import Product


class CompareProductsView(View):
    def get(self, request, pk):
        # Assuming you have a product with this ID
        product = get_object_or_404(Product, pk=pk)

        # Get products in the same category
        same_category_products = Product.objects.filter(category=product.category).exclude(pk=pk)

        # Get products in the same collection
        same_collection_products = Product.objects.filter(collection=product.collection).exclude(pk=pk)

        # Combine products and remove duplicates if any
        combined_products = same_category_products | same_collection_products
        combined_products = combined_products.distinct()[:4]

        return render(request, 'compare.html', {
            'combined_products': combined_products,
        })
