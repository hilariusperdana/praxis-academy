from django import forms
from django.forms import ModelForm
from .models import Tambahproduk
from .models import Tambahpenjual
from .models import Category
from django.shortcuts import render, redirect
from .models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# from .decorators import admin_produk

class FormTambahproduk(forms.ModelForm):
    class Meta:
        exclude = []
        model = Tambahproduk
    
    # @login_required
    # @admin_produk
    def simpandata(self):
        form = FormTambahproduk( )
        if self.POST:
            form = FormTambahproduk(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                # group = None
                # if group == 'umkmmanagement':
                #     return redirect('/produk_umkm')
                # elif group == 'usermanagement':
                return redirect ('/produk')
                # else:
                #     return redirect ('home')

		        # if group == 'usermanagement':
                #     return redirect('/produk')
            #(form.errors)
        return render(self, 'catalog/form.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Tambahproduk.objects.filter(id=id).first()
        form=FormTambahproduk(instance=data)
        if self.POST:
            form=FormTambahproduk(self.POST, self.FILES, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/produk')
        return render(self,'catalog/form.html', {'form':form})

class FormPenjual(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Tambahpenjual
    
    def simpandata(self):
        form = FormPenjual( )
        if self.POST:
            form = FormPenjual(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/form')
            #(form.errors)
        return render(self, 'catalog/form.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Tambahpenjual.objects.filter(id=id).first()
        form=FormPenjual(instance=data)
        if self.POST:
            form=FormPenjual(self.POST, self.FILES, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/home_user')
        return render(self,'catalog/form.html', {'form':form})

class FormCategory(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Category
    
    def simpandata(self):
        form = FormCategory( )
        if self.POST:
            form = FormCategory(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home_user')
            #(form.errors)
        return render(self, 'catalog/form.html',{
            'form' : form,
        } )



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
         model = UserProfileInfo
         fields = ('nama','foto_profil')