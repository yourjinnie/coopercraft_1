from django.http import JsonResponse
from django.views import View
import json

class RemoveCompareView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        product_id = data.get('product_id')
        compare_product_ids = request.session.get('compare_product_ids', [])
        if int(product_id) in compare_product_ids:
            compare_product_ids.remove(int(product_id))
            request.session['compare_product_ids'] = compare_product_ids
        return JsonResponse({'status': 'success', 'product_id': product_id})
