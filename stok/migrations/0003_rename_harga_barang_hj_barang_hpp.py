# Generated by Django 5.0.2 on 2024-11-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0002_remove_barang_deskripsi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barang',
            old_name='harga',
            new_name='hj',
        ),
        migrations.AddField(
            model_name='barang',
            name='hpp',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]