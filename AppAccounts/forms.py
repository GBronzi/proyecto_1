from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear un perfil con los datos adicionales
            profile = Profile.objects.create(user=user)
            profile.avatar = self.cleaned_data.get('avatar')
            profile.save()
        return user

# Formulario de edición de perfil (Profile)
class EditProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    birthday = forms.DateField(required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birthday']

# Formulario de autenticación de usuario
class ProfileAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']