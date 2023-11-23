from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from our_products.models import Cart


def order_create(request):
    cart = Cart(request)
    cart_items = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart_items:
                OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=1)

            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                      'orders/order/create.html',
                      {'cart': cart, 'form': form, 'cart_items': cart_items})
