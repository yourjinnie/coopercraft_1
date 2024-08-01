from django.views import View
from django.shortcuts import render
from store.models import Product


class Compare(View):
    def get(self, request, *args, **kwargs):
        # Retrieve category_ids and collection_ids from session
        category_ids = request.session.get('category_ids', [])
        collection_ids = request.session.get('collection_ids', [])

        # For debugging, print the retrieved IDs
        print("Session Category IDs:", category_ids)
        print("Session Collection IDs:", collection_ids)

        # Fetch products based on the provided IDs
        pros = Product.objects.filter(
            id__in=category_ids + collection_ids
        )

        context = {
            'pros': pros
        }
        return render(request, 'compare.html', context)

# from django.views import View
# from django.shortcuts import render
#
# class Compare(View):
#     def get(self,request):
#         return render(request,'compare.html')