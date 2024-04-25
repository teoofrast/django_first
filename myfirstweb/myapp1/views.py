from django.shortcuts import render

from myapp1.models import Product


def index_page(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', {"data": all_products})
