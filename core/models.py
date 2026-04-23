from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    edad          = models.PositiveIntegerField(null=True, blank=True)
    puntaje_total = models.IntegerField(default=0)

    def __str__(self):
        return f"Perfil de {self.user.username}"


class ResultadoTest(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resultados')
    categoria = models.CharField(max_length=120)
    correctas = models.IntegerField(default=0)
    total     = models.IntegerField(default=0)
    fecha     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']

    def porcentaje(self):
        return round((self.correctas / self.total) * 100) if self.total else 0

    def __str__(self):
        return f"{self.user.username} — {self.categoria} ({self.porcentaje()}%)"


# Crea el perfil automáticamente al crear un usuario
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.get_or_create(user=instance)
