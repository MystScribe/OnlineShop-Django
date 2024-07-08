from django.shortcuts import render, get_object_or_404, redirect
from .models import product
from django.views.generic import DetailView


class ProductDetailView(DetailView):
    def get(self, request, slug):
        products = get_object_or_404(product, slug=slug)
        return render(request, 'product/detail.html', {'product': products})

    def post(self, request, slug):
        products = get_object_or_404(product, slug=slug)
        return render(request, 'product/detail.html', {'product': products})
