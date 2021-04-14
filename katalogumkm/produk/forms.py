from django import forms
from django.forms import ModelForm
from .models import Tambahproduk
from .models import Tambahpenjual
from .models import Category
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

class FormTambahproduk(forms.ModelForm):
    class Meta:
        exclude = []
        model = Tambahproduk
    
    def simpandata(self):
        form = FormTambahproduk( )
        if self.POST:
            form = FormTambahproduk(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/produk')
            #(form.errors)
        return render(self, 'produk/form.html',{
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
        return render(self,'produk/form.html', {'form':form})

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
                return redirect('/Form')
            #(form.errors)
        return render(self, 'produk/form.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Tambahpenjual.objects.filter(id=id).first()
        form=FormPenjual(instance=data)
        if self.POST:
            form=FormPenjual(self.POST, self.FILES, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/')
        return render(self,'produk/form.html', {'form':form})

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
                return redirect('/')
            #(form.errors)
        return render(self, 'produk/form.html',{
            'form' : form,
        } )