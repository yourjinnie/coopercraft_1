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