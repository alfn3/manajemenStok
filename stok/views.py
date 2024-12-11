from django.shortcuts import render, get_object_or_404, redirect
from .models import Barang
from .forms import BarangForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def barang_list(request):
    barangs = Barang.objects.values('id', 'nama', 'jenis', 'hpp', 'hj').order_by('order')  # Urutkan berdasarkan 'order'
    all_jenis = Barang.objects.values_list('jenis', flat=True).distinct()  # Hanya jenis unik

    # Urutkan jenis secara alfabetis (atau sesuai dengan kebutuhan)
    ordered_jenis = sorted(set(all_jenis))

    return render(request, 'stok/barang_list.html', {'barangs': barangs, 'jenis_list': ordered_jenis})

from django.shortcuts import render
from .models import Barang

def gudang_list(request):
    # Ambil hanya kolom yang dibutuhkan, termasuk 'order'
    gudangs = Barang.objects.values(
        'id', 'nama', 'jenis', 'stok_awal', 'topup', 'topup_toko1', 'topup_toko2', 'order'
    ).order_by('order')  # Pastikan data diurutkan berdasarkan 'order'

    # Hitung stok_akhir untuk setiap gudang
    for gudang in gudangs:
        gudang['stok_akhir'] = gudang['topup'] + gudang['topup_toko1'] + gudang['topup_toko2'] - gudang['stok_awal']

    # Ambil semua jenis untuk filtering atau tampilan
    all_jenis = Barang.objects.values_list('jenis', flat=True).distinct()
    ordered_jenis = sorted(set(all_jenis))  # Urutkan jenis secara alfabetis

    return render(request, 'stok/stok.html', {'gudangs': gudangs, 'jenis_list': ordered_jenis})

def barang_detail(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    return render(request, '/stok', {'barang': barang})

def barang_create(request):
    if request.method == "POST":
        form = BarangForm(request.POST)
        if form.is_valid():
            barang = form.save()
            return redirect('/stok', pk=barang.pk)
    else:
        form = BarangForm()
    return render(request, '/stok', {'form': form})

def barang_update(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    if request.method == "POST":
        form = BarangForm(request.POST, instance=barang)
        if form.is_valid():
            barang = form.save()
            return redirect('/stok', pk=barang.pk)
    else:
        form = BarangForm(instance=barang)
    return render(request, '/stok', {'form': form})

def barang_delete(request, pk):
    barang = get_object_or_404(Barang, pk=pk)
    if request.method == "POST":
        barang.delete()
        return redirect('barang_list')
    return render(request, 'stok/', {'barang': barang})

def update_order(request):
            try:
                data = json.loads(request.body)  # Parsing data JSON yang dikirimkan
                order = data.get('order', [])  # Mengambil urutan baru

                for index, item in enumerate(order):
                    if item['id']:  # Pastikan id tidak kosong
                        barang = Barang.objects.get(pk=item['id'])
                        barang.order = item['order']  # Update urutan barang
                        barang.save()
                    else:
                        return JsonResponse({'status': 'error', 'message': 'ID is missing for item at index ' + str(index)})

                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def update_barang(request, id):
    if request.method == 'POST':
        data = json.loads(request.body)
        field = data.get('field')
        value = data.get('value')
        stok_akhir = data.get('stok_akhir')

        # Update the record with the new values
        try:
            barang = Barang.objects.get(id=id)
            setattr(barang, field, value)
            barang.stok_akhir = stok_akhir
            barang.save()

            return JsonResponse({'success': True})
        except Barang.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Barang not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
