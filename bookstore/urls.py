from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', RedirectView.as_view(url='/api/v1/')),
    re_path('bookstore/(?P<version>(v1|v2))/', include('order.urls')),
    re_path('bookstore/(?P<version>(v1|v2))/', include('product.urls'))
]