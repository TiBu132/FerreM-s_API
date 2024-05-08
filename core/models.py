from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto=models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=50, unique=True)
    valor_producto=models.IntegerField()
    descripcion_producto=models.CharField(max_length=120)
    tipo_producto=models.ForeignKey("Tipo_producto",on_delete=models.CASCADE, default="Sin tipo", to_field="tipo_producto")
    
    def __str__(self):
        return self.nombre_producto
    
class Tipo_Producto(models.Model):
    id_tipoProducto=models.AutoField(primary_key=True)
    tipo_producto=models.CharField(max_length=40, default="Sin tipo", unique=True)
    
    def __str__(self):
        return self.tipo_producto
    
class Stock(models.Model):
    cantidad_stock=models.IntegerField(default=0)
    nombre_producto=models.ForeignKey("Producto",on_delete=models.CASCADE,to_field="nombre_producto",default="Sin Producto")

    def __str__(self):
        return f"{self.nombre_producto} = {self.cantidad_stock}"