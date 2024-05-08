from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from core.models import Producto
from .serializers import ProductoSerializer
import requests
from django.shortcuts import render

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        serializer = ProductoSerializer(Producto.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

def home(request):
    # Hacer solicitud GET a tu API de DRF
    response = requests.get('http://127.0.0.1:8000/api')
    # Obtener los datos JSON de la respuesta
    data = response.json()
    # Renderizar tu plantilla HTML con los datos obtenidos
    return render(request, 'home.html', {'data': data})