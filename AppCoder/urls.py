from django.urls import path
from .views import index, buscar, acerca, contacto, cargar_socio, lista_socios, cargar_instructor, lista_instructores

urlpatterns = [
    path('', index, name='index'),
    path('cargar_socio/', cargar_socio, name='cargar_socio'),
    path('socios/', lista_socios, name='lista_socios'),
    path('cargar_instructor/', cargar_instructor, name='cargar_instructor'),
    path('instructores/', lista_instructores, name='lista_instructores'),
    path('acerca/', acerca, name='acerca'),
    path('contacto/', contacto, name='contacto'),
    path('buscar/', buscar, name='buscar'),
]
