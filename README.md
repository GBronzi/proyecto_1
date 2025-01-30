# Proyecto  Gestión de Socios e Instructores

Este es un proyecto para gestionar socios e instructores en un gimnasio. Se ha desarrollado utilizando **Django** para el backend y **HTML con Bootstrap** para la interfaz de usuario. El sistema permite agregar, ver y buscar tanto socios como instructores, así como gestionar actividades realizadas por los socios.

## Descripción

La aplicación está compuesta por diferentes secciones que permiten una gestión completa de socios, instructores y actividades:

- **Navbar**: Menú de navegación para acceder a las secciones de gestión de socios, instructores, actividades, perfiles y mensajería.
- **Hero Section**: Un mensaje de bienvenida que invita al usuario a seleccionar una opción del menú para gestionar los datos del gimnasio.
- **Gestión de Socios**: Permite agregar nuevos socios o consultar la lista de socios existentes, con funcionalidades para editar y eliminar registros.
- **Gestión de Instructores**: Similar a la de socios, pero dedicada a los instructores del gimnasio.
- **Gestión de Actividades**: Sección donde se pueden agregar, editar o eliminar las actividades realizadas por los socios.
- **Buscador**: Herramienta que permite buscar tanto socios como instructores por nombre, apellido o correo electrónico.
- **Sistema de Mensajería**: Funcionalidad que permite a los usuarios enviarse mensajes entre sí.
- **Login de Usuario**: Los usuarios pueden registrarse, iniciar sesión y acceder a su perfil para editar y actualizar su información personal, incluyendo avatar, biografía y fecha de nacimiento.

## Características

- **Autenticación de usuarios**: Los usuarios pueden registrarse, iniciar sesión y editar sus perfiles. La funcionalidad incluye campos como nombre, apellido, avatar, biografía y fecha de nacimiento.
- **Gestión de Socios**: Los administradores pueden agregar, ver, editar y eliminar socios.
- **Gestión de Instructores**: Los administradores pueden agregar, ver, editar y eliminar instructores.
- **Gestión de Actividades**: Los socios pueden cargar nuevas actividades, y se puede editar o eliminar cualquier actividad existente.
- **Buscador**: Permite buscar socios e instructores por nombre, apellido o correo electrónico.
- **Mensajería entre usuarios**: Los usuarios pueden enviarse mensajes y recibir notificaciones sobre nuevos mensajes o actualizaciones.
- **Notificaciones de éxito**: Mensajes de confirmación que indican si las acciones fueron exitosas (crear, editar, eliminar).
- **Edición de perfil de usuario**: Los usuarios pueden acceder a su perfil y actualizar sus datos personales, incluyendo el avatar y biografía.

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
![Página principal](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/main/AppCoder/static/img/pag_1.1.png)

### Gestión de Socios
![Gestión de Socios](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/master/AppCoder/static/img/pag_2.png)

### Gestión de Instructores
![Gestion de Instructores](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/main/static/img/pag_3.png)

### Blog
![Lista del Blog](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/main/static/img/pag_4.png)

### Login
![Ingreso de usuario registrado](https://raw.githubusercontent.com/GBronzi/proyecto_1/refs/heads/main/static/img/pag_5.png)
