from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from our_products.models import Category, Product


def home(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, "home.html", {"category": category, "categories" : categories, "items": products, "page_tag": "home"})
