from django.db import models

# Create your models here.
class Registrasi(models.Model):
    no_urut = models.CharField(max_length = 10)
    nama = models.CharField(max_length = 255)
    alamat = models.CharField(max_length = 255)
    no_tlp = models.CharField(max_length = 15)