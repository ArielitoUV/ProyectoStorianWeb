from django.contrib import admin
from django.urls import path
from core import views
from core.views import registrar_usuario,iniciar_sesion,registrar_resena,gestionar_perfil,report_contacto



urlpatterns = [
    path('',views.index,name="index"),
    path('registro/', registrar_usuario, name='registrar_usuario'),
    # path('registro/',views.registro,name="registro"),
    # path('iniciosesion/',views.iniciosesion,name="iniciosesion"),
    path('iniciosesion/', iniciar_sesion, name='iniciar_sesion'),
    path('busqueda/',views.busqueda,name="busqueda"),
    path('viajetiempo/',views.viajetiempo,name="viajetiempo"),
    # path('reseñas/',views.reseñas,name="reseñas"),
    path('registrar_resena/', registrar_resena, name='registrar_resena'),
    path('planificar/',views.planificar,name="planificar"),
    path('mapa/',views.mapa,name="mapa"),
    # path('contacto/',views.contacto,name="contacto"),
    path('contacto/', report_contacto, name='contacto'),
    path('micuenta/', gestionar_perfil, name='gestionar_perfil'),
    path('finalresena/',views.finalresena,name="finalresena"),
    path('admin/', admin.site.urls),
]


