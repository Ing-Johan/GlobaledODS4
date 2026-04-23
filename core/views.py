import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .forms import RegistroForm, LoginForm, RecuperarForm
from .models import ResultadoTest

# ── Datos estáticos ──────────────────────────────────────────
METAS_ODS4 = [
    {"num": "4.1", "titulo": "Educación primaria y secundaria gratuita",
     "desc": "Garantizar que todos los niños y niñas terminen la enseñanza primaria y secundaria, gratuita, equitativa y de calidad.",
     "categoria": "Acceso universal"},
    {"num": "4.2", "titulo": "Atención y educación en la primera infancia",
     "desc": "Asegurar que todas las niñas y niños tengan acceso a servicios de atención y desarrollo en la primera infancia y educación preescolar de calidad.",
     "categoria": "Primera infancia"},
    {"num": "4.3", "titulo": "Acceso igualitario a la educación superior",
     "desc": "Asegurar el acceso igualitario de todos los hombres y mujeres a una formación técnica, profesional y superior de calidad, incluida la universitaria.",
     "categoria": "Educación superior"},
    {"num": "4.4", "titulo": "Competencias para el empleo",
     "desc": "Aumentar el número de jóvenes y adultos que tienen las competencias técnicas y profesionales necesarias para acceder al empleo.",
     "categoria": "Habilidades"},
    {"num": "4.5", "titulo": "Igualdad de género y acceso universal",
     "desc": "Eliminar las disparidades de género y garantizar el acceso igualitario a todos los niveles de enseñanza para personas en situación de vulnerabilidad.",
     "categoria": "Equidad"},
    {"num": "4.6", "titulo": "Alfabetización universal",
     "desc": "Garantizar que todos los jóvenes y una proporción considerable de adultos estén alfabetizados y tengan nociones elementales de aritmética.",
     "categoria": "Alfabetización"},
    {"num": "4.7", "titulo": "Educación para el desarrollo sostenible",
     "desc": "Garantizar que todos adquieran conocimientos para promover el desarrollo sostenible, los derechos humanos y la cultura de paz.",
     "categoria": "Sostenibilidad"},
    {"num": "4.a", "titulo": "Entornos de aprendizaje seguros",
     "desc": "Construir instalaciones educativas inclusivas, seguras y adecuadas para niños y personas con discapacidad.",
     "categoria": "Infraestructura"},
    {"num": "4.b", "titulo": "Becas para países en desarrollo",
     "desc": "Aumentar a nivel mundial el número de becas disponibles para países en desarrollo, especialmente los menos adelantados.",
     "categoria": "Financiamiento"},
    {"num": "4.c", "titulo": "Docentes capacitados",
     "desc": "Aumentar considerablemente la oferta de docentes calificados mediante cooperación internacional para la formación docente.",
     "categoria": "Docentes"},
]

# ── Vistas públicas ───────────────────────────────────────────
def splash(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/splash.html')


def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/welcome.html')


def registro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegistroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f'¡Bienvenido, {user.username}! Tu cuenta ha sido creada.')
        return redirect('dashboard')
    return render(request, 'core/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user:
            login(request, user)
            return redirect(request.GET.get('next', 'dashboard'))
        messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('splash')


def recuperar(request):
    form = RecuperarForm(request.POST or None)
    enviado = False
    if request.method == 'POST' and form.is_valid():
        enviado = True
        messages.success(request, 'Si el usuario existe, recibirás instrucciones pronto.')
    return render(request, 'core/recover.html', {'form': form, 'enviado': enviado})


# ── Vistas protegidas ─────────────────────────────────────────
@login_required
def dashboard(request):
    resultados = ResultadoTest.objects.filter(user=request.user)[:5]
    puntaje    = request.user.perfil.puntaje_total
    return render(request, 'core/dashboard.html', {
        'resultados': resultados,
        'puntaje': puntaje,
    })


@login_required
def explorar(request):
    return render(request, 'core/explorar.html')


@login_required
def metas(request):
    return render(request, 'core/metas.html', {'metas': METAS_ODS4})


@login_required
def tests(request):
    resultados = ResultadoTest.objects.filter(user=request.user)[:8]
    puntaje    = request.user.perfil.puntaje_total
    return render(request, 'core/tests.html', {
        'resultados': resultados,
        'puntaje': puntaje,
    })


@login_required
@require_POST
def guardar_resultado(request):
    try:
        data      = json.loads(request.body)
        categoria = data.get('categoria', 'General')
        correctas = int(data.get('correctas', 0))
        total     = int(data.get('total', 0))

        ResultadoTest.objects.create(
            user=request.user,
            categoria=categoria,
            correctas=correctas,
            total=total,
        )
        perfil = request.user.perfil
        perfil.puntaje_total += correctas
        perfil.save()
        return JsonResponse({'ok': True})
    except Exception as e:
        return JsonResponse({'ok': False, 'error': str(e)}, status=400)

