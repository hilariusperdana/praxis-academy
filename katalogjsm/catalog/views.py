from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .forms import UserForm, UserProfileInfoForm
from .models import *
from .decorators import unauthenticated_user, allowed_users, admin_only

#USERMAN VIEW

def listproduk(req):
    register = Tambahproduk.objects.all()
    return render(req, 'catalog/listproduk.html', {
        'data': register,
    })

def listprodukpnj(req, penjual):
    register = Tambahproduk.objects.filter(penjual__nama_toko=penjual)
    return render(req, 'catalog/listproduk.html', {
        'data': register,
    })

def listprodukcat(req, kategori):
    register = Tambahproduk.objects.filter(kategori__nama_Kategori=kategori)
    return render(req, 'catalog/listproduk.html', {
        'data': register,
    })

def hapus(req, id):
    dt = Tambahproduk.objects.get(id=id)
    dt.delete()
    return redirect('/catalog')

def hapuspnj(req, id):
    dt1 = Tambahpenjual.objects.get(id=id)
    dt1.delete()
    return redirect('/')

def hapuskat(req, id):
    dt2 = Category.objects.get(id=id)
    dt2.delete()
    return redirect('/')
@login_required
# @allowed_users(allowed_roles=['usermanagement'])
@admin_only
def cardproduk(req):
    register = Tambahproduk.objects.all()
    pnj = Tambahpenjual.objects.all()
    Cat = Category.objects.all()
    return render(req, 'catalog/index.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat,
    })
@login_required(login_url='user_login')
@allowed_users(allowed_roles=['usermanagement'])
def listpenjual(req):
    pnj = Tambahpenjual.objects.all()
    return render(req, 'catalog/listpenjual.html', { 
        'data1': pnj,
    })

def about(req):
    return render(req, 'catalog/about.html', { 
    })

def index(request):
    if request.user.is_authenticated:
        dt = UserProfileInfo.objects.filter(user=request.user.id).first()
        data = {
            'bio': dt
        }
        return render(request,'catalog/index.html',data)
    # print(dt.foto_profil)
    return render(request,'catalog/index.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@unauthenticated_user
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'foto_profil' in request.FILES:
                print('found it')
                profile.foto_profil = request.FILES['foto_profil']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'catalog/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'catalog/login.html', {})

#UMKMMAN VIEWS
@login_required
@allowed_users(allowed_roles=['umkmmanagement'])
def cardproduk_umkm(req):
    register = Tambahproduk.objects.all()
    pnj = Tambahpenjual.objects.all()
    Cat = Category.objects.all()
    return render(req, 'umkmman/index.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat,
    })
@login_required(login_url='user_login')
@allowed_users(allowed_roles=['umkmmanagement'])
def listpenjual_umkm(req):
    pnj = Tambahpenjual.objects.all()
    return render(req, 'umkmman/listpenjual.html', { 
        'data1': pnj,
    })

def index_umkm(request):
    if request.user.is_authenticated:
        dt = UserProfileInfo.objects.filter(user=request.user.id).first()
        data = {
            'bio': dt
        }
        return render(request,'umkmman/index.html',data)
    # print(dt.foto_profil)
    return render(request,'umkmman/index.html')

#ENDUSER VIEWS
@unauthenticated_user
def cardproduk_user(req):
    register = Tambahproduk.objects.all()
    pnj = Tambahpenjual.objects.all()
    Cat = Category.objects.all()
    return render(req, 'enduser/index.html', {
        'data': register,
        'data1': pnj,
        'data2': Cat,
    })
@unauthenticated_user
def listpenjual_user(req):
    pnj = Tambahpenjual.objects.all()
    return render(req, 'enduser/listpenjual.html', { 
        'data1': pnj,
    })
@unauthenticated_user
def listproduk_user(req):
    register = Tambahproduk.objects.all()
    return render(req, 'enduser/listproduk.html', {
        'data': register,
    })