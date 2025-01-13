from django import forms
from .models import Socio, Instructor

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'email', 'edad', 'telefono', 'tipo_clase']
        
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['nombre', 'apellido', 'email', 'especialidad']
        
