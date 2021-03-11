from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Registrasi(models.Model):
    nama = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 15)
    deskripsi = models.CharField(max_length = 255)
    no_tlp = models.CharField(max_length = 15)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)
    foto = models.ImageField(upload_to='produk/', blank=True)
    

    def __str__(self):
        return self.nama