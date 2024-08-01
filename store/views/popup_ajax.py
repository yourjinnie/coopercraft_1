from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from store.models import Product

class AjaxPopupView(View):
    def get(self, request, *args, **kwargs):
        data = Product.objects.all()
        html = render_to_string('popup_content.html', {'data': data})
        return JsonResponse({'html': html})