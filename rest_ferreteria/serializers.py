from rest_framework import serializers
from core.models import Producto, Stock, Tipo_Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        safe = False

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields= '__all__'
        safe=False

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Producto
        fields='__all__'
        safe=False