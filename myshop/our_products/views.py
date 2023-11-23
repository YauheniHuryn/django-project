from .models import Category, Product
from .forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from our_products.models import *
from .models import Cart, ShoppingList
from django.contrib import messages


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "list.html", {"category": category, "categories": categories, "products": products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "detail.html", {"product": product, "cart_product_form": cart_product_form})


@login_required
def add_to_cart(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product=product_id).first()
    product = Product.objects.get(pk=product_id)
    user = request.user
    library_list = ShoppingList.objects.filter(user=user.id)
    if product in library_list:
        messages.success(request, "Item in your library.")
    else:
        Cart.objects.create(user=user, product=product)
        messages.success(request, "Item added to your cart.")

    return redirect("cart_detail")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("cart_detail")


@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price for item in cart_items)
    if request.method == "POST":
        current_user = request.user
        for cart_item in cart_items:
            ShoppingList.objects.create(user=current_user, product=cart_item.product)
            cart_item['update_quantity_form']=CartAddProductForm(initial={
                'quantity': cart_item.quantity,
                'update': True})
        Cart.objects.all().delete()
        return redirect("home_page")

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/detail.html", context)
