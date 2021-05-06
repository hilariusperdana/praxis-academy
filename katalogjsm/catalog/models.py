from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tambahpenjual(models.Model):
    nama_toko = models.CharField(max_length = 255)
    keterangan = models.CharField(max_length = 255)
    no_hp = models.CharField(max_length = 15)
    foto_toko = models.ImageField(upload_to='toko/', blank=True)

    def delete(self, *args, **kwargs):
        self.foto_toko.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nama_toko

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
    penjual = models.ForeignKey(Tambahpenjual, on_delete=models.CASCADE, related_name='info', default='')  

    def delete(self, *args, **kwargs):
        self.foto.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.nama



# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)
    foto_profil = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username