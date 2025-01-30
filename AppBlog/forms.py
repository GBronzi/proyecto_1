from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget 

# Formulario para la creación y edición de publicaciones
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  
        fields = ['title', 'subtitle', 'content', 'image']  # Campos que estarán en el formulario

        # widgets para personalizar la apariencia de los campos
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Campo de texto 
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),  # Campo de subtítulo con 
            'content': forms.CharField(widget=CKEditorWidget()),  # Campo de contenido con CKEditor para texto enriquecido
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),  # Campo para subida de imágenes
        }

    # las etiquetas de los campos en español
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)  # constructor de la clase padre
        self.fields['title'].label = "Título"  # Etiqueta para el título
        self.fields['subtitle'].label = "Subtítulo"  # Etiqueta para el subtítulo
        self.fields['content'].label = "Contenido"  # Etiqueta para el contenido
        self.fields['image'].label = "Imagen (opcional)"  # Etiqueta para la imagen