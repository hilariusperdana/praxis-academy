from django.db import models

# Create your models here.
class RegBrg(models.Model):
    nama = models.CharField(max_length = 255)
    Deskripsi = models.CharField(max_length = 255)
    harga = models.CharField(max_length = 15)
    no_tlp = models.CharField(max_length = 15)