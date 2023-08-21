from django.shortcuts import render, get_object_or_404
from .models import Products, Category
from django.db.models import Q 

# Create your views here.

def search(request):
    query = request.GET.get('query', '')
    products = Products.objects.filter(status=Products.ACTIVE).filter
    (Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'store/search.html', {'query': query, 'products': products})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Products.ACTIVE)

    return render(request, 'store/category_detail.html', {'category': category, 'products': products})

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Products, slug=slug, status=Products.ACTIVE)
    
    return render(request, 'store/product_detail.html', {'product': product})