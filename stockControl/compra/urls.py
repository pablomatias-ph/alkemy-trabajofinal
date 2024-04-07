from django.urls import path
from . import views

urlpatterns = [
    path('proveedores', views.lista_proveedores, name='lista_proveedores'),
    path('productos', views.lista_productos, name='lista_productos'),
    path('agregar_proveedor', views.agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('editar_proveedor/<int:proveedor_id>', views.editar_proveedor, name='editar_proveedor'),
    path('editar_producto/<int:producto_id>', views.editar_producto, name='editar_producto'),
]