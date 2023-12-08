from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser ingresado.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tiposexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'),('femenino', 'Femenino'),])
    fecha_nacimiento = models.DateField(null=True)
    email = models.EmailField(unique=True)
    seudonimo = models.CharField(max_length=100)
    AVATAR_CHOICES = [
        ('chico.png', 'Avatar Chico'),
        ('madre.png', 'Avatar Madre'),
        ('papa.png', 'Avatar Papa'),
        # Agrega más opciones según sea necesario
    ]
    avatar = models.CharField(max_length=100, null=True, blank=True, choices=AVATAR_CHOICES)

    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tiposexo', 'fecha_nacimiento', 'seudonimo']

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'