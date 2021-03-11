from django.urls import path

from . import views
from . import forms
from cobasik import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home_screen),
    # path('tambah',views.tambah),
    # path('profil',views.profil_s),
    path('hapus/<int:id>',views.hapus),
    path('editform/<int:id>',forms.FormRegistrasi.edit),
    path('Form', forms.FormRegistrasi.simpandata),
    path('Upload', forms.FormRegistrasi.upload_file),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
