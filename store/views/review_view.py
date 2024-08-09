from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from store.models import Product, Review
from store.forms import ReviewForm

class AddReviewView(FormView):
    form_class = ReviewForm
    template_name = 'product_detail.html'

    def form_valid(self, form):
        # Get the product based on the primary key in the URL
        product = get_object_or_404(Product, pk=self.kwargs['pk'])

        # Save the review with the associated product
        review = form.save(commit=False)
        review.product = product
        review.save()

        # Redirect to the product detail page after saving the review
        return redirect('product_detail', pk=product.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return context

        # Redirect to the product detail page
        return redirect('product-detail', pk=product.pk)
