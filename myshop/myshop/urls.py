from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from our_products.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("about_us.urls")),
    path("contact/", include("contact.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("account/registration", include("account.urls")),
    path("products/", product_list, name="product_list"),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", cart_detail, name="cart_detail"),
    path('products/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('products/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('orders/', include('orders.urls', namespace='orders')),
    path("", include("home.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
