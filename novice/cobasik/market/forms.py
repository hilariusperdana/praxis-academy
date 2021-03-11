from django import forms
from django.forms import ModelForm
from .models import Registrasi
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Registrasi
    
    def simpandata(self):
        form = FormRegistrasi( )
        if self.POST:
            form = FormRegistrasi(self.POST, self.FILES)
            if form.is_valid():
                form.save()
                return redirect('/market')
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
            return redirect('/market')
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
