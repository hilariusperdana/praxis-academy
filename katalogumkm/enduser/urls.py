from django.urls import path

from . import views
from katalogumkm import settings
from django.conf.urls.static import static


urlpatterns = [
    path('produk',views.listproduk),
    path('listpenjual',views.listpenjual),
    path('about',views.about),  
    path('',views.cardproduk),    
    path('produk/<penjual>',views.listprodukpnj),
    path('produk/ctr/<kategori>',views.listprodukcat),    
    path('search',views.search, name='search'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
