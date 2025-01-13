from django.db import models

# Create your models here.
class  Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido:  {self.apellido}"
    
class  Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    curso = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"