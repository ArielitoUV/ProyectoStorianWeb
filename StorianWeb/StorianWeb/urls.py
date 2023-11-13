"""StorianWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('',views.index,name="index"),
    path('registro/',views.registro,name="registro"),
    path('iniciosesion/',views.iniciosesion,name="iniciosesion"),
    path('busqueda/',views.busqueda,name="busqueda"),
    path('viajetiempo/',views.viajetiempo,name="viajetiempo"),
    path('reseñas/',views.reseñas,name="reseñas"),
    path('planificar/',views.planificar,name="planificar"),
    path('formulariovisita/',views.formulariovisita,name="formulariovisita"),
    path('informacion/',views.informacion,name="informacion"),
    path('usuarios/',views.usuarios,name="usuarios"),
    path('mapa/',views.mapa,name="mapa"),
    path('admin/', admin.site.urls),
]

