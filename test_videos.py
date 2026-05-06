import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from competencias.models import Contenido
from django.conf import settings

print('Verificando configuración de videos...')

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL', 'cloudinary://649355296422886:RTHChP8mCqRZmkt2FU1nmDawj8o@dysab8vmt')
if CLOUDINARY_URL and CLOUDINARY_URL != 'cloudinary://649355296422886:RTHChP8mCqRZmkt2FU1nmDawj8o@dysab8vmt':
    print('✓ CLOUDINARY_URL está configurado (desde variable de entorno)')
else:
    print('✓ CLOUDINARY_URL configurado por defecto en settings.py')

print(f'MEDIA_ROOT: {settings.MEDIA_ROOT}')
print(f'DEFAULT_FILE_STORAGE: {getattr(settings, "DEFAULT_FILE_STORAGE", "django.core.files.storage.FileSystemStorage (default)")}')

videos_en_db = Contenido.objects.exclude(video_file='').count()
print(f'Videos en base de datos: {videos_en_db}')

if videos_en_db > 0:
    print('\nPrimeros 5 videos encontrados:')
    for contenido in Contenido.objects.exclude(video_file='')[:5]:
        video_path = contenido.video_file.name
        local_full_path = settings.MEDIA_ROOT / video_path
        existe_local = local_full_path.exists()
        print(f'  - {video_path} (local: {"✓" if existe_local else "✗"})')

print('\nPara subir videos a Cloudinary:')
print('1. Las credenciales ya están configuradas en settings.py')
print('2. Ejecuta: python upload_videos_cloudinary.py')
print('3. Los videos nuevos se subirán automáticamente')
