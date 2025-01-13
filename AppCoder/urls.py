from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cargar_socio/', views.cargar_socio, name='cargar_socio'),
    path('socios/', views.lista_socios, name='lista_socios'),
    path('cargar_instructor/', views.cargar_instructor, name='cargar_instructor'),
    path('instructores/', views.lista_instructores, name='lista_instructores'),
    path('cargar_actividad/', views.cargar_actividad, name='cargar_actividad'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('editar_actividad/<int:pk>/', views.editar_actividad, name='editar_actividad'),
    path('eliminar_actividad/<int:pk>/', views.eliminar_actividad, name='eliminar_actividad'),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('buscar/', views.buscar, name='buscar'),
]
