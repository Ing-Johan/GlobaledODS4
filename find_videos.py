import cloudinary
import cloudinary.api
from django.conf import settings
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=settings.CLOUDINARY_STORAGE['API_KEY'],
    api_secret=settings.CLOUDINARY_STORAGE['API_SECRET']
)

try:
    # Buscar archivos que empiecen con 'nivel_'
    result = cloudinary.api.resources(max_results=50)
    nivel_files = [r for r in result['resources'] if 'nivel_' in r['public_id']]
    print(f'Archivos con "nivel_" encontrados: {len(nivel_files)}')
    for r in nivel_files:
        print(f'  - {r["public_id"]} ({r["format"]}) - {r["bytes"]} bytes')

    # Buscar en carpeta globaled
    try:
        globaled_result = cloudinary.api.resources(prefix='globaled', max_results=50)
        print(f'\nArchivos en carpeta globaled: {len(globaled_result["resources"])}')
        for r in globaled_result['resources']:
            print(f'  - {r["public_id"]} ({r["format"]}) - {r["bytes"]} bytes')
    except Exception as e:
        print(f'Error buscando en globaled: {e}')

except Exception as e:
    print(f'Error: {e}')