from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Título del post
    subtitle = models.CharField(max_length=200)  # Subtítulo
    content = models.TextField(default = "default contenent") # Contenido del post
    image = models.ImageField(upload_to='posts/', null=True, blank=True)  # Imagen opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Ultima actualización

    def __str__(self):
        return self.title

