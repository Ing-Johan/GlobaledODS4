from django.urls import path
from . import views

app_name = 'competencias'

urlpatterns = [
    # Lista de las 4 competencias
    path('',
         views.lista_competencias,
         name='lista'),

    # Niveles de una competencia
    path('<slug:slug>/',
         views.lista_niveles,
         name='niveles'),

    # Contenido educativo de un nivel (lección)
    path('<slug:slug>/nivel/<int:numero>/leccion/',
         views.contenido,
         name='contenido'),

    # Quiz de un nivel
    path('<slug:slug>/nivel/<int:numero>/quiz/',
         views.quiz,
         name='quiz'),

    # Resultado tras enviar el quiz
    path('<slug:slug>/nivel/<int:numero>/resultado/',
         views.resultado,
         name='resultado'),
]