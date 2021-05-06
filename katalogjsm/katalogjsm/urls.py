from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from catalog import views
from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

urlpatterns = [
    
    
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR) # baris ini adalah untuk menampilkan foto profil kita