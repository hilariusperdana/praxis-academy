from django import forms
from django.forms import ModelForm
from .models import RegBrg
from django.shortcuts import render, redirect

class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = RegBrg
    
    def simpandata(self):
        form = FormRegistrasi( )
        if self.POST:
            form = FormRegistrasi(self.POST)
            if form.is_valid():
                form.save()
                return redirect('/market')
            #(form.errors)
        return render(self, 'market/saveform.html',{
            'form' : form,
        } )
    
    def edit(self,id):
        data = RegBrg.objects.filter(id=id).first()
        form=FormRegistrasi(instance=data)
        if self.POST:
            form=FormRegistrasi(self.POST, instance=data)
            if form.is_valid():
                form.save()
            return redirect('/market')
        return render(self,'market/saveform.html', {'form':form})

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

