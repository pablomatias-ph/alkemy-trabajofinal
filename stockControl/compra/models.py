from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre / Razon Social")
    apellido = models.CharField(max_length=100, blank = True, null = True)
    dni = models.CharField(max_length=11, verbose_name="DNI / CUIT")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.nombre