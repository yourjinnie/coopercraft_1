from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from store.models import Product, Color, Size, Review
from django.db.models import F, FloatField, ExpressionWrapper
from store.forms import ReviewForm


class ProductDetail(View):
    def get(self, request, id):
        prods = get_object_or_404(Product, id=id)
        queryset = Product.objects.order_by('-view_count')[:4]  # Top 4 popular products

        # Define a weighted popularity score
        popular_products = Product.objects.annotate(
            popularity=ExpressionWrapper(
                F('view_count') * 0.5 + F('sales') * 0.5,
                output_field=FloatField()
            )
        ).order_by('-popularity')[:10]  # Top 10 by popularity

        # Fetch reviews related to the product
        reviews = Review.objects.filter(product=prods).order_by('-id')

        # Initialize an empty review form
        form = ReviewForm()

        context = {
            'prods': prods,
            'popular_products': popular_products,
            'queryset': queryset,
            'colors': Color.objects.all(),  # Fetch color options
            'sizes': Size.objects.all(),  # Fetch size options
            'form': form,  # Include the review form in the context
            'reviews': reviews,  # Include the reviews in the context
        }
        return render(request, 'product-detail.html', context)

    def post(self, request, id):
        prods = get_object_or_404(Product, id=id)
        form = ReviewForm(request.POST)

        if form.is_valid():
            # Create the review without saving it to associate it with the product
            review = form.save(commit=False)
            review.product = prods  # Associate the review with the current product
            review.save()  # Save the review to the database
            return redirect('product-detail', id=prods.id)  # Redirect back to the product detail page

        # If the form is not valid, re-render the page with the existing form and its errors
        queryset = Product.objects.order_by('-view_count')[:4]
        popular_products = Product.objects.annotate(
            popularity=ExpressionWrapper(
                F('view_count') * 0.5 + F('sales') * 0.5,
                output_field=FloatField()
            )
        ).order_by('-popularity')[:10]

        # Fetch reviews related to the product
        reviews = Review.objects.filter(product=prods).order_by('-id')

        context = {
            'prods': prods,
            'popular_products': popular_products,
            'queryset': queryset,
            'colors': Color.objects.all(),
            'sizes': Size.objects.all(),
            'form': form,  # Include the form with errors to show validation messages
            'reviews': reviews,  # Include the reviews in the context
        }
        return render(request, 'product-detail.html', context)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from store.models import Product, Color, Size, Review
# from django.db.models import F, FloatField, ExpressionWrapper
# from store.forms import ReviewForm  # Import the review form
#
#
# class ProductDetail(View):
#     def get(self, request, id):
#         prods = get_object_or_404(Product, id=id)
#         queryset = Product.objects.order_by('-view_count')[:4]  # Top 4 popular products
#
#         # Define a weighted popularity score
#         popular_products = Product.objects.annotate(
#             popularity=ExpressionWrapper(
#                 F('view_count') * 0.5 + F('sales') * 0.5,
#                 output_field=FloatField()
#             )
#         ).order_by('-popularity')[:10]  # Top 10 by popularity
#
#         # Initialize an empty review form
#         form = ReviewForm()
#
#         context = {
#             'prods': prods,
#             'popular_products': popular_products,
#             'queryset': queryset,
#             'colors': Color.objects.all(),  # Fetch color options
#             'sizes': Size.objects.all(),  # Fetch size options
#             'form': form,  # Include the review form in the context
#         }
#         return render(request, 'product-detail.html', context)
#
#     def post(self, request, id):
#         prods = get_object_or_404(Product, id=id)
#         form = ReviewForm(request.POST)
#
#         if form.is_valid():
#             # Create the review without saving it to associate it with the product
#             review = form.save(commit=False)
#             review.product = prods  # Associate the review with the current product
#             review.save()  # Save the review to the database
#             return redirect('product-detail', id=prods.id)  # Redirect back to the product detail page
#
#         # If the form is not valid, re-render the page with the existing form and its errors
#         queryset = Product.objects.order_by('-view_count')[:4]
#         popular_products = Product.objects.annotate(
#             popularity=ExpressionWrapper(
#                 F('view_count') * 0.5 + F('sales') * 0.5,
#                 output_field=FloatField()
#             )
#         ).order_by('-popularity')[:10]
#
#         context = {
#             'prods': prods,
#             'popular_products': popular_products,
#             'queryset': queryset,
#             'colors': Color.objects.all(),
#             'sizes': Size.objects.all(),
#             'form': form,  # Include the form with errors to show validation messages
#         }
#         return render(request, 'product-detail.html', context)




# from django.shortcuts import render,redirect
# from django.views import View
# from store.models import Product, Color, Size
# from django.db.models import F, FloatField, ExpressionWrapper
#
# class ProductDetail(View):
#     def get(self, request, id):
#         prods = Product.objects.filter(id=id).first()
#         queryset = Product.objects.order_by('-view_count')[:4]  # Top 4 popular products
#         # Define a weighted popularity score
#         popular_products = Product.objects.annotate(
#             popularity=ExpressionWrapper(
#                 F('view_count') * 0.5 + F('sales') * 0.5,
#                 output_field=FloatField()
#             )
#         ).order_by('-popularity')[:10]  # Top 10 by popularity
#
#         context = {
#             'prods': prods,
#             'popular_products':popular_products,
#             'queryset': queryset,
#             'colors': Color.objects.all(),  # Fetch color options
#             'sizes': Size.objects.all(),    # Fetch size options
#         }
#         return render(request, 'product-detail.html', context)

