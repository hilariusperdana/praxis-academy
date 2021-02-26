from django import forms
from django.forms import ModelForm
from .models import Registrasi, Suplier, Customer, Transaksi

# untuk form Barang

class FormRegistrasi(forms.ModelForm):
    class Meta:
        exclude = [ ]
        model = Registrasi