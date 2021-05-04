# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from . import models
from .models import Tambahproduk
from .models import Tambahpenjual
from .models import Category

def listproduk(req):
    register = Tambahproduk.objects.all()
    return render(req, 'katalog/listproduk.html', {
        'data': register,
    })

def listprodukpnj(req, penjual):
    register = Tambahproduk.objects.filter(penjual__nama_toko=penjual)
    return render(req, 'katalog/listproduk.html', {
        'data': register,
    })

def listprodukcat(req, kategori):
    register = Tambahproduk.objects.filter(kategori__nama_Kategori=kategori)
    return render(req, 'katalog/listproduk.html', {
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
    
    group = req.user.groups.first()
    if group is not None and group.name == 'usermanagement':
        register = Tambahproduk.objects.all()
        pnj = Tambahpenjual.objects.all()
        Cat = Category.objects.all()
    return render(req, 'katalog/index.html',{
        'data': register,
        'data1': pnj,
        'data2': Cat,
    })

# def cardproduk(req):
#     register = Tambahproduk.objects.all()
#     pnj = Tambahpenjual.objects.all()
#     Cat = Category.objects.all()
#     return render(req, 'katalog/index.html', {
#         'data': register,
#         'data1': pnj,
#         'data2': Cat,
#     })

def listpenjual(req):
    pnj = Tambahpenjual.objects.all()
    return render(req, 'katalog/listpenjual.html', { 
        'data1': pnj,
    })

def about(req):
    return render(req, 'katalog/about.html', { 
    })

def search(req):
    if req.method == "POST":
        searched = req.POST['searched']
        tambahproduks = Tambahproduk.objects.filter(nama__contains=searched)
        return render(req, 'search.html', {
        'tambahproduks':tambahproduks ,   
        'searched':searched })
    else:
        return render(req, 'search.html', {
          
    })
