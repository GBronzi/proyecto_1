from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message
from .forms import MessageForm

# =============================Enviar mensaje================================================
@login_required
def SendMessageView(request):
    """
    Vista para enviar mensajes entre usuarios autenticados.
    """
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')  # Obtiene el ID del destinatario desde el formulario

        # Evitar que el usuario se envíe mensajes a sí mismo
        if receiver_id == str(request.user.id):
            messages.error(request, "No puedes enviarte un mensaje a ti mismo.")
            return redirect('AppMessages:send_message')

        receiver = User.objects.get(id=receiver_id)  # Obtiene el usuario destinatario
        content = request.POST.get('content')  # Obtiene el contenido del mensaje

        # Crea y guarda el mensaje
        message = Message(sender=request.user, receiver=receiver, content=content)
        message.save()

        messages.success(request, "¡Mensaje enviado con éxito!")
        return redirect('AppMessages:inbox')  # Redirige a la bandeja de entrada

    # Lista de usuarios disponibles para enviar mensajes (excluyendo al usuario actual)
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'AppMessages/send_message.html', {'users': users})

# =============================Vista bandeja entrada mensajes================================
@login_required
def InboxView(request):
    """
    Vista para mostrar los mensajes recibidos por el usuario autenticado.
    """
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')  # Mensajes ordenados por fecha
    unread_count = Message.objects.filter(receiver=request.user, is_read=False).count()  # Contador de mensajes no leídos

    return render(request, 'AppMessages/inbox.html', {
        'received_messages': received_messages,
        'unread_count': unread_count
    })

# =============================Detalles del mensaje================================================
@login_required
def MessageDetailView(request, message_id):
    """
    Vista para ver el detalle de un mensaje específico.
    Si el mensaje no ha sido leído y el usuario es el receptor, se marca como leído.
    """
    message = get_object_or_404(Message, id=message_id)

    # Si el mensaje pertenece al usuario y no ha sido leído, lo marca como leído
    if not message.is_read and message.receiver == request.user:
        message.is_read = True
        message.save()

    return render(request, 'AppMessages/message_detail.html', {'message': message})