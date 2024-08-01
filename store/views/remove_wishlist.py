from django.views import View
from django.shortcuts import redirect
from store.models import Product


class RemoveFromWishlistView(View):
    def get(self, request, item_id, *args, **kwargs):
        # Retrieve the wishlist from the session, or initialize it as an empty list if it doesn't exist
        wishlist = request.session.get('wishlist', [])

        # Ensure item_id is an integer, as session data might store it as a string
        item_id = int(item_id)

        # Remove the item from the wishlist if it's present
        if item_id in wishlist:
            wishlist.remove(item_id)
            request.session['wishlist'] = wishlist

        return redirect('wishlist')

# from django.views import View
# from django.shortcuts import get_object_or_404, redirect
# from store.models import Wishlist, Product
#
# class RemoveFromWishlistView(View):
#     def get(self, request, item_id, *args, **kwargs):
#         if request.user.is_authenticated:
#             # Authenticated user: remove item from the database
#             wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
#             wishlist_item.delete()
#         else:
#             # Unauthenticated user: remove item from the session
#             wishlist = request.session.get('wishlist', [])
#             if item_id in wishlist:
#                 wishlist.remove(item_id)
#                 request.session['wishlist'] = wishlist
#         return redirect('wishlist')
