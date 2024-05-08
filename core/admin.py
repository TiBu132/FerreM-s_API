from django.contrib import admin
from core.models import Producto, Tipo_Producto, Stock
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipo_Producto)
admin.site.register(Stock)