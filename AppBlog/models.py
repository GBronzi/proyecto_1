from django.db import models
from ckeditor.fields import RichTextField  # Campo de texto enriquecido para el contenido

class Post(models.Model):
    # Campos de la publicación
    title = models.CharField(max_length=200)  # Título del post
    subtitle = models.CharField(max_length=200)  # Subtítulo
    content = RichTextField()  # Campo de texto enriquecido con CKEditor
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # Imagen opcional, almacenada en 'media/posts/'

    # Campos de control de tiempo
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización automática

    def __str__(self):
        return self.title
