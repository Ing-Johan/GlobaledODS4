from django.contrib import admin
from .models import Competencia, Nivel, Contenido, Pregunta, Opcion, ResultadoUsuario


class OpcionInline(admin.TabularInline):
    model  = Opcion
    extra  = 4
    fields = ('texto', 'correcta', 'orden')


class PreguntaInline(admin.StackedInline):
    model  = Pregunta
    extra  = 5
    fields = ('texto', 'orden')
    show_change_link = True


class ContenidoInline(admin.StackedInline):
    model  = Contenido
    extra  = 1
    fields = ('titulo', 'cuerpo', 'ejemplo', 'tip')


class NivelInline(admin.TabularInline):
    model  = Nivel
    extra  = 0
    fields = ('numero', 'titulo', 'descripcion')
    show_change_link = True


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'slug', 'color', 'orden')
    prepopulated_fields = {'slug': ('nombre',)}
    inlines       = [NivelInline]


@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display  = ('__str__', 'numero', 'etiqueta_dificultad')
    list_filter   = ('competencia',)
    inlines       = [ContenidoInline, PreguntaInline]


@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'nivel', 'orden')
    list_filter  = ('nivel__competencia', 'nivel')
    inlines      = [OpcionInline]


@admin.register(ResultadoUsuario)
class ResultadoUsuarioAdmin(admin.ModelAdmin):
    list_display  = ('usuario', 'nivel', 'correctas', 'total', 'porcentaje', 'aprobado', 'fecha')
    list_filter   = ('nivel__competencia', 'completado')
    readonly_fields = ('fecha', 'actualizado')