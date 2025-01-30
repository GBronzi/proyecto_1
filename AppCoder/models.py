from django.db import models

# Modelo para los Socios del gimnasio
class Socio(models.Model):
    
    # Opciones de tipos de clases que pueden elegir los socios
    tipos_clases = [
        ('musculacion', 'Musculación'),
        ('spinning', 'Spinning'),
        ('yoga', 'Yoga'),
        ('bailoterapia', 'Bailoterapia'),
        ('natacion', 'Natación'),
        ('crossfit', 'Crossfit'),
        ('pase libre', 'Pase libre'),
    ]
    
    # Campos del modelo Socio
    nombre = models.CharField(max_length=100)  # Nombre del socio
    apellido = models.CharField(max_length=100)  # Apellido del socio
    email = models.EmailField()  # Correo electrónico único
    edad = models.PositiveIntegerField()  # Edad del socio
    telefono = models.CharField(max_length=20)  # Número de teléfono del socio
    tipo_clase = models.CharField(max_length=20, choices=tipos_clases)  # Clase elegida por el socio

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.tipo_clase}"  


# Modelo para los Instructores del gimnasio
class Instructor(models.Model):
    
    # Opciones de especialidades para los instructores
    especialidades = [
        ('musculacion', 'Musculación'),
        ('spinning', 'Spinning'),
        ('yoga', 'Yoga'),
        ('bailoterapia', 'Bailoterapia'),
        ('natacion', 'Natación'),
        ('crossfit', 'Crossfit'),
        ('entrenamiento funcional', 'Entrenamiento funcional'),
    ]
    
    # Campos del modelo Instructor
    nombre = models.CharField(max_length=100)  # Nombre del instructor
    apellido = models.CharField(max_length=100)  # Apellido del instructor
    email = models.EmailField()  # Correo electrónico único del instructor
    especialidad = models.CharField(max_length=50, choices=especialidades)  # Especialidad del instructor

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"  


# Modelo para gestionar las actividades disponibles en el gimnasio
class Actividad(models.Model):
    
    # Opciones de duración de las actividades
    DURACIONES = [
        ('00:30:00', '30 minutos'),
        ('01:00:00', '1 hora'),
        ('01:30:00', '1 hora y 30 minutos'),
        ('02:00:00', '2 horas'),
    ]
    
    # Opciones de horarios para las actividades
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
    
    # Campos del modelo Actividad
    nombre = models.CharField(max_length=50) 
    descripcion = models.TextField(blank=True, null=True)  # Descripción opcional de la actividad
    duracion = models.CharField(max_length=8, choices=DURACIONES, default='01:00:00')  # Duración de la actividad
    especialidad = models.CharField(max_length=50, choices=Instructor.especialidades)  # Especialidad requerida para la actividad
    horario = models.CharField(max_length=8, choices=HORARIOS, default='06:00:00')  # Horario en el que se dicta la actividad
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='actividades')  # Relación con el instructor encargado

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}" 