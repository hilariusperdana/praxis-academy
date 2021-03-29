from django import forms
from django.forms import ModelForm
from .models import Registrasi
from .models import Daftarpenjual
from .models import Category
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ 'penjual' ]
        model = Registrasi
    
    def simpandata(self):
        form = FormRegistrasi( )
        if self.POST:
            form = FormRegistrasi(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/produk')
            #(form.errors)
        return render(self, 'market/saveform.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Registrasi.objects.filter(id=id).first()
        form=FormRegistrasi(instance=data)
        if self.POST:
            form=FormRegistrasi(self.POST, self.FILES, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/produk')
        return render(self,'market/saveform.html', {'form':form})
    
    # def upload_file(self):
    #     if self.method == 'POST':
    #         form = ModelForm(self.POST, self.FILES)
    #         if form.is_valid():
    #             # file is saved
    #             form.save()
    #             return HttpResponseRedirect('/success/url/')
    #     else:
    #         form = ModelForm()
    #     return render(self, 'upload.html', {'form': form})


class FormPenjual(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Daftarpenjual
    
    def simpandata(self):
        form = FormPenjual( )
        if self.POST:
            form = FormPenjual(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/Form')
            #(form.errors)
        return render(self, 'market/formpenjual.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Daftarpenjual.objects.filter(id=id).first()
        form=FormPenjual(instance=data)
        if self.POST:
            form=FormPenjual(self.POST, self.FILES, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/')
        return render(self,'market/formpenjual.html', {'form':form})

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
        return render(self, 'market/formkategori.html',{
            'form' : form,
        } )