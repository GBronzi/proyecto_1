# Proyecto AppCoder

Este es un proyecto para gestionar socios e instructores en un gimnasio. Se construyó utilizando Django para el backend y HTML con Bootstrap para la interfaz de usuario. El sistema permite agregar, ver y buscar tanto socios como instructores.

## Descripción

La página principal de la aplicación (index.html) incluye las siguientes secciones:

- **Navbar**: Menú de navegación para acceder a las secciones de gestión de socios, instructores, acerca y contacto.
- **Hero Section**: Mensaje de bienvenida que invita al usuario a seleccionar una opción del menú para gestionar socios o instructores.
- **Gestión de Socios**: Sección que permite agregar nuevos socios o consultar la lista de socios existentes.
- **Gestión de Instructores**: Sección similar a la de socios, pero para los instructores del gimnasio.
- **Gestion de Actividades**: Sección donde pueden cargar las actividades realizadas por los socios
- **Buscador**: Sección para buscar socios o instructores por nombre, apellido o correo electrónico.

## Características

- **Agregar Socios**: Permite a los administradores añadir nuevos socios a la base de datos.
- **Ver Lista de Socios**: Muestra todos los socios registrados en la plataforma.
- **Agregar Instructores**: Permite agregar nuevos instructores para el gimnasio.
- **Ver Lista de Instructores**: Permite visualizar todos los instructores registrados.
- **Carga de Actividades**: Permite agregar nuevas actividades para los socios.
- **Ver lista de actividades**: Permite visualizar las actividades del socio con su respectivo instructor. adicional puede editar o eliminar actividad
- **Buscador**: Los usuarios pueden buscar socios e instructores por nombre, apellido o email.

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone -->direccion repositorio en github.com<--
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd MiProyecto
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
   Django          5.1.4
   virtualenv      20.28.0

5. Aplica las migraciones de la base de datos:
   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para poder acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```

7. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

8. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000`.

## Capturas de Pantalla

A continuación, algunas capturas de pantalla de la interfaz de la aplicación:

### Página principal
![Página principal](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/master/AppCoder/static/img/pag_1.png)

### Gestión de Socios
![Gestión de Socios](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/master/AppCoder/static/img/pag_2.png)

### Gestión de Instructores
![Gestiond de Instructores](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/master/AppCoder/static/img/pag_3.png)
