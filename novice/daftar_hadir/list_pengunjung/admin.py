from django.contrib import admin

# Register your models here.
from .models import Registrasi

class RegistrasiForAdmin (admin.ModelAdmin):
    list_display = ['nama', 'no_tlp']

admin.site.register(Registrasi, RegistrasiForAdmin)
