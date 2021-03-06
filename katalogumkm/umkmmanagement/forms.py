from django import forms
from django.forms import ModelForm
from .models import Tambahproduk
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
        return render(self, 'katalog/form.html',{
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
        return render(self,'katalog/form.html', {'form':form})


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
        return render(self, 'katalog/form.html',{
            'form' : form,
        } )