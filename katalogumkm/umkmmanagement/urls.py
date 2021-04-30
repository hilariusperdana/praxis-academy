from django.urls import path

from . import views
from . import forms
from katalogumkm import settings
from django.conf.urls.static import static


urlpatterns = [
    path('produk',views.listproduk),
    path('listpenjual',views.listpenjual),
    path('about',views.about),
    path('hapus/<int:id>',views.hapus),
    path('hapuskat/<int:id>',views.hapuskat),
    path('editform/<int:id>',forms.FormTambahproduk.edit),
    path('form', forms.FormTambahproduk.simpandata),   
    path('',views.cardproduk),    
    path('produk/<penjual>',views.listprodukpnj),
    path('kategori', forms.FormCategory.simpandata),
    path('produk/ctr/<kategori>',views.listprodukcat),    
    path('search',views.search, name='search'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
