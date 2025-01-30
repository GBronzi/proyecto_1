from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileAuthenticationForm, UserRegistrationForm, EditProfileForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile
from django.conf import settings

def login_view(request):
    if request.method == "POST":
        form = ProfileAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Mensaje de éxito
                messages.success(request, "¡Bienvenido, has iniciado sesión con éxito!")
                return redirect('index')  # Redirige al index después de iniciar sesión
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Datos no válidos")
    else:
        form = ProfileAuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Mensaje de éxito
    messages.success(request, "¡Has cerrado sesión correctamente!")
    return redirect('index')  # Redirige al home

def index(request):
    return render(request, 'AppCoder/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Mensaje de éxito
            messages.success(request, "¡Te has registrado con éxito!")
            return redirect('index')  # Redirige al index después de registrarse
    else:
        form = UserRegistrationForm()
    return render(request, 'Accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'Accounts/profile.html', {'user': profile})

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            form.save()
            # Mensaje de éxito
            messages.success(request, "¡Perfil actualizado con éxito!")
            return redirect('AppAccounts:profile')  # Redirige al perfil después de guardar
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'Accounts/edit_profile.html', {'form': form})

def edit_profile(request):
    form = EditProfileForm(instance=request.user.profile)
    return render(request, "edit_perfil.html", {"form": form, "MEDIA_URL": settings.MEDIA_URL})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'Accounts/change_password.html'  
    success_url = reverse_lazy('AppAccounts:profile')  # Redirige al perfil después de cambiar la contraseña
    # Mensaje de éxito
    def form_valid(self, form):
        messages.success(self.request, "¡Contraseña cambiada con éxito!")
        return super().form_valid(form)
