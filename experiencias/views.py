
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from .models import Experiencia, Inscripcion


@login_required(login_url='/login/')
def inscribirse(request, experiencia_id):
    if request.method != 'POST':
        return redirect('inicio')

    experiencia = get_object_or_404(
        Experiencia,
        id=experiencia_id,
        activa=True
    )

    if experiencia.cupos <= 0:
        messages.error(request, 'No quedan cupos disponibles.')
        return redirect('inicio')

    inscripcion, creada = Inscripcion.objects.get_or_create(
        turista=request.user,
        experiencia=experiencia
    )

    if creada:
        experiencia.cupos -= 1
        experiencia.save(update_fields=['cupos'])
        messages.success(request, 'Inscripción realizada correctamente.')
    else:
        messages.warning(request, 'Ya estás inscrito en esta experiencia.')

    return redirect('inicio')
