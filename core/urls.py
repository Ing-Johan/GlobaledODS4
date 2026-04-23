from django.urls import path
from . import views

urlpatterns = [
    path('',                   views.splash,            name='splash'),
    path('inicio/',            views.welcome,           name='welcome'),
    path('registro/',          views.registro,          name='registro'),
    path('login/',             views.login_view,        name='login'),
    path('logout/',            views.logout_view,       name='logout'),
    path('recuperar/',         views.recuperar,         name='recuperar'),
    path('dashboard/',         views.dashboard,         name='dashboard'),
    path('explorar/',          views.explorar,          name='explorar'),
    path('metas/',             views.metas,             name='metas'),
    path('tests/',             views.tests,             name='tests'),
    path('tests/guardar/',     views.guardar_resultado, name='guardar_resultado'),
]