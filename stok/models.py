from django.db import models

class Barang(models.Model):
    jenis = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)    
    hpp = models.DecimalField(max_digits=10, decimal_places=2)
    hj = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.IntegerField(default=0)  # Field untuk menyimpan urutan barang
    stok_awal = models.IntegerField(default=0)
    topup = models.IntegerField(default=0)
    toko1 = models.IntegerField(default=0)
    stokawal_toko1 = models.IntegerField(default=0)
    topup_toko1 = models.IntegerField(default=0)
    toko2 = models.IntegerField(default=0)
    stokawal_toko2 = models.IntegerField(default=0)
    topup_toko2 = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['jenis', 'order']
    def __str__(self):
        return self.nama