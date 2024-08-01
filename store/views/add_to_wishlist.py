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

        # Debugging: Print wishlist to ensure product is added
        print("Session Wishlist:", request.session['wishlist'])

        return redirect('wishlist')

# from django.views import View
# from django.shortcuts import get_object_or_404, redirect
# from store.models import Wishlist, Product
#
#
# class AddToWishlistView(View):
#     def get(self, request, *args, **kwargs):
#         product = get_object_or_404(Product, pk=kwargs['pk'])
#         if request.user.is_authenticated:
#             wishlist, created = Wishlist.objects.get_or_create(user=request.user, product=product)
#             if created:
#                 wishlist.save()
#         else:
#             wishlist = request.session.get('wishlist', [])
#             if product.id not in wishlist:
#                 wishlist.append(product.id)
#                 request.session['wishlist'] = wishlist
#             # Debugging: Print wishlist to ensure product is added
#             print("Session Wishlist:", request.session['wishlist'])
#         return redirect('wishlist')
#
