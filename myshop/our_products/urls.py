from django.urls import path, re_path
from . import views
from .views import *

app_name = "our_products"

urlpatterns = [
    path("", product_list, name="product_list"),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", cart_detail, name="cart_detail"),
    re_path(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail')
]
