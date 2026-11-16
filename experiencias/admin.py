from django.contrib import admin
from .models import Categoria, Experiencia, Inscripcion


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 'categoria', 'guia',
        'fecha', 'cupos', 'precio', 'activa'
    )
    search_fields = ('titulo', 'descripcion')
    list_filter = ('categoria', 'activa', 'fecha')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = (
        'turista', 'experiencia', 'fecha_inscripcion'
    )
    search_fields = (
        'turista__username',
        'experiencia__titulo'
    )