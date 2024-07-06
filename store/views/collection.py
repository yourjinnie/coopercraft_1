from django.shortcuts import render,get_object_or_404
from django.views import View
from store.models.products import Product
from store.models.collections import Collection



class Collection(View):
    def get(self, request,product_id):
        product = get_object_or_404(Product, id=product_id)
        collections = Collection.objects.filter(product=product)
        context = {
            'product':product,
            'collections': collections
        }
        return render(request, 'collection_detail.html',context)

    # products = Product.get_all_products()
    # collections = Collection.objects.all()
    # collection_id = request.GET.get('collection_id')
    # if collection_id:
    #     products = Product.get_product_by_collection_id(collection_id)
    # else:
    #     products = Product.get_all_products()