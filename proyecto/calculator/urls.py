# calculator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.metodos, name='metodos'),
    path('base/', views.base, name='base'),  
  
    # Agrega aquí otras rutas según sea necesario
]
