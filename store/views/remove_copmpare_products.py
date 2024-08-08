from django.shortcuts import redirect
from django.views import View

class ClearComparisonView(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        if product_id:
            # Assuming 'compare_products' is a session-based list of product IDs
            compare_products = request.session.get('compare_products', [])
            if product_id in compare_products:
                compare_products.remove(product_id)
                request.session['compare_products'] = compare_products

        return redirect('homepage')  # Ensure this name matches the URL pattern name




