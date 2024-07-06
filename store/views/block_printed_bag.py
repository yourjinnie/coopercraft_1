from django.views import View
from django.shortcuts import render, redirect


class BlockPrintedBag(View):
    def get(self, request):
        return render(request, 'block-printed-bag.html')