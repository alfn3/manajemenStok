from django.urls import path
from . import views

urlpatterns = [
    path('update-order/', views.update_order, name='update_order'),
    path('', views.barang_list, name='barang_list'),
    path('stokpage/', views.gudang_list, name='gudang_list'),
    path('barang/new/', views.barang_create, name='barang_create'),
    path('barang/<int:id>/update/', views.update_barang, name='update_barang'),
    path('barang/<int:pk>/edit/', views.barang_update, name='barang_update'),
    path('barang/<int:pk>/delete/', views.barang_delete, name='barang_delete'),
]
