Objetivos:
-Integrar un proyecto django con PostgreSQL
-Poder cambiar algunas funcionalidades del portfolio y que le quede al alumno un proyecto funcional y que pueda utilizar ademas para la comercializacion del mismo.

-Creacion de un entorno virtual con virtualenv:
virtualenv nombre-del-entorno-virtual

-Activar el entorno virtual

-Instalacion de django:
pip install django

-Creacion de proyecto Django
django-admin startproject config .

-Se puede hacer tranquilamente todo en el proyecto, pero crearemos una app para manejar todo desde ahi. Nuestro proyecto sera tipo monolito
django-admin startapp portfolio

-Agregamos la app a INSTALLED_APPS

-Corremos el servidor para ver si funciona: python manage.py runserver. No preocuparse por el mensaje:
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
Para eso hay que aplicar las migraciones y luego migrarlas, con los siguientes comandos:
python manage.py makemigrations
python manage.py migrate
PERO si vamos a utilizar mas adelante PostgreSQL, por el momento no es necesario


-Creamos la carpeta templates en la app portfolio y dentro de esta otra carpeta que se llame como la app en nuetro caso portfolio y ahi ponemos el archivo index.html.
Para este tutorial usaremos la plantilla gratuita: https://startbootstrap.com/theme/freelancer

-Creamos la carpeta static en la app portfolio y dentro de esta otra carpeta que se llame como la app en nuetro caso portfolio y ahi ponemos los archivos css, js e imagenes y videos.

-Creamos un archivo llamado urls.py en la app portfolio, esto es para manejar de manera mas
ordenada las rutas. Si bien va a ser un proyecto pequeño, para ir acostumbrandose a las buenas
practicas, creemos que es necesario realizarlo asi.
Debemos importar el path: from django.urls import path
y generar la lista de url:
urlpatterns = [
    path(),
]

-En el archivo views.py crearemos una vista y retornaremos el archivo index.html.

-Luego es momento de agregar al urlpatterns nuestra vista, nuestro archivo urls.py de portfolio, quedaria asi:
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
]

-Ahora iremos a urls.py de nuestro proyecto (config) e incluiremos los urls de nuestra app portfolio de la siguiente manera:
from django.urls import path, include (importamos include)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("portfolio.urls")),
]

-Al ver nuestra pagina ya no estara el COHETE DE DJANGO, sino nuestro index pero sin estilos aplicados. Trataremos esto a continuacion.

-En nuestro archivo index.html arriba de todo cargaremos los estaticos:
{% load static %}

y para cargar el css:
<link href="{% static 'portfolio/css/styles.css' %}" rel="stylesheet" />
y para cargar el js:
<script src="{% static 'portfolio/js/scripts.js' %}"></script>

Ahora podremos ver la pagina con estilos y funcionalidades aplicadas. NO veremos las imagenes.
Para eso hay que trabajar de la misma manera que hicimos con el css y el js.

-El proximo paso sera crear los modelos (clases) en el archivo models.py para poder ir personalizando nuestra plantilla.
A modo de practica crearemos dos modelos, uno para todo lo que es datos de la persona y otro que se encargara de los trabajos realizados por esa persona que quiera mostrar en su pagina.
Son los siguientes:
--------------------
from django.db import models

# Create your models here.
class UserData(models.Model):
    title_tab = models.CharField(max_length=100, blank=True)
    image_header = models.ImageField(blank=True, upload_to="images/")
    name = models.CharField(max_length=50, blank=True)
    title_header = models.CharField(max_length=100, blank=True)
    skill_header = models.CharField(max_length=255, blank=True)
    about_me_title = models.CharField(max_length=100, blank=True)
    about_me_text = models.TextField(blank=True)
    cv_file = models.FileField(null=True, upload_to="cv/")
    location = models.CharField(max_length=50, blank=True)
    city_and_country = models.CharField(max_length=50, blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    behance_url = models.URLField(blank=True)

    def __str__(self):
        return f"Portfolio de {self.name}"

class Portfolio(models.Model):
    job_image = models.ImageField(blank=True)
    job_url = models.URLField(blank=True)

# los parametros blank=True es para que no sea obligatorio el ingreso del dato
--------------------
Al utilizar tipos de datos que manejan imagenes debemos de instalar una dependencia llamada pillow,
con el siguiente comando:
pip install Pillow

-Ahora deberemos crear las migraciones con el comando:
python manage.py makemigrations
-Y luego aplicarlas para que se vean reflejadas en la base de datos con el comando:
python manage.py migrate

-Luego crearemos un superusuario para ingresar al panel de administracion que nos provee django, con
el siguiente comando:
python manage.py createsuperuser
usuario: coderhouse
contraseña: 1234

-Para ingresar al panel de administracion debemos ir a: http://127.0.0.1:8000/admin e ingresar las credenciales.

-Para que podamos ver los modelos que creamos en nuestra App portfolio, en el panel de administracion debemos "registrarlos". Para eso tenemos que ir al archivo admin.py de la App portfolio y agregarlos ahi:
--------------------
from django.contrib import admin

from .models import UserData, Portfolio

# Register your models here.
admin.site.register(UserData)
admin.site.register(Portfolio)
--------------------

-Luego podremos crear un modelo de User data en el panel de administracion e ingresar los datos que querramos.
-Despues tenemos que obtener esos datos en la vista que renderiza nuestra unica pagina, y lo hacemos del siguiente modo:
--------------------
def index(request):

    user_data = UserData.objects.first()

    context = {
        "user_data": user_data,
    }
    print(context)

    return render(request, "portfolio/index.html", context)
--------------------

-Y en el index.html tendremos que ir pasando esos datos con la nomenclatura de llaves --> {{ }}

-Para la imagen tenemos que hacer unas configuraciones primero:
--En settings.py debemos agregar:
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

--Y en urls.py del proyecto debemos hacer lo siguiente:
from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

--Finalmente en el index.html 
{% if user_data.image_header %}
    <img class="masthead-avatar mb-5" src="{{user_data.image_header.url}}" alt="Avatar" />
{% else %}
    <img class="masthead-avatar mb-5" src="{% static 'portfolio/assets/img/man.png' %}" alt="Avatar" />
{% endif %}

-Ahora pasaremos a poder mostrar los proyectos, para eso ya tenemos creado el modelo Portfolio, con dos atributos, uno sera la imagen (la debera subir el usuario) y el otro un link para poder acceder al proyecto.
-Luego en el index.html crearemos un bucle for para recorrer todos los proyectos que fue agregando el usuario.

-Por ultimo realizaremos un formulario de contacto para que el usuario puda ver los mensajes que le envian desde en el panel de administracion:
--Creamos la clase:
-----------------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email}"
-----------------

--Luego creamos un archivo en nuestra App portfolio llamado forms.py y en el ponemos el codigo:
-----------------
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField()
------------------

--En el archivo admin.py importamos la clase Contact y la registramos, como hicimos con UserData y Portfolio

--Por ultimo tenemos que modificar un poco la vista index para utilizar el metodo POST del formulario:
------------------
def index(request):

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            messages.success(request, "Muchas gracias por tu contacto")
            
            info = contact_form.cleaned_data

            contact = Contact(name=info['name'], message=info['message'], email=info['email'])

            contact.save()

            contact_form = ContactForm()
        
    else:
        contact_form = ContactForm()

    user_data = UserData.objects.first()
    portfolios = Portfolio.objects.all()

    context = {
        "user_data": user_data,
        "portfolios": portfolios,
        "contact_form": contact_form,
    }

    return render(request, "portfolio/index.html", context)
------------------

--En el index.html tenemos que crear el formulario, lo haremos de dos formas para mostrar como podemos
individualizar cada campo:
METODO 1:
------------------
<form action="" method="POST">
    {% csrf_token %}
    {{contact_form}}
</form>
------------------

METODO 2:
------------------
<form action="" method="POST">
    {% csrf_token %}
    <div class="form-floating mb-3">
        {{contact_form.name}}
        <label for="floatingInput">Nombre</label>
    </div>
    <div class="form-floating mb-3">
        {{contact_form.email}}
        <label for="floatingInput">Correo electrónico</label>
        </div>
    <div class="form-floating mb-3">
        {{contact_form.message}}
        <label for="floatingTextarea">Mensaje</label>
    </div>
    <button class="btn btn-primary btn-xl" id="submitButton" type="submit">Enviar</button>
</form>
------------------

Con esto terminamos.