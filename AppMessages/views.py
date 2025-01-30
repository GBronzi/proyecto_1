from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def SendMessageView(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')
        if receiver_id == str(request.user.id):
            messages.error(request, "No puedes enviarte un mensaje a ti mismo.")
            return redirect('AppMessages:send_message')

        receiver = User.objects.get(id=receiver_id)
        content = request.POST.get('content')

        message = Message(sender=request.user, receiver=receiver, content=content)
        message.save()

        messages.success(request, "¡Mensaje enviado con éxito!")
        return redirect('AppMessages:inbox')

    users = User.objects.exclude(id=request.user.id)
    return render(request, 'AppMessages/send_message.html', {'users': users})

@login_required
def InboxView(request):
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    unread_count = Message.objects.filter(receiver=request.user, is_read=False).count()
    return render(request, 'AppMessages/inbox.html', {'received_messages': received_messages, 'unread_count': unread_count})

@login_required
def MessageDetailView(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if not message.is_read and message.receiver == request.user:
        message.is_read = True
        message.save()
    return render(request, 'AppMessages/message_detail.html', {'message': message})
