from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from .models import Registrasi
from .models import Daftarpenjual
from .models import Category

def listproduk(req):
    register = Registrasi.objects.all()
    return render(req, 'market/index.html', {
        'data': register,
    })

# def listpenjual(req):
#     pnj = Daftarpenjual.objects.all()
#     return render(req, 'market/card.html', {
#         'data1': pnj,
#     })

def listprodukpnj(req, penjual):
    register = Registrasi.objects.filter(penjual__nama_toko=penjual)
    return render(req, 'market/index.html', {
        'data': register,
    })

def listprodukcat(req, kategori):
    register = Registrasi.objects.filter(kategori__nama_Kategori=kategori)
    
    return render(req, 'market/index.html', {
        'data': register,
    })
# def tambah(req):
#     if req.POST:
#         Registrasi.objects.create(
#             no_urut = req.POST['no_urut'],
#             nama = req.POST['nama'],
#             alamat = req.POST['alamat'],
#             no_tlp = req.POST['no_tlp'],
#         )
#         return redirect('/market')
#     return render(req, 'market/tambah.html')


def hapus(req, id):
    dt = Registrasi.objects.get(id=id)
    dt.delete()
    return redirect('/produk')

def hapuspnj(req, id):
    dt1 = Daftarpenjual.objects.get(id=id)
    dt1.delete()
    return redirect('/')

def hapuskat(req, id):
    dt2 = Category.objects.get(id=id)
    dt2.delete()
    return redirect('/')



# def edit(req, id):
#     data = Registrasi.objects.get(id=id)
#     if req.POST:
#         Registrasi.objects.filter(pk=id).update(
#             nama = req.POST['nama'],
#             alamat = req.POST['alamat'],
#             no_tlp = req.POST['no_tlp'],
#         )
#         return redirect('/market')
#     return render(req,'market/edit.html', {'data':data})

# def profil_s(req):
#     return render(req, 'market/profil.html')

def cardproduk(req):
    register = Registrasi.objects.all()
    pnj = Daftarpenjual.objects.all()
    Cat = Category.objects.all()
    return render(req, 'market/card.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat
    })

