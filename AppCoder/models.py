from django.db import models

# Modelo Socio (anteriormente Estudiante)
class Socio(models.Model):
    # Opciones de tipos de clase
    tipos_clases = [
        ('musculacion', 'Musculación'),
        ('spinning', 'Spinning'),
        ('yoga', 'Yoga'),
        ('bailoterapia', 'Bailoterapia'),
        ('natacion', 'Natación'),
        ('crossfit', 'Crossfit'),
        ('pase libre', 'Pase libre'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length=20)
    tipo_clase = models.CharField(max_length=20, choices=tipos_clases)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.tipo_clase}"

# Modelo Instructor
class Instructor(models.Model):
    # Opciones de especialidad
    especialidades = [
        ('musculacion', 'Musculación'),
        ('spinning', 'Spinning'),
        ('yoga', 'Yoga'),
        ('bailoterapia', 'Bailoterapia'),
        ('natacion', 'Natación'),
        ('crossfit', 'Crossfit'),
        ('entrenamiento funcional', 'Entrenamiento funcional'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    especialidad = models.CharField(max_length=50, choices=especialidades)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

