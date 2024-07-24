from django.views import View
from django.shortcuts import get_object_or_404, redirect
from store.models import Wishlist, Product

class RemoveFromWishlistView(View):
    def get(self, request, item_id, *args, **kwargs):
        if request.user.is_authenticated:
            # Authenticated user: remove item from the database
            wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
            wishlist_item.delete()
        else:
            # Unauthenticated user: remove item from the session
            wishlist = request.session.get('wishlist', [])
            if item_id in wishlist:
                wishlist.remove(item_id)
                request.session['wishlist'] = wishlist
            # Debugging: Print wishlist to ensure product is removed
            print("Session Wishlist after removal:", request.session['wishlist'])
        return redirect('wishlist')
