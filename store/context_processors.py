from store.models.categories import Category
from store.models.products import Product

def category_context_processors(request):
    categories=Category.objects.all()
    return {'categories':categories}

def product_context_processors(request):
    # ids = list(request.session.get('cart').keys())
    cart = request.session.get('cart', {})  # Provide an empty dictionary as the default value
    ids = list(cart.keys())
    products = Product.get_products_by_id(ids)
    return {'products':products}

from store.models.products import Product

def cart_products(request):
    cart = request.session.get('cart', {})
    cart_product_ids = cart.keys()
    cart_products = Product.objects.filter(id__in=cart_product_ids)
    return {'cart_products': cart_products}
