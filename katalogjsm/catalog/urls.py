from django.urls import path

from catalog import views, forms
from katalogjsm import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path

app_name = 'catalog' # jangan lupa edit bagian ini, esuaikan app yang dibuat

urlpatterns = [
#urls usermanagement
    path('home_user',views.cardproduk, name='home_user'),
    path('produk',views.listproduk, name='listproduk'),
    path('detailproduk/<int:id>',views.detailproduk),
    path('listpenjual',views.listpenjual, name='listpenjual'),
    path('about',views.about, name='about'),
    path('hapus/<int:id>',views.hapus),
    path('hapuspnj/<int:id>',views.hapuspnj),
    path('hapuskat/<int:id>',views.hapuskat),
    path('editform/<int:id>',forms.FormTambahproduk.edit),
    path('form', forms.FormTambahproduk.simpandata),
    path('penjual', forms.FormPenjual.simpandata),
    path('produk/<penjual>',views.listprodukpnj, name='product_seller'),
    path('kategori', forms.FormCategory.simpandata),
    path('produk/ctr/<kategori>',views.listprodukcat, name='category_product'),
    path('register/',views.register,name='register'),
    path('catalog/user_login/',views.user_login,name="user_login"),
    path('logout', views.user_logout, name='logout'),
    path('search', views.search, name='search'),

#url umkmmanagement
    path('home_umkm',views.cardproduk_umkm, name='home_umkm'),
    path('listpenjual_umkm',views.listpenjual_umkm, name='listpenjual_umkm'),
    path('produk_umkm',views.listproduk_umkm, name='listproduk_umkm'),
    
#url enduser
    path('',views.cardproduk_user, name='home'),
    path('produk_user',views.listproduk_user, name='listproduk_user'),
    path('listpenjual_user',views.listpenjual_user, name='listpenjual_user'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
