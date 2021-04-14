from django.urls import path

from . import views
from . import forms
from katalogumkm import settings
from django.conf.urls.static import static


urlpatterns = [
    path('produk',views.listproduk),
    # path('tambah',views.tambah),
    # path('profil',views.profil_s),
    path('hapus/<int:id>',views.hapus),
    path('hapuspnj/<int:id>',views.hapuspnj),
    path('hapuskat/<int:id>',views.hapuskat),
    path('editform/<int:id>',forms.FormTambahproduk.edit),
    path('form', forms.FormTambahproduk.simpandata),
    # path('Upload', forms.FormRegistrasi.upload_file),
    path('',views.cardproduk),
    path('penjual', forms.FormPenjual.simpandata),
    path('produk/<penjual>',views.listprodukpnj),
    path('kategori', forms.FormCategory.simpandata),
    path('produk/ctr/<kategori>',views.listprodukcat),
    # path('produk/ctr/Jasa',viewsCategory.listCategory),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
