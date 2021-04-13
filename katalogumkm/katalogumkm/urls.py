from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render
from django.conf.urls.static import static

def index(req):
    return render(req, 'index.html')

urlpatterns = [
    # path('', index),
    # path('market/', include('market.urls')),
    path('', include('produk.urls')),
    path('admin/', admin.site.urls),
]