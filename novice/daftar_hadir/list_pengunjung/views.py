from django.shortcuts import render, redirect

# Create your views here.
from .models import Registrasi

def home_screen(req):
    register = Registrasi.objects.all()
    return render(req, 'list_pengunjung/index.html', {
        'data': register,
    })

def tambah(req):
    if req.POST:
        Registrasi.objects.create(
            no_urut = req.POST['no_urut'],
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            no_tlp = req.POST['no_tlp'],
        )
        return redirect('/list_pengunjung')
    return render(req, 'list_pengunjung/tambah.html')


def hapus(req, id):
    dt = Registrasi.objects.get(id=id)
    dt.delete()
    return redirect('/list_pengunjung/')

def edit(req, id):
    data = Registrasi.objects.get(id=id)
    if req.POST:
        Registrasi.objects.filter(pk=id).update(
            nama = req.POST['nama'],
            alamat = req.POST['alamat'],
            no_tlp = req.POST['no_tlp'],
        )
        return redirect('/list_pengunjung')
    return render(req,'list_pengunjung/edit.html', {'data':data})

def profil_s(req):
    return render(req, 'list_pengunjung/profil.html')