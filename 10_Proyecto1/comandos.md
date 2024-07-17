# Comandos ⌨:
Aqui te presento los comandos para la creación de este ejemplo para trabajar con proyectos y aplicaciones en Django.

## Creación proyecto 🐍
Para crear un proyecto con Django recordar estar en el _directorio_ donde queremos colocar nuestro proyecto.
> Ruta del directorio: `django-admin startproject "Name"`

### Creación aplicacion
Para crear una nueva aplicacion dentro de nuestro proyecto Django recordar estar en el _directorio_ de nuestro proyecto donde queremos colocar la aplicacion.
> Ruta de tu proyecto: `django-admin startapp "Name"`

### Makemigration
Para realizar las migraciones para el manejo de base de datos de la aplicacion, recordar estar en el _directorio_ de nuestro proyecto.
> Ruta de tu proyecto (Dentro donde este el archivo manage): `python manage.py makemigrations`

### Migrate
Con el comando migrate aplica las migraciones para nuestra base de datos.
> Ruta de tu proyecto (Dentro donde este el archivo manage): `python manage.py migrate`

### Runserver
Corre un servidor interno para visualizar nuestro proyecto
> Ruta de la proyecto (Dentro donde este el archivo manage): `python manage.py runserver`