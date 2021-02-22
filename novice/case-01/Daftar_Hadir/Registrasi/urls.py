from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_screen),
    path('profil',views.profil_s),
]