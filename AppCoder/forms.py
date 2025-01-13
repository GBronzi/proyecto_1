from django import forms
from .models import Socio, Instructor, Actividad

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'email', 'edad', 'telefono', 'tipo_clase']
        
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre', 'apellido', 'email', 'especialidad']

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'duracion', 'instructor', 'horario', 'cupo_maximo']

