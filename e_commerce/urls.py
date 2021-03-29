from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .views import ProductListViewHomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListViewHomePage.as_view(), name='home'),

    path('products/', include("product.urls", namespace="products")),
    path('auth/', include("user.urls", namespace="user")),
    path('search/', include("search.urls", namespace="search")),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)