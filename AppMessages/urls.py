from django.urls import path
from .views import InboxView, MessageDetailView, SendMessageView

app_name = 'AppMessages'

urlpatterns = [
    path('inbox/', InboxView, name='inbox'),
    path('message/<int:message_id>/', MessageDetailView, name='message_detail'),
    path('send/', SendMessageView, name='send_message'),
]
