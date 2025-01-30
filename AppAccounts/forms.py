from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from ckeditor.widgets import CKEditorWidget
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Repetir Contraseña")
    email = forms.EmailField(label="Correo", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    
    AVATAR_CHOICES = [
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

    avatar = forms.ChoiceField(
        choices=AVATAR_CHOICES, 
        required=False, 
        widget=forms.RadioSelect
    )

    bio = forms.CharField(label="Biografia",widget=CKEditorWidget(), required=False)
    birthday = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=False)
    address = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    phone = forms.CharField(label="Telefono", widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{3}-[0-9]{4}', 'placeholder': 'Ingresa tu numero personal: xxx-xxx-xxxx'}), required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'birthday', 'address', 'phone']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)


        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

        if self.instance.avatar:
            self.fields['avatar'].initial = self.instance.avatar


class ProfileAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        
        