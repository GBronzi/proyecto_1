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
    DURACIONES = [
        ('00:30:00', '30 minutos'),
        ('01:00:00', '1 hora'),
        ('01:30:00', '1 hora y 30 minutos'),
        ('02:00:00', '2 horas'),
    ]
    
    HORARIOS = [
        ('06:00:00', '06:00 AM'),
        ('07:00:00', '07:00 AM'),
        ('08:00:00', '08:00 AM'),
        ('09:00:00', '09:00 AM'),
        ('10:00:00', '10:00 AM'),
        ('11:00:00', '11:00 AM'),
        ('12:00:00', '12:00 PM'),
        ('13:00:00', '01:00 PM'),
        ('14:00:00', '02:00 PM'),
        ('15:00:00', '03:00 PM'),
        ('16:00:00', '04:00 PM'),
        ('17:00:00', '05:00 PM'),
        ('18:00:00', '06:00 PM'),
        ('19:00:00', '07:00 PM'),
        ('20:00:00', '08:00 PM'),
    ]
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    duracion = models.CharField(max_length=8, choices=DURACIONES, default='01:00:00')
    especialidad = models.CharField(max_length=50, choices=Instructor.especialidades)
    horario = models.CharField(max_length=8, choices=HORARIOS, default='06:00:00')
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='actividades')

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"
