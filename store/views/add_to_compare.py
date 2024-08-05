from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from store.models import Product


class AddToComparisonView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        comparison_list = request.session.get('comparison_list', [])
        comparison_type = request.session.get('comparison_type', None)

        if comparison_type is None or product.type == comparison_type:
            if product_id not in comparison_list:
                if len(comparison_list) < 4:
                    comparison_list.append(product_id)
                    request.session['comparison_list'] = comparison_list
                    request.session['comparison_type'] = product.type
                else:
                    # Set an error message in the session and redirect to a suitable page
                    request.session['comparison_error'] = 'You can only compare products of the same type.'
                    return redirect('product_detail', product_id=product_id)  # Adjust the redirect target as needed

        # return redirect('compare_products')
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        else:
            return redirect('fallback-url')  # Use a fallback URL in case HTTP_REFERER is not available