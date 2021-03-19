from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Registrasi)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'deskripsi', 'harga')