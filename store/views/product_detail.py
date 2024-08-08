from django.shortcuts import render
from django.views import View
from store.models import Product, Color, Size

class ProductDetail(View):
    def get(self, request, id):
        prods = Product.objects.filter(id=id).first()
        queryset = Product.objects.order_by('-view_count')[:8]  # Top 8 popular products
        context = {
            'prods': prods,
            'queryset': queryset,
            'colors': Color.objects.all(),  # Fetch color options
            'sizes': Size.objects.all(),    # Fetch size options
        }
        return render(request, 'product-detail.html', context)





# # from django.views import View
# # from django.shortcuts import render,redirect
# # from store.models import Product
# #
# # class ProductDetail(View):
# #     def get(self,request,id):
#         prods=Product.objects.filter(id=id).first()
#         queryset = Product.objects.order_by('-view_count')[:10]  # Top 10 popular products
# #         context={
# #             'prods':prods,
# #             'queryset':queryset,
# #         }
# #         return render(request,'product-detail.html',context)
#
#
#
#
#
