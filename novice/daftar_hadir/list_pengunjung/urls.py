from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_screen),
    path('tambah',views.tambah),
    path('profil',views.profil_s),
    path('hapus/<int:id>',views.hapus),

]