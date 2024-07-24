from django.shortcuts import render
from django.views import View
from store.models import Product, Compare

class CompareView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            compare_items = Compare.objects.filter(user=request.user).select_related('product')
        else:
            compare_ids = request.session.get('compare', [])
            compare_items = Product.objects.filter(id__in=compare_ids)

        context = {
            'compare_items': compare_items
        }
        return render(request, 'compare.html', context)
