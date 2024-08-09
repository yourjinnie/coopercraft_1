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


def cart_products(request):
    cart = request.session.get('cart', {})
    cart_product_ids = cart.keys()
    cart_products = Product.objects.filter(id__in=cart_product_ids)
    return {'cart_products': cart_products}


def product_list_context(request):
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)

    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
        except ValueError:
            min_price = 0
            max_price = 500
    else:
        min_price = 0
        max_price = 500

    products = Product.objects.filter(product_price__gte=min_price, product_price__lte=max_price)
    return {'products': products}


def compare_products_count(request):
    product_ids = request.session.get('compare_products', [])
    compare_count = len(product_ids)
    return {
        'compare_count': compare_count
    }
