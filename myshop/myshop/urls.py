from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("about_us.urls")),
    path("contact/", include("contact.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("account/registration", include("account.urls")),
    path("products", include("our_products.urls", namespace="our_products")),
    path('cart/', include('cart.urls', namespace='cart')),
    path("", include("home.urls")),


    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

