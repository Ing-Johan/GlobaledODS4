import os
import django
import cloudinary

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from django.core.files import File
from competencias.models import Contenido
from django.conf import settings

# Configurar cloudinary con las credenciales
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE["CLOUD_NAME"],
    api_key=settings.CLOUDINARY_STORAGE["API_KEY"],
    api_secret=settings.CLOUDINARY_STORAGE["API_SECRET"]
)

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL', 'cloudinary://649355296422886:RTHChP8mCqRZmkt2FU1nmDawj8o@dysab8vmt')
if not CLOUDINARY_URL:
    print('ERROR: No se pudo configurar CLOUDINARY_URL.')
    print('Verifica que las credenciales estén correctas en settings.py')
    raise SystemExit(1)

print('Subiendo videos locales a Cloudinary...')
print(f'Usando Cloudinary URL: {CLOUDINARY_URL.replace(CLOUDINARY_URL.split(":")[2], "***")}')

print('Subiendo videos locales a Cloudinary...')

subidos = 0
skipped = 0
no_exist = 0

from cloudinary.exceptions import Error as CloudinaryError

for contenido in Contenido.objects.exclude(video_file=''):
    video_path = contenido.video_file.name
    if not video_path:
        skipped += 1
        continue

    local_full_path = settings.MEDIA_ROOT / video_path
    if not local_full_path.exists():
        print(f'  ✗ No existe localmente: {local_full_path}')
        no_exist += 1
        continue

    # Usar solo el nombre del archivo para Cloudinary, no la ruta completa
    filename = os.path.basename(video_path)

    try:
        with open(local_full_path, 'rb') as f:
            contenido.video_file.save(filename, File(f), save=True)
        subidos += 1
        print(f'  ✓ Subido: {filename}')
    except CloudinaryError as e:
        skipped += 1
        print(f'  ✗ Error Cloudinary para {filename}: {e}')
    except Exception as e:
        skipped += 1
        print(f'  ✗ Error subiendo {filename}: {e}')

print('\nResumen:')
print(f'  Videos subidos: {subidos}')
print(f'  Videos omitidos (sin path o con error): {skipped}')
print(f'  Videos faltantes localmente: {no_exist}')
print('\nListo. En producción, asegúrate de definir CLOUDINARY_URL en Render y reiniciar la app.')
