from django.shortcuts import redirect, render
# from django.shortcuts import get_object_or_404
# from django.views.generic import ListView
from django.views import View
from store.models.categories import Category
from store.models.products import Product
# from store.models.collections import Collection


class CategoryView(View):
    # class CategoryView(ListView):
    #     model = Product
    #     template_name = 'category.html'
    #     context_object_name = 'products'
    #
    #     def get_queryset(self):
    #         category_id = self.kwargs['category_id']
    #         self.category = get_object_or_404(Category, id=category_id)
    #         return Product.objects.filter(category=self.category)
    #
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['category'] = self.category
    #         return context
    #
    #     def get(self, request, *args, **kwargs):
    #         cart = request.session.get('cart')
    #         if not cart:
    #             request.session['cart'] = {}
    #         return super().get(request, *args, **kwargs)
    def get(self, request,*args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = Product.get_all_products()
        categories = Category.objects.all()
        category_id = request.GET.get('category')
        if category_id:
           products = Product.get_product_by_category_id(category_id)
        else:
           products = Product.get_all_products()
        context = {
           'products': products,
           'categories': categories
        }

        return render(request, 'category.html', context)

def post(self, request,*args, **kwargs):
    product = request.POST.get('product')
    remove = request.POST.get('remove')
    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(product)
        if quantity:
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] = quantity - 1
            else:
                cart[product] = quantity + 1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
    request.session['cart'] = cart
    return redirect(request.path)

    # return render(request, 'category.html')


# category = get_object_or_404(Category, pk=category_id)
# collection = get_object_or_404(Collection, pk=collection_id)
# products = Product.objects.filter(category=category)
# context = {
#     'collection': collection,
#     'category': category,
#     'products': products,
# }