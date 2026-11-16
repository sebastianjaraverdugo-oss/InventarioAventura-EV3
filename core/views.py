
from django.shortcuts import render
from experiencias.models import Experiencia, Categoria

def inicio(request):
    experiencias = Experiencia.objects.filter(activa=True).order_by('fecha')
    categorias = Categoria.objects.all()

    contexto = {
        'experiencias': experiencias,
        'categorias': categorias,
    }

    return render(request, 'core/inicio.html', contexto)
