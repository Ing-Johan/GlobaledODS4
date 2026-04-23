from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from .models import Competencia, Nivel, Pregunta, Opcion, ResultadoUsuario


# ── helpers ──────────────────────────────────────────────────

def _get_nivel(slug, numero):
    comp  = get_object_or_404(Competencia, slug=slug)
    nivel = get_object_or_404(Nivel, competencia=comp, numero=numero)
    return comp, nivel


def _resultado_usuario(user, nivel):
    """Devuelve el ResultadoUsuario o None."""
    try:
        return ResultadoUsuario.objects.get(usuario=user, nivel=nivel)
    except ResultadoUsuario.DoesNotExist:
        return None


# ── vistas ───────────────────────────────────────────────────

@login_required
def lista_competencias(request):
    """Pantalla principal: las 4 competencias."""
    competencias = Competencia.objects.prefetch_related('niveles').all()

    # Para cada competencia calculamos cuántos niveles completó el usuario
    data = []
    for comp in competencias:
        niveles      = comp.niveles.all()
        total_niv    = niveles.count()
        completados  = ResultadoUsuario.objects.filter(
            usuario=request.user,
            nivel__in=niveles,
            completado=True
        ).count()
        data.append({
            'comp': comp,
            'total': total_niv,
            'completados': completados,
            'pct': round((completados / total_niv) * 100) if total_niv else 0,
        })

    return render(request, 'competencias/lista_competencias.html', {'data': data})


@login_required
def lista_niveles(request, slug):
    """Los 5 niveles de una competencia con estado del usuario."""
    comp   = get_object_or_404(Competencia, slug=slug)
    niveles = comp.niveles.select_related('contenido').all()

    resultados_map = {
        r.nivel_id: r
        for r in ResultadoUsuario.objects.filter(
            usuario=request.user, nivel__in=niveles
        )
    }

    niveles_data = []
    for niv in niveles:
        res = resultados_map.get(niv.id)
        niveles_data.append({'nivel': niv, 'resultado': res})

    return render(request, 'competencias/lista_niveles.html', {
        'comp': comp,
        'niveles_data': niveles_data,
    })


@login_required
def contenido(request, slug, numero):
    comp, nivel = _get_nivel(slug, numero)
    contenido = nivel.contenido  # objeto
    texto = contenido.cuerpo     # string real
    lineas = [l.strip() for l in texto.splitlines() if l.strip()]

    resultado = _resultado_usuario(request.user, nivel)

    return render(request, 'competencias/contenido.html', {
        'comp': comp,
        'nivel': nivel,
        'leccion': contenido, 
        'lineas': lineas,
        'resultado': resultado,
    })


@login_required
def quiz(request, slug, numero):
    """Muestra el quiz del nivel."""
    comp, nivel = _get_nivel(slug, numero)
    preguntas   = nivel.preguntas.prefetch_related('opciones').all()

    if not preguntas.exists():
        messages.error(request, 'Este nivel aún no tiene preguntas.')
        return redirect('competencias:contenido', slug=slug, numero=numero)

    return render(request, 'competencias/quiz.html', {
        'comp':      comp,
        'nivel':     nivel,
        'preguntas': preguntas,
    })


@login_required
@require_POST
def resultado(request, slug, numero):
    """Procesa las respuestas y guarda el resultado."""
    comp, nivel = _get_nivel(slug, numero)
    preguntas   = nivel.preguntas.prefetch_related('opciones').all()

    correctas_ids  = set(
        Opcion.objects.filter(
            pregunta__nivel=nivel, correcta=True
        ).values_list('id', flat=True)
    )

    total     = preguntas.count()
    correctas = 0
    detalle   = []   # para mostrar feedback pregunta a pregunta

    for preg in preguntas:
        key            = f'pregunta_{preg.id}'
        opcion_id_str  = request.POST.get(key)
        opcion_elegida = None
        opcion_correcta = preg.opciones.filter(correcta=True).first()
        es_correcto    = False

        if opcion_id_str and opcion_id_str.isdigit():
            opcion_id = int(opcion_id_str)
            try:
                opcion_elegida = preg.opciones.get(id=opcion_id)
                es_correcto    = opcion_id in correctas_ids
                if es_correcto:
                    correctas += 1
            except Opcion.DoesNotExist:
                pass

        detalle.append({
            'pregunta':        preg,
            'elegida':         opcion_elegida,
            'correcta':        opcion_correcta,
            'es_correcto':     es_correcto,
            'sin_responder':   opcion_elegida is None,
        })

    # Guardar o actualizar resultado (update_or_create evita duplicados)
    res, _ = ResultadoUsuario.objects.update_or_create(
        usuario=request.user,
        nivel=nivel,
        defaults={
            'correctas':  correctas,
            'total':      total,
            'completado': True,
        }
    )

    return render(request, 'competencias/resultado.html', {
        'comp':      comp,
        'nivel':     nivel,
        'resultado': res,
        'detalle':   detalle,
        'aprobado':  res.aprobado(),
    })