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
        fields = ['nombre', 'descripcion', 'duracion', 'especialidad', 'horario', 'instructor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'duracion': forms.Select(attrs={'class': 'form-control'}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }
