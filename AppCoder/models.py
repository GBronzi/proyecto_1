from django.db import models


class Socio(models.Model):
    
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

class Instructor(models.Model):
    
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

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.DurationField(help_text="Duración de la actividad (ejemplo: 01:30:00)")
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, related_name='actividades')
    horario = models.TimeField(help_text="Hora de inicio de la actividad")
    cupo_maximo = models.IntegerField(help_text="Cantidad máxima de participantes")

    def __str__(self):
        return f"{self.nombre} - {self.instructor.nombre if self.instructor else 'Sin instructor'}"
