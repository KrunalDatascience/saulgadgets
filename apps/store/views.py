from itertools import product
from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from .models import Product, Category
# Create your views here.

def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug = product_slug)
    context = {
        'product': product
    }
    return render(request, 'product-details.html', context)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category-details.html', context)