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

    local_full_path = os.path.join(settings.MEDIA_ROOT, video_path)
    if not os.path.exists(local_full_path):
        print('ERROR: No existe localmente: ' + local_full_path)
        no_exist += 1
        continue

    # Usar solo el nombre del archivo para Cloudinary, no la ruta completa
    filename = os.path.basename(video_path)

    try:
        with open(local_full_path, 'rb') as f:
            contenido.video_file.save(filename, File(f), save=True)
        subidos += 1
        print('OK: Subido ' + filename)
    except CloudinaryError as e:
        skipped += 1
        print('ERROR Cloudinary para ' + filename + ': ' + str(e))
    except Exception as e:
        skipped += 1
        print('ERROR subiendo ' + filename + ': ' + str(e))

print('')
print('Resumen:')
print('Videos subidos: ' + str(subidos))
print('Videos omitidos (sin path o con error): ' + str(skipped))
print('Videos faltantes localmente: ' + str(no_exist))
print('')
print('Listo. Los videos nuevos deberian estar disponibles en produccion.')