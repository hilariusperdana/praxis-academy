from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from akun import views
from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

urlpatterns = [
    # path('', index),
    # path('market/', include('market.urls')),
    path('', include('produk.urls')),
    path('admin/', admin.site.urls),
    path('', include('akun.urls')),
    url(r'^akun/',include('akun.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^special/',views.special,name='special'),
    url(r'^login/',views.user_login,name='user_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR) # baris ini adalah untuk menampilkan foto profil kita