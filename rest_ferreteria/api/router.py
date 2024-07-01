from django.urls import path
from rest_ferreteria.views import ProductView, StockView, TipoProductoView
urlpatterns = [
    path('producto/', ProductView.as_view()),
    path('producto/<int:id_producto>', ProductView.as_view()),
    path('producto/<int:id_producto>/eliminar', ProductView.as_view()),
    path('producto/agregar', ProductView.as_view()),
    path('producto/<int:id_producto>/actualizar', ProductView.as_view()),
    path('stock/', StockView.as_view()),
    path('stock/<str:nombre_producto>', StockView.as_view()),
    path('stock/agregar', StockView.as_view()),
    path('stock/<str:nombre_producto>/actualizar', StockView.as_view()),
    path('tipo_producto/', TipoProductoView.as_view()),
    path('tipo_producto/agregar', TipoProductoView.as_view()),
]
