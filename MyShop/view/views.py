from django.shortcuts import render, get_object_or_404
from django.views import View
from product.models import Category, product

class HomeView(View):
    def get(self, request):
        available_products = product.objects.filter(available=True)
        products = product.objects.all()

        categories = Category.objects.filter(is_sub=False)
        subcategories = Category.objects.filter(is_sub=True)

        return render(request, 'view/index.html',
                      {
                                'products': products,
                                'available_products': available_products,
                                'categories': categories,
                                'subcategories': subcategories
        })

