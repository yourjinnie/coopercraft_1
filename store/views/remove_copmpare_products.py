from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

class ClearComparisonView(View):
    def get(self, request):
        request.session['comparison_list'] = []
        request.session['comparison_type'] = None
        return redirect('compare_products')