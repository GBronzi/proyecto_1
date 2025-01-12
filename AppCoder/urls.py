from django.urls import path
from .views import index, buscar, acerca, contacto, cargar_estudiante, lista_estudiantes, cargar_profesor, lista_profesores

urlpatterns = [
    path('', index, name='index'),
    path('cargar_estudiante/', cargar_estudiante, name='cargar_estudiante'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('cargar_profesor/', cargar_profesor, name='cargar_profesor'),
    path('profesores/', lista_profesores, name='lista_profesores'),
    path('acerca/', acerca, name='acerca'),
    path('contacto/', contacto, name='contacto'),
    path('buscar/', buscar, name='buscar'),
]


