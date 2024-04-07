from django.urls import path
from . import views

urlpatterns = [
    path('proveedores', views.lista_proveedores, name='lista_proveedores'),
    path('productos', views.lista_productos, name='lista_productos'),
]