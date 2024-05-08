from django.urls import path
from rest_ferreteria.views import ProductView
urlpatterns = [
    path('get', ProductView.as_view()),
]
