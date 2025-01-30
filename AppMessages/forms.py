from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message  # Modelo asociado al formulario
        fields = ['receiver', 'content']  # Campos que se mostrarán en el formulario
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Área de texto
            'receiver': forms.Select(attrs={'class': 'form-control'})  # Menú desplegable para seleccionar receptor
        }