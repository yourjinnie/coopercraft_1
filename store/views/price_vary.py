from django.views import View
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from store.models.products import Product
from store.models.product_attr import ProductAttribute


class GetPrice(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        color_id = request.GET.get('color_id')
        size_id = request.GET.get('size_id')

        try:
            variant = ProductAttribute.objects.get(product_id=product_id, color_id=color_id, size_id=size_id)
            data = {
                'sale_price': variant.sale_price,
                'product_price': variant.price,
                'image_url': variant.var_image.url,  # Return the image URL
                # Add other fields as necessary
            }
            return JsonResponse(data)
        except ProductAttribute.DoesNotExist:
            return JsonResponse({'error': 'Product variant not found'}, status=404)