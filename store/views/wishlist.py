from django.shortcuts import render
from django.views import View
from store.models import Product

class Wishlist(View):
    def get(self, request, *args, **kwargs):
        # Get wishlist item IDs from session
        wishlist_ids = request.session.get('wishlist', [])

        # Fetch products based on wishlist IDs
        wishlist_items = Product.objects.filter(id__in=wishlist_ids)

        context = {
            'wishlist_items': wishlist_items
        }
        return render(request, 'wishlist.html', context)






# from django.shortcuts import render
# from django.views import View
# from store.models import Product, Wishlist
#
# class Wishlist(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             # Fetch wishlist items for authenticated users
#             wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
#         else:
#             # Fetch wishlist items from session for unauthenticated users
#             wishlist_ids = request.session.get('wishlist', [])
#             wishlist_items = Product.objects.filter(id__in=wishlist_ids)
#
#         context = {
#             'wishlist_items': wishlist_items
#         }
#         return render(request, 'wishlist.html', context)
