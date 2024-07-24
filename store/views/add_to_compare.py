from django.views import View
from django.shortcuts import get_object_or_404, redirect
from store.models import Compare, Product


class AddToCompareView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if request.user.is_authenticated:
            compare, created = Compare.objects.get_or_create(user=request.user, product=product)
            if created:
                compare.save()
        else:
            compare = request.session.get('compare', [])
            if product.id not in compare:
                compare.append(product.id)
                request.session['compare'] = compare
            # Debugging: Print wishlist to ensure product is added
            print("Session Compare:", request.session['compare'])
        return redirect('compare')

