from django.shortcuts import render

# Create your views here.
from .models import Registrasi

def home_screen(req):
    register = Registrasi.objects.all()
    return render(req, 'list_pengunjung/index.html')

def profil_s(req):
    return render(req, 'list_pengunjung/profil.html')