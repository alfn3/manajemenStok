# Generated by Django 5.0.2 on 2024-11-28 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0007_alter_barang_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=255)),
                ('stok_awal', models.IntegerField(default=0)),
                ('topup', models.IntegerField(default=0)),
                ('toko1', models.IntegerField(default=0)),
                ('toko2', models.IntegerField(default=0)),
            ],
        ),
    ]
