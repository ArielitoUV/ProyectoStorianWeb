from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
# from .forms import PerfilForm, CambiarContraseñaForm
from .forms import ResenaForm
from .models import Resena
def registrar_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Renderizar la plantilla con los datos del usuario
            email_body = render_to_string('core/reporte_registro.txt', {'usuario': usuario})
            # Configurar el correo
            subject = 'Nuevo Registro de Usuario en Storian-WEb'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['storianweb@gmail.com']
            # Configurar el correo como mensaje de texto plano
            message = EmailMessage(subject, email_body, from_email, to_email)
            message.send(fail_silently=False)
            # Redirige a la página de inicio de sesión después del registro exitoso
            return redirect('iniciar_sesion')
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomUserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

def index(request):
    return render(request, "core/index.html")

def iniciar_sesion(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirige a la página de inicio después del inicio de sesión exitoso
            return redirect('busqueda')
        else:
            print(form.errors)
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = CustomAuthenticationForm()
    return render(request, 'core/iniciosesion.html', {'form': form})


def busqueda(request):
    return render(request, "core/busqueda.html")

def viajetiempo(request):
    return render(request, "core/viajetiempo.html")



def registrar_resena(request):
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save()
            
            # Renderizar la plantilla con los datos de la reseña
            email_body = render_to_string('core/reporte_resena.txt', {'resena': resena})
            
            # Configurar el correo
            subject = 'Nueva Reseña en Storian-Web'
            from_email = settings.EMAIL_HOST_USER
            to_email = ['storianweb@gmail.com']  # Cambia a la dirección de correo del administrador
            # Configurar el correo como mensaje de texto plano
            message = EmailMessage(subject, email_body, from_email, to_email)
            message.send(fail_silently=False)
            
            # Redirige a alguna página después de la creación de la reseña
            return redirect('reseñaagrax')  # Puedes crear una página de agradecimiento
            
    else:
        # Si no es una solicitud POST, crea un nuevo formulario (limpio)
        form = ResenaForm()
        
    return render(request, 'core/reseñas.html', {'form': form})


def planificar(request):
    return render(request, "core/planificar.html")

def mapa(request):
    return render(request, "core/mapa.html")

def contacto(request):
    return render(request, "core/contacto.html")

def micuenta(request):
    return render(request, "core/micuenta.html")