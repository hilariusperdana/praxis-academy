from django.db import models

# Create your models here.
class Daftarpenjual(models.Model):
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


class Registrasi(models.Model):
    nama = models.CharField(max_length = 255)
    kategori = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cats', default='')
    # kategori = models.CharField(
    #     max_length=40, choices=[
    #     (None, "Pilih Kategori"),    
    #     ('Bahan Baku', "Bahan Baku"),
    #     ('Jasa', "Jasa"),
    #     ('Kuliner', "Kuliner"),
    #     ('Kerajinan', "Kerajinan"),
    # ], default='')
    deskripsi = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 15)
    # no_tlp = models.CharField(max_length = 15)
    tanggal = models.DateField(auto_now_add=True, null=True)
    foto = models.ImageField(upload_to='produk/', blank=True)
    penjual = models.ForeignKey(Daftarpenjual, on_delete=models.CASCADE, related_name='info', default='')
    # penjual = models.CharField(
    #     max_length=40, choices=[
    #     (None, "nama penjual"),    
    #     ('a', "a"),
    #     ('b', "b"),
    #     ('c', "c"),
    # ], default='')

    def delete(self, *args, **kwargs):
        self.foto.delete()
        super().delete(*args, **kwargs)
    
    def __str__(self):
        return self.nama


