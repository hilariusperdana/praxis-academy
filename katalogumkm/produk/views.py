# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from .models import Tambahproduk
from .models import Tambahpenjual
from .models import Category

def listproduk(req):
    register = Tambahproduk.objects.all()
    return render(req, 'produk/index.html', {
        'data': register,
    })

def listprodukpnj(req, penjual):
    register = Tambahproduk.objects.filter(penjual__nama_toko=penjual)
    return render(req, 'produk/index.html', {
        'data': register,
    })

def listprodukcat(req, kategori):
    register = Tambahproduk.objects.filter(kategori__nama_Kategori=kategori)
    return render(req, 'produk/index.html', {
        'data': register,
    })

def hapus(req, id):
    dt = Tambahproduk.objects.get(id=id)
    dt.delete()
    return redirect('/produk')

def hapuspnj(req, id):
    dt1 = Tambahpenjual.objects.get(id=id)
    dt1.delete()
    return redirect('/')

def hapuskat(req, id):
    dt2 = Category.objects.get(id=id)
    dt2.delete()
    return redirect('/')

def cardproduk(req):
    register = Tambahproduk.objects.all()
    pnj = Tambahpenjual.objects.all()
    Cat = Category.objects.all()
    return render(req, 'produk/index.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat
    })

