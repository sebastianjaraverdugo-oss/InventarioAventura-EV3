from django.db import models
from django.conf import settings


class Perfil(models.Model):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('GUIA', 'Guía'),
        ('TURISTA', 'Turista'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    rol = models.CharField(
        max_length=10,
        choices=ROLES,
        default='TURISTA'
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.get_rol_display()}"