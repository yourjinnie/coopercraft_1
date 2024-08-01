# shop/middleware.py
from django.utils.deprecation import MiddlewareMixin
from store.models import Product

class BrowsingHistoryMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        product_id = view_kwargs.get('product_id')
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                history = request.session.get('browsing_history', [])
                if product_id not in history:
                    history.append(product_id)
                    if len(history) > 10:  # Keep only the last 10 viewed products
                        history.pop(0)
                    request.session['browsing_history'] = history
            except Product.DoesNotExist:
                pass
        return None
