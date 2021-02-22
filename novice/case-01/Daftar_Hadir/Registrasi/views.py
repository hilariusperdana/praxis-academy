from django.shortcuts import render

# Create your views here.
from .models import Registrasi

def home_screen(req):
    register = Registrasi.object.all()
    return render(req, 'Registrasi/index.html')

def profil_s(req):
    return render(req, 'Registrasi/profil.html')