from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE) # Remitente del mensaje (Usuario que envía)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE) # Destinatario del mensaje (Usuario que recibe)
    content = models.TextField() # Contenido del mensaje
    timestamp = models.DateTimeField(auto_now_add=True) # Fecha y hora de envío (se asigna automáticamente al crear el mensaje)
    is_read = models.BooleanField(default=False) # Estado de lectura del mensaje (False por defecto)

    def __str__(self):
        return f"Mensaje de {self.sender.username} a {self.receiver.username}"

    class Meta:
        ordering = ['-timestamp']  # Ordenar los mensajes más recientes primero