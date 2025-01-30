from django.shortcuts import render, redirect
from .forms import SocioForm, InstructorForm, ActividadForm
from .models import Socio, Instructor, Actividad
from django.db.models import Q
from django.contrib import messages

# =============================Paginas=====================
def index(request):
    return render(request, 'AppCoder/index.html')

def acerca(request):
    return render(request, 'AppCoder/acerca.html')

def contacto(request):
    return render(request, 'AppCoder/contacto.html')

# =============================Cargar Socios================================================
def cargar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Socio cargado con éxito!')
            return redirect('lista_socios')
    else:
        form = SocioForm()
    return render(request, 'AppCoder/form_socio.html', {'form': form})

# ==========================Lista Socios======================================================
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'AppCoder/lista_socios.html', {'socios': socios})

# =============================Carga Instructores=============================================
def cargar_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Instructor cargado con éxito!')
            return redirect('lista_instructores')
    else:
        form = InstructorForm()
    return render(request, 'AppCoder/form_instructor.html', {'form': form})

# =============================Lista Instructores=============================================
def lista_instructores(request):
    instructores = Instructor.objects.all()
    return render(request, 'AppCoder/lista_instructores.html', {'instructores': instructores})

# =============================Actividad=============================================
def lista_actividades(request):
    actividades = Actividad.objects.all()
    return render(request, 'AppCoder/lista_actividades.html', {'actividades': actividades})

def cargar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Actividad cargada con éxito!')
            return redirect('lista_actividades')
    else:
        form = ActividadForm()
    return render(request, 'AppCoder/form_actividad.html', {'form': form})

# =============================Editar Actividad=============================================
def editar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            # Mensaje de éxito
            messages.success(request, '¡Actividad actualizada con éxito!')
            return redirect('lista_actividades')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'AppCoder/editar_actividad.html', {'form': form})

# =============================Eliminar Actividad=============================================
def eliminar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    if request.method == 'POST':
        actividad.delete()
        # Mensaje de éxito
        messages.success(request, '¡Actividad eliminada con éxito!')
        return redirect('lista_actividades')  # Redirige a la lista de actividades
    return render(request, 'AppCoder/eliminar_actividad.html', {'actividad': actividad})

# =============================BUSQUEDA=======================================================
def buscar(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        socios = Socio.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query)
        )
        instructores = Instructor.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(especialidad__icontains=query)
        )

        for socio in socios:
            resultados.append({
                'tipo': 'Socio',
                'nombre': socio.nombre,
                'apellido': socio.apellido,
                'email': socio.email,
                'extra': '-',
            })

        for instructor in instructores:
            resultados.append({
                'tipo': 'Instructor',
                'nombre': instructor.nombre,
                'apellido': instructor.apellido,
                'email': instructor.email,
                'especialidad': f'{instructor.especialidad}',
            })

    return render(request, 'AppCoder/index.html', {'resultados': resultados})
