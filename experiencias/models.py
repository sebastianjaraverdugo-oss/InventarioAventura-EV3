from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Experiencia(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='experiencias'
    )
    guia = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='experiencias_guiadas'
    )
    fecha = models.DateField()
    cupos = models.PositiveIntegerField()
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Inscripcion(models.Model):
    turista = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    experiencia = models.ForeignKey(
        Experiencia,
        on_delete=models.CASCADE,
        related_name='inscripciones'
    )
    fecha_inscripcion = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['turista', 'experiencia'],
                name='inscripcion_unica_turista_experiencia'
            )
        ]

    def __str__(self):
        return f"{self.turista.username} - {self.experiencia.titulo}"