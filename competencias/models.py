from django.db import models
from django.contrib.auth.models import User


class Competencia(models.Model):
    """Las 4 áreas de aprendizaje alineadas con el ODS 4."""
    ICONOS = {
        'razonamiento':  '🔢',
        'lectura':       '📖',
        'ciudadana':     '🌍',
        'ciencias':      '🔬',
    }

    nombre      = models.CharField(max_length=120)
    slug        = models.SlugField(unique=True)
    descripcion = models.TextField()
    color       = models.CharField(max_length=7, default='#1565C0',
                                   help_text='Color HEX para la UI')
    icono       = models.CharField(max_length=4, default='📚')
    orden       = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name        = 'Competencia'
        verbose_name_plural = 'Competencias'

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    """Cada competencia tiene 5 niveles de dificultad creciente."""
    competencia = models.ForeignKey(
        Competencia, on_delete=models.CASCADE, related_name='niveles'
    )
    numero      = models.PositiveSmallIntegerField()   # 1–5
    titulo      = models.CharField(max_length=160)
    descripcion = models.CharField(max_length=300)

    class Meta:
        ordering            = ['numero']
        unique_together     = ('competencia', 'numero')
        verbose_name        = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return f"{self.competencia.nombre} – Nivel {self.numero}"

    def etiqueta_dificultad(self):
        etiquetas = {1: 'Básico', 2: 'Elemental', 3: 'Intermedio',
                     4: 'Avanzado', 5: 'Experto'}
        return etiquetas.get(self.numero, '')


class Contenido(models.Model):
    """Explicación educativa que el alumno ve ANTES del quiz."""
    nivel      = models.OneToOneField(
        Nivel, on_delete=models.CASCADE, related_name='contenido'
    )
    titulo     = models.CharField(max_length=200)
    cuerpo     = models.TextField(help_text='Texto principal de la lección')
    ejemplo    = models.TextField(blank=True,
                                  help_text='Ejemplo concreto para el niño')
    tip        = models.CharField(max_length=300, blank=True,
                                  help_text='Tip rápido o frase memorable')

    class Meta:
        verbose_name        = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return f"Contenido: {self.titulo}"


class Pregunta(models.Model):
    """Pregunta de opción múltiple vinculada a un nivel."""
    nivel  = models.ForeignKey(
        Nivel, on_delete=models.CASCADE, related_name='preguntas'
    )
    texto  = models.TextField()
    orden  = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering            = ['orden']
        verbose_name        = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return f"[{self.nivel}] {self.texto[:60]}"


class Opcion(models.Model):
    """4 opciones por pregunta; solo 1 es correcta."""
    pregunta  = models.ForeignKey(
        Pregunta, on_delete=models.CASCADE, related_name='opciones'
    )
    texto     = models.CharField(max_length=300)
    correcta  = models.BooleanField(default=False)
    orden     = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering            = ['orden']
        verbose_name        = 'Opción'
        verbose_name_plural = 'Opciones'

    def __str__(self):
        marca = '✓' if self.correcta else '✗'
        return f"{marca} {self.texto[:50]}"


class ResultadoUsuario(models.Model):
    """Registro del desempeño de un usuario en un nivel."""
    usuario     = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resultados_competencias'
    )
    nivel       = models.ForeignKey(
        Nivel, on_delete=models.CASCADE, related_name='resultados'
    )
    correctas   = models.PositiveSmallIntegerField(default=0)
    total       = models.PositiveSmallIntegerField(default=0)
    completado  = models.BooleanField(default=False)
    fecha       = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering            = ['-actualizado']
        # Un registro por usuario + nivel (se actualiza, no se duplica)
        unique_together     = ('usuario', 'nivel')
        verbose_name        = 'Resultado de usuario'
        verbose_name_plural = 'Resultados de usuarios'

    def __str__(self):
        return (f"{self.usuario.username} | {self.nivel} | "
                f"{self.correctas}/{self.total}")

    def porcentaje(self):
        return round((self.correctas / self.total) * 100) if self.total else 0

    def aprobado(self):
        return self.porcentaje() >= 60