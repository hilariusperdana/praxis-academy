from django.urls import path
from akun import views as account_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', account_views.Register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='akun/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='akun/logout.html'), name='logout'),
]