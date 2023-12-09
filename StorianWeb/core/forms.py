from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico'}),
    )
    nombre = forms.CharField(
        label=_("Nombre"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
    )
    seudonimo = forms.CharField(
        label=_("Seudonimo"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su seudonimo'}),
    )
    apellido = forms.CharField(
        label=_("Apellido"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
    )
    fecha_nacimiento = forms.DateField(
        label=_("Fecha de Nacimiento"),
        input_formats=['%d-%m-%Y'],
        widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Fecha de nacimiento DD-MM-YYYY'}),
    )

    tiposexo = forms.ChoiceField(
        label=_("Sexo"),
        choices=[('', 'Seleccione una opción'), ('masculino', 'Masculino'), ('femenino', 'Femenino')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    AVATAR_CHOICES = [
        ('chico.png', 'Chico'),
        ('papa.png', 'Papa'),
        ('madre.png', 'Madre'),
        ('superestrella.png', 'Rebelde'),
        ('estudianteF.png', 'EstudianteF'),
        ('estudianteM.png', 'EstudianteM'),
        # Agrega más opciones de avatar según tus necesidades
    ]

    avatar = forms.ChoiceField(
        choices=AVATAR_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )

    password1 = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
    )

    password2 = forms.CharField(
        label=_("Confirmar contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña'}),
        strip=False,
    )

    class Meta:
        model = Usuario
        fields = ['email', 'nombre', 'apellido', 'fecha_nacimiento', 'avatar', 'seudonimo', 'tiposexo', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("Las contraseñas no coinciden.")
        self.error_messages['password_too_short'] = _("La contraseña debe tener al menos 8 caracteres.")
        self.error_messages['password_common'] = _("La contraseña no puede ser una contraseña común.")
        self.error_messages['password_entirely_numeric'] = _("La contraseña no puede ser completamente numérica.")
        self.error_messages['email_in_use'] = _('Este email ya está en uso. Por favor, elige otro.')
        # Aplica clases de Bootstrap a los campos con errores
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})





class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label=_('Correo electrónico'), widget=forms.EmailInput(attrs={'autofocus': False,'placeholder':'Ingrese correo electrónico'}))
    password = forms.CharField(
        label=_("Contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}),
    )

# class PerfilForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['nombre', 'apellido', 'fecha_nacimiento', 'telefono', 'estado', 'ciudad']

# class CambiarContraseñaForm(PasswordChangeForm):
#     pass