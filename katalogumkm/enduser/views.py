
from django.shortcuts import render, redirect

# Create your views here.
from .models import Tambahproduk
from .models import Tambahpenjual
from .models import Category

def listproduk(req):
    register = Tambahproduk.objects.all()
    return render(req, 'enduser/listproduk.html', {
        'data': register,
    })

def listprodukpnj(req, penjual):
    register = Tambahproduk.objects.filter(penjual__nama_toko=penjual)
    return render(req, 'enduser/listproduk.html', {
        'data': register,
    })

def listprodukcat(req, kategori):
    register = Tambahproduk.objects.filter(kategori__nama_Kategori=kategori)
    return render(req, 'enduser/listproduk.html', {
        'data': register,
    })


def cardproduk(req):
    register = Tambahproduk.objects.all()
    pnj = Tambahpenjual.objects.all()
    Cat = Category.objects.all()
    group = req.user.groups.first()
    if group is None :
        register = Tambahproduk.objects.all()
        pnj = Tambahpenjual.objects.all()
        Cat = Category.objects.all()
    return render(req, 'enduser/index.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat,
    })
    # if group is not None and group.name == 'usermanagement':
    #     register = Tambahproduk.objects.all()
    #     pnj = Tambahpenjual.objects.all()
    #     Cat = Category.objects.all()
    # return render(req, 'katalog/index.html',{
    #     'data': register,
    #     'data1': pnj,
    #     'data2': Cat,
    # })
    # if group is not None and group.name == 'umkmmanagement':
    #     register = Tambahproduk.objects.all()
    #     pnj = Tambahpenjual.objects.all()
    #     Cat = Category.objects.all()
    # return render(req, 'umkmmanagement/index.html',{
    #     'data': register,
    #     'data1': pnj,
    #     'data2': Cat,
    # })

def listpenjual(req):
    pnj = Tambahpenjual.objects.all()
    return render(req, 'katalog/listpenjual.html', { 
        'data1': pnj,
    })

def about(req):
    return render(req, 'enduser/about.html', { 
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
