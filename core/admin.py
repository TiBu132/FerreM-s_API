from django.contrib import admin
from core.models import Producto, Tipo_Producto, Stock, Usuario, tipoUsuario, Boleta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipo_Producto)
admin.site.register(Stock)
admin.site.register(tipoUsuario)
admin.site.register(Usuario)
admin.site.register(Boleta)