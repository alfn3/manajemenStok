# Generated by Django 5.0.2 on 2024-11-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0008_stok'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stok',
        ),
        migrations.AddField(
            model_name='barang',
            name='stok_awal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='stokawal_toko1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='stokawal_toko2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='toko1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='toko2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='topup',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='topup_toko1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='barang',
            name='topup_toko2',
            field=models.IntegerField(default=0),
        ),
    ]
