# proyecto_1

# AppCoder

**AppCoder** es una aplicación web simple que permite gestionar **estudiantes** y **profesores**. Este proyecto fue hecho con **Python** y **Django** como una manera fácil de aprender y poner en práctica lo que se sabe sobre desarrollo web.

## ¿Qué hace AppCoder?

- **Gestión de Estudiantes**: Puedes agregar estudiantes nuevos, ver su lista y buscar por nombre, apellido o correo.
- **Gestión de Profesores**: Igual que con los estudiantes, puedes agregar profesores y ver la lista.
- **Búsqueda**: Si tienes muchos estudiantes o profesores, puedes buscar a alguien por su nombre o email.
  
La página está hecha con **Bootstrap**, lo que significa que se ve bien en cualquier dispositivo.

## ¿Qué necesitas para ejecutar el proyecto?

- **Python 3.x**: Asegúrate de tener la versión más reciente de Python.
- **Django**: Si no lo tienes, puedes instalarlo fácilmente.

## ¿Cómo instalar y ejecutar el proyecto?

1. **Clona el proyecto**:
   Si aún no tienes el proyecto en tu computadora, abre una terminal y escribe:

   ```bash
   git clone direccion 

   2. Navega al directorio del proyecto:

    ```bash
    cd appcoder
    ```

3. Crea un entorno virtual e instala las dependencias necesarias:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

4. Aplica las migraciones para crear las tablas en la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Corre el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

6. Abre tu navegador y visita `http://127.0.0.1:8000/
