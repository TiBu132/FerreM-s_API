from django.db import models
from django.db.models import Sum

# Create your models here.

class Producto(models.Model):
    id_producto=models.AutoField(primary_key=True)
    nombre_producto=models.CharField(max_length=50, unique=True)
    valor_producto=models.IntegerField()
    descripcion_producto=models.CharField(max_length=150)
    tipo_producto=models.ForeignKey("Tipo_producto",on_delete=models.CASCADE, default="Sin tipo", to_field="tipo_producto")

    @property
    def cantidad_stock(self):
        return Stock.objects.filter(nombre_producto=self).aggregate(total=Sum('cantidad_stock'))['total'] or 0


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
 
class Usuario(models.Model):
    rut=models.CharField(max_length=50,primary_key=True,unique=True)
    nombre_usuario=models.CharField(max_length=50)
    password_usuario=models.CharField(max_length=24,null=False,blank=False)
    pnombre=models.CharField(max_length=30)
    snombre=models.CharField(max_length=30,blank=True,null=True)
    apaterno=models.CharField(max_length=30)
    amaterno=models.CharField(max_length=30,blank=True,null=True)
    correo=models.CharField(max_length=50)
    tipo_usuario=models.ForeignKey("tipoUsuario", on_delete=models.CASCADE, to_field="tipo_usuario", null=False)

    def __str__(self):
        return f"{self.pnombre} {self.apaterno}"
 
class tipoUsuario(models.Model):
    tipo_usuario=models.CharField(max_length=30, primary_key=True, unique=True)

    def __str__(self):
        return f"{self.tipo_usuario}"
    
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True, unique=True)
    productos=models.CharField(max_length=300)
    valor_total=models.IntegerField(null=False,blank=False)
    orden_compra=models.CharField(max_length=50,null=False,blank=False)
    codigo_auth=models.CharField(max_length=50,null=False,blank=False)
    fecha_transaccion=models.TimeField()
    rut=models.ForeignKey("Usuario",on_delete=models.CASCADE, to_field="rut", default="")

    def __str__(self):
        return f"{self.id_boleta}, {self.rut}, {self.orden_compra}"