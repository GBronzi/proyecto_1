from django import forms
from .models import Socio, Instructor, Actividad

# Formulario para la creación y edición de Socios
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio  # Se define el modelo al que está vinculado el formulario
        fields = ['nombre', 'apellido', 'email', 'edad', 'telefono', 'tipo_clase']  # Campos que aparecerán en el formulario

# Formulario para la creación y edición de Instructores
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor  # Se define el modelo al que está vinculado el formulario
        fields = ['nombre', 'apellido', 'email', 'especialidad']  # Campos que aparecerán en el formulario

# Formulario para la gestión de Actividades
class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad  # Se define el modelo al que está vinculado el formulario
        fields = ['nombre', 'descripcion', 'duracion', 'especialidad', 'horario', 'instructor']  # Campos incluidos en el formulario
        
        # Personalización de los widgets para mejorar la interfaz del formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),  
            'duracion': forms.Select(attrs={'class': 'form-control'}),  
            'instructor': forms.Select(attrs={'class': 'form-control'}),  
            'especialidad': forms.Select(attrs={'class': 'form-control'}),  
            'horario': forms.Select(attrs={'class': 'form-control'}), 
        }