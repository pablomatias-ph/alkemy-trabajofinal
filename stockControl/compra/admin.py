from django.contrib import admin
from .models import Proveedor, Producto

class ProveedorAdministrador(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni"]
    search_fields = ["nombre", "apellido"]

class ProductoAdministrador(admin.ModelAdmin):
    list_display = ["nombre", "precio", "stock_actual", "proveedor"]
    search_fields = ["nombre", "proveedor__nombre"]
    
admin.site.register(Proveedor, ProveedorAdministrador)
admin.site.register(Producto, ProductoAdministrador)