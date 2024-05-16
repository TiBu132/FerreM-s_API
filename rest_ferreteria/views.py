from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework import status
from django.http import JsonResponse
from core.models import Producto, Stock, Tipo_Producto
from .serializers import ProductoSerializer, StockSerializer, TipoProductoSerializer
import requests
from django.shortcuts import render

# Create your views here.
class ProductView(APIView):
    def get(self, request, id_producto=None):
        if id_producto is not None:
            print("ID de producto recibido:", id_producto)
            producto = Producto.objects.filter(id_producto=id_producto)
        else:
            producto = Producto.objects.all()

        serializer = ProductoSerializer(producto, many=True)
        
        for data in serializer.data:
            stock_producto = Producto.objects.get(id_producto=data['id_producto'])
            data['cantidad_stock'] = stock_producto.cantidad_stock
        
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Producto.objects.create(
                nombre_producto=data['nombre_producto'],
                valor_producto=data['valor_producto'],
                descripcion_producto=data['descripcion_producto'],
                tipo_producto_id=data['tipo_producto'],
            )
            
            return JsonResponse({"mensaje":"El Producto se ha registrado exitosamente"}, status=200) 
        except Exception as e:
            
            print(f'Error en la vista: {repr(e)}',)
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, id_producto):
        try:
            producto = Producto.objects.get(id_producto=id_producto)
            serializer = ProductoSerializer(instance=producto, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "El Producto se ha actualizado exitosamente"}, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Producto.DoesNotExist:
            return Response({"error": "El producto no existe"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def delete(self, request, id_producto):
        try:
            producto = Producto.objects.get(id_producto=id_producto)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class StockView(APIView):
    def get(self, request):
        serializer = StockSerializer(Stock.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        try:
            data= JSONParser().parse(request)
            Stock.objects.create(
                cantidad_stock=data['cantidad_stock'],
                nombre_producto_id=data['nombre_producto'],
            )

            return JsonResponse({"mensaje":"El Stock se ha registrado exitosamente"}, status=200)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}',)
            return JsonResponse({'error': str(e)}, status=500)
    
    def put(self, request, nombre_producto):
        try:
            producto = Producto.objects.get(nombre_producto=nombre_producto)
            stock = Stock.objects.get(nombre_producto=producto)
            serializer = StockSerializer(instance=stock, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "El Stock se ha actualizado exitosamente"}, status=200)
            else:
                return Response(serializer.errors, status=400)
        except Producto.DoesNotExist:
            return Response({"error": "El producto no existe"}, status=404)
        except Stock.DoesNotExist:
            return Response({"error": "El stock para este producto no existe"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class TipoProductoView(APIView):
    def get(self,request):
        serializer = TipoProductoSerializer(Tipo_Producto.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Tipo_Producto.objects.create(
                tipo_producto=data["tipo_producto"],
            )

            return JsonResponse({"mensaje":"El tipo de producto se ha registrado exitosamente"}, status=200)
        
        except Exception as e:
            print(f'Error en la vista: {repr(e)}',)
            return JsonResponse({'error': str(e)}, status=500)