from django.contrib import admin
from django.urls import path
from core import views
from core.views import registrar_usuario,iniciar_sesion



urlpatterns = [
    path('',views.index,name="index"),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    # path('registro/',views.registro,name="registro"),
    # path('iniciosesion/',views.iniciosesion,name="iniciosesion"),
    path('iniciosesion/', iniciar_sesion, name='iniciar_sesion'),
    path('busqueda/',views.busqueda,name="busqueda"),
    path('viajetiempo/',views.viajetiempo,name="viajetiempo"),
    path('reseñas/',views.reseñas,name="reseñas"),
    path('planificar/',views.planificar,name="planificar"),
    path('mapa/',views.mapa,name="mapa"),
    path('contacto/',views.contacto,name="contacto"),
    path('micuenta/',views.micuenta,name="micuenta"),
    path('finalreseña/',views.finalreseña,name="finalreseña"),
    path('admin/', admin.site.urls),
]


