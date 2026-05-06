import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from competencias.models import Contenido

print('Reseteando rutas de videos duplicadas...')

reseted = 0
for contenido in Contenido.objects.exclude(video_file=''):
    video_path = contenido.video_file.name

    # Si la ruta tiene duplicación, corregirla
    if 'videos/2026/05/videos/2026/05/' in video_path:
        # Extraer solo la parte final después de la segunda duplicación
        parts = video_path.split('videos/2026/05/videos/2026/05/')
        if len(parts) > 1:
            corrected_path = 'videos/2026/05/videos/2026/05/' + parts[1]
            contenido.video_file.name = corrected_path
            contenido.save()
            reseted += 1
            print(f'  ✓ Corregido: {corrected_path}')

print(f'\nRutas reseteadas: {reseted}')