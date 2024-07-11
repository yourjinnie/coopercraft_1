from store.models.categories import Category

def category_context_processors(request):
    categories=Category.objects.all()
    return {'categories':categories}