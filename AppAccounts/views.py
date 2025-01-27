from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileAuthenticationForm, UserRegistrationForm, EditProfileForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile

# Vista para el login
def login_view(request):
    if request.method == "POST":
        form = ProfileAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirige al perfil después de iniciar sesión
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    else:
        form = ProfileAuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})

# Vista para el logout
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige al home

# Vista para el registro
def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente")
            return redirect('login')  # Redirige al login
    else:
        form = UserRegistrationForm()
    return render(request, 'Accounts/signup.html', {'form': form})

# Vista para el registro (duplicada, puedes eliminar una de las dos)
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la vista de login después de registrarse
    else:
        form = UserRegistrationForm()
    return render(request, 'Accounts/signup.html', {'form': form})

# Vista Profile
@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'Accounts/profile.html', {'user': profile})

# Vista editar perfil
@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil después de guardar
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'Accounts/edit_profile.html', {'form': form})

# Vista cambiar contraseña
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'Accounts/change_password.html'  
    success_url = reverse_lazy('profile')  # Redirige al perfil después de cambiar la contraseña
