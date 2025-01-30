from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

AVATAR_CHOICES = [
    ('avatars/avataruser.png', 'Avatar por defecto'),
    ('avatars/avatar1.png', 'Avatar 1'),
    ('avatars/avatar2.png', 'Avatar 2'),
    ('avatars/avatar3.png', 'Avatar 3'),
    ('avatars/avatar4.png', 'Avatar 4'),
    ('avatars/avatar5.png', 'Avatar 5'),
    ('avatars/avatar6.png', 'Avatar 6'),
    ('avatars/avatar7.png', 'Avatar 7'),
    ('avatars/avatar8.png', 'Avatar 8'),
    ('avatars/avatar9.png', 'Avatar 9'),
    ('avatars/avatar10.png', 'Avatar 10'),
    ('avatars/avatar11.png', 'Avatar 11'),
    ('avatars/avatar12.png', 'Avatar 12'),
    ('avatars/avatar13.png', 'Avatar 13'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/avataruser.png')
    bio = RichTextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def get_avatar_url(self):
        return f"/media/{self.avatar}"
