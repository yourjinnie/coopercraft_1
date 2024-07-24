from django.views import View
from django.shortcuts import render, get_object_or_404
from store.models import Product


class ZoomProductView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return render(request, 'zoom_product.html', {'product': product})