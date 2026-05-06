from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('competencias/', include('competencias.urls')),
]

# Servir archivos media en producción y en desarrollo.
# En Render esto permite que los videos dentro de media/ sean accesibles
# siempre que los archivos estén desplegados junto a la app.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)