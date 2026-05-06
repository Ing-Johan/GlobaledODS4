import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cambia-esta-clave-en-produccion-123456'

DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "https://globaledods4.onrender.com"
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = ['https://globaledods4.onrender.com','*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'core',
    'competencias',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'globaled.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'globaled.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-co'
TIME_ZONE     = 'America/Bogota'
USE_I18N      = True
USE_TZ        = True

# ── ENCODING UTF-8 ──
DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'

STATIC_URL  = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "core" / "static"
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL   = '/media/'
MEDIA_ROOT  = BASE_DIR / 'media'

CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL', 'cloudinary://649355296422886:RTHChP8mCqRZmkt2FU1nmDawj8o@dysab8vmt')

# Configurar Cloudinary inmediatamente si hay URL
if CLOUDINARY_URL:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.VideoMediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'dysab8vmt',
        'API_KEY': '649355296422886',
        'API_SECRET': 'RTHChP8mCqRZmkt2FU1nmDawj8o',
        'MEDIA_TAGS': ['globaled'],
        'FOLDER': 'globaled',
    }
else:
    # Fallback a almacenamiento local
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Función para configurar storage después de que Django esté listo
def configure_cloudinary_storage():
    """Configura Cloudinary storage después de que Django esté inicializado"""
    if CLOUDINARY_URL:
        try:
            from django.core.files.storage import default_storage
            from cloudinary_storage.storage import VideoMediaCloudinaryStorage
            
            # Forzar el uso del storage de Cloudinary
            if not isinstance(default_storage._wrapped, VideoMediaCloudinaryStorage):
                default_storage._wrapped = VideoMediaCloudinaryStorage()
                print("✓ Cloudinary VideoMedia storage configurado correctamente")
        except Exception as e:
            print(f"✗ Error configurando Cloudinary storage: {e}")

# Configurar storage si Django ya está inicializado
import django
if django.apps.apps.ready:
    configure_cloudinary_storage()

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL           = '/login/'
LOGIN_REDIRECT_URL  = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'