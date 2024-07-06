from django.views.generic import DetailView
from store.models.collections import Collection
from store.models.products import Product
class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collection = self.get_object()
        context['products'] = collection.product_set.all() # Add products to the context
        context['collection'] = collection
        return context


