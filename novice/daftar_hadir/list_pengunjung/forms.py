from django import forms
from django.forms import ModelForm
from .models import Registrasi
from django.shortcuts import render, redirect

class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Registrasi
    
    def simpandata(self):
        form = FormRegistrasi( )
        if self.POST:
            form = FormRegistrasi(self.POST)
            if form.is_valid():
                form.save()
                return redirect('/list_pengunjung')
            #(form.errors)
        return render(self, 'list_pengunjung/saveform.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = Registrasi.objects.filter(id=id).first()
        form=FormRegistrasi(instance=data)
        if self.POST:
            form=FormRegistrasi(self.POST, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/list_pengunjung')
        return render(self,'list_pengunjung/saveform.html', {'form':form})