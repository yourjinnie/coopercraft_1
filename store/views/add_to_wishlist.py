from django.views import View
from django.shortcuts import get_object_or_404, redirect
from store.models import Product


class AddToWishlistView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])

        # Get the wishlist from session, or create an empty list if not present
        wishlist = request.session.get('wishlist', [])

        # Add the product to the wishlist if it's not already there
        if product.id not in wishlist:
            wishlist.append(product.id)
            request.session['wishlist'] = wishlist

        # return redirect('wishlist')
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        else:
            return redirect('fallback-url')


