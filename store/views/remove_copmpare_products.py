from django.shortcuts import redirect
from django.views import View

class ClearComparisonView(View):
    def post(self, request):
        # Get product_id from the form and ensure it is a string
        product_id = str(request.POST.get('product_id'))

        # Retrieve the comparison list from the session
        comparison_list = request.session.get('comparison_list', [])

        # Debugging: Check current comparison list
        print("Current comparison list before removal:", comparison_list)
        print("Product ID to remove:", product_id)
        print("Type of product ID to remove:", type(product_id))

        # Ensure all IDs in comparison_list are strings
        comparison_list = [str(item) for item in comparison_list]

        # Remove product_id from the comparison list if it exists
        if product_id in comparison_list:
            comparison_list.remove(product_id)
            request.session['comparison_list'] = comparison_list
            # Save the session explicitly
            request.session.modified = True

        # Debugging: Check updated comparison list
        print("Updated comparison list after removal:", comparison_list)

        # Redirect to the comparison page
        return redirect('compare_products')


