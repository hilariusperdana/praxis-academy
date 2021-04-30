from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Category(models.Model):
    nama_Kategori = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama_Kategori


class Tambahproduk(models.Model):
    nama = models.CharField(max_length = 255)
    kategori = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cats', default='')
    deskripsi = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 15)
    # no_tlp = models.CharField(max_length = 15)
    tanggal = models.DateField(auto_now_add=True, null=True)
    foto = models.ImageField(upload_to='produk/', blank=True)
    

    def delete(self, *args, **kwargs):
        self.foto.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.nama


