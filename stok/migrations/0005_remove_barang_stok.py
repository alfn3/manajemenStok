# Generated by Django 5.0.2 on 2024-11-27 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0004_barang_jenis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='stok',
        ),
    ]