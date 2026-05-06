import cloudinary
import cloudinary.api
from django.conf import settings
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

print('Configuración de Cloudinary:')
print(f'CLOUD_NAME: {settings.CLOUDINARY_STORAGE["CLOUD_NAME"]}')
print(f'API_KEY: {settings.CLOUDINARY_STORAGE["API_KEY"][:10]}...')
print(f'API_SECRET: {settings.CLOUDINARY_STORAGE["API_SECRET"][:10]}...')

# Configurar cloudinary con las credenciales
cloudinary.config(
    cloud_name=settings.CLOUDINARY_STORAGE["CLOUD_NAME"],
    api_key=settings.CLOUDINARY_STORAGE["API_KEY"],
    api_secret=settings.CLOUDINARY_STORAGE["API_SECRET"]
)

try:
    # Buscar todos los recursos, incluyendo videos
    result = cloudinary.api.resources(resource_type='video', max_results=50)
    print(f'\nVideos encontrados: {len(result["resources"])}')
    if result['resources']:
        print('Videos en Cloudinary:')
        for r in result['resources']:
            print(f'  - {r["public_id"]} ({r["format"]}) - {r["bytes"]} bytes')
    else:
        print('No hay videos en Cloudinary')

    # También buscar todos los recursos
    all_result = cloudinary.api.resources(max_results=50)
    print(f'\nTotal recursos encontrados: {len(all_result["resources"])}')

    # Buscar específicamente en la carpeta globaled
    try:
        folder_result = cloudinary.api.resources(prefix='globaled', max_results=50)
        print(f'Recursos en carpeta globaled: {len(folder_result["resources"])}')
        if folder_result['resources']:
            print('Archivos en globaled:')
            for r in folder_result['resources']:
                print(f'  - {r["public_id"]} ({r["format"]}) - {r["bytes"]} bytes')
    except:
        print('No se pudo buscar en carpeta globaled')

except Exception as e:
    print(f'\nError de conexión: {e}')
    print('Posibles causas:')
    print('- Credenciales incorrectas')
    print('- Problema de red')
    print('- Cuenta de Cloudinary no activa')