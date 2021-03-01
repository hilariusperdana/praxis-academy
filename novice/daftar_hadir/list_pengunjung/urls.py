from django.urls import path

from . import views
from . import forms

urlpatterns = [
    path('',views.home_screen),
    path('tambah',views.tambah),
    path('profil',views.profil_s),
    path('hapus/<int:id>',views.hapus),
    path('edit/<int:id>',views.edit),
    path('Form', forms.FormRegistrasi.simpandata),
]