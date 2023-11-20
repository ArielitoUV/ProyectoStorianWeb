from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def registro(request):
    return render(request, "core/registro.html")

def iniciosesion(request):
    return render(request, "core/iniciosesion.html")

def busqueda(request):
    return render(request, "core/busqueda.html")

def viajetiempo(request):
    return render(request, "core/viajetiempo.html")

def reseñas(request):
    return render(request, "core/reseñas.html")

def planificar(request):
    return render(request, "core/planificar.html")

def mapa(request):
    return render(request, "core/mapa.html")

def contacto(request):
    return render(request, "core/contacto.html")

def gestionperfil(request):
    return render(request, "core/gestionperfil.html")