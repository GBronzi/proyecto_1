from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileAuthenticationForm, UserRegistrationForm, EditProfileForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile

def login_view(request):
    if request.method == "POST":
        form = ProfileAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige al index después de iniciar sesión
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Formulario no válido")
    else:
        form = ProfileAuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige al home

def index(request):
    return render(request, 'AppCoder/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
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
            return redirect('AppAccounts:profile')  # Redirige al perfil después de guardar
    else:
        form = EditProfileForm(instance=request.user.profile)
    return render(request, 'Accounts/edit_profile.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'Accounts/change_password.html'  
    success_url = reverse_lazy('AppAccounts:profile')  # Redirige al perfil después de cambiar la contraseña
    
def index(request):
    return render(request, 'AppCoder/index.html')