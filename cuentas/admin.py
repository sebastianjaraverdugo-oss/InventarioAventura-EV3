from django.contrib import admin
from .models import Perfil


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')
    search_fields = ('usuario__username',)
    list_filter = ('rol',)