from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Resena, Lugar
class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'nombre', 'apellido', 'tiposexo', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido', 'tiposexo', 'fecha_nacimiento', 'seudonimo', 'avatar')}),
        ('Permisos', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre', 'apellido', 'tiposexo', 'fecha_nacimiento', 'seudonimo', 'avatar', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    ordering = ('email',)

    filter_horizontal = ()
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Resena)
admin.site.register(Lugar)
