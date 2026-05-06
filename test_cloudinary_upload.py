import os
import django
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

print('Probando subida simple a Cloudinary...')

try:
    # Crear un archivo de prueba simple
    test_content = b'Este es un archivo de prueba'
    test_file = ContentFile(test_content, name='test_file.txt')

    # Intentar guardarlo
    saved_path = default_storage.save('test_cloudinary.txt', test_file)
    print(f'✓ Archivo guardado en: {saved_path}')

    # Generar URL
    file_url = default_storage.url(saved_path)
    print(f'✓ URL generada: {file_url}')

    print('Cloudinary está funcionando correctamente!')

except Exception as e:
    print(f'✗ Error: {e}')
    print('Cloudinary no está configurado correctamente')