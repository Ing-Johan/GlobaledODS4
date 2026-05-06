#!/usr/bin/env python3
"""
Script para descargar videos educativos de YouTube
Organizados por competencia y nivel
"""

import os
import json
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp no está instalado")
    exit(1)

# Configuración de videos a descargar
# Formato: (competencia, nivel, título, url_youtube)
VIDEOS = {
    'razonamiento': [
        (1, 'Números del 1 al 20 para niños', 'https://www.youtube.com/watch?v=xmwJhT5RJBg'),
        (2, 'Suma y Resta para Niños', 'https://www.youtube.com/watch?v=hmjgQpAiW74'),
        (3, 'Tablas de Multiplicar para Niños', 'https://www.youtube.com/watch?v=jPOlWHLJb-k'),
        (4, 'Fracciones para Niños', 'https://www.youtube.com/watch?v=H8aBNKHkrUc'),
        (5, 'Problemas de Matemáticas para Niños', 'https://www.youtube.com/watch?v=qrKNmIxBDIY'),
    ],
    'lectura': [
        (1, 'Comprensión Lectora para Niños', 'https://www.youtube.com/watch?v=XB5vWV7Qs4w'),
        (2, 'Vocabulario Nuevo para Niños', 'https://www.youtube.com/watch?v=d8JLyC5Pz5A'),
        (3, 'Hechos y Opiniones en Lectura', 'https://www.youtube.com/watch?v=Xzl1bGlJxAE'),
        (4, 'Lectura Entre Líneas para Niños', 'https://www.youtube.com/watch?v=EfaVBkB7B-I'),
        (5, 'Tipos de Textos para Niños', 'https://www.youtube.com/watch?v=XGPV7rvfqWo'),
    ],
    'ciudadana': [
        (1, 'Vivir en Comunidad para Niños', 'https://www.youtube.com/watch?v=h-hRgAU0GyY'),
        (2, 'Derechos y Deberes de los Niños', 'https://www.youtube.com/watch?v=dI6LUstGdME'),
        (3, 'Resolución de Conflictos para Niños', 'https://www.youtube.com/watch?v=g13sZFBqNQY'),
        (4, 'Participación Ciudadana para Niños', 'https://www.youtube.com/watch?v=gE8-3C0ySWc'),
        (5, 'Diversidad e Inclusión para Niños', 'https://www.youtube.com/watch?v=yWGLDcEEzDc'),
    ],
    'ciencias': [
        (1, 'Seres Vivos para Niños', 'https://www.youtube.com/watch?v=rKJkEVhqHkI'),
        (2, 'El Cuerpo Humano para Niños', 'https://www.youtube.com/watch?v=a0L8H1Dxo0c'),
        (3, 'Cuidado del Medio Ambiente', 'https://www.youtube.com/watch?v=hhYLHpqJCKM'),
        (4, 'Estados de la Materia para Niños', 'https://www.youtube.com/watch?v=E7kTYpbvJFE'),
        (5, 'Sistema Solar para Niños', 'https://www.youtube.com/watch?v=wMq-WdIb4hc'),
    ],
}

def descargar_video(competencia, nivel, titulo, url, directorio_salida):
    """Descarga un video de YouTube en MP4"""
    
    archivo_salida = f"{directorio_salida}/nivel_{nivel}.mp4"
    
    # Si ya existe, saltarlo
    if os.path.exists(archivo_salida):
        print(f"✓ {competencia.upper()} Nivel {nivel}: Ya existe")
        return True
    
    try:
        print(f"⏳ {competencia.upper()} Nivel {nivel}: Descargando '{titulo}'...")
        
        ydl_opts = {
            'format': 'best[ext=mp4]/best',
            'outtmpl': archivo_salida.replace('.mp4', ''),
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 60,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"✓ {competencia.upper()} Nivel {nivel}: ¡Descargado!")
        return True
            
    except Exception as e:
        print(f"✗ {competencia.upper()} Nivel {nivel}: {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("DESCARGA DE VIDEOS EDUCATIVOS - GlobalEd")
    print("="*60 + "\n")
    
    directorio_base = Path('media/videos')
    directorio_base.mkdir(parents=True, exist_ok=True)
    
    total_videos = sum(len(v) for v in VIDEOS.values())
    descargados = 0
    
    for competencia, videos_list in VIDEOS.items():
        directorio_comp = directorio_base / competencia
        directorio_comp.mkdir(parents=True, exist_ok=True)
        
        for nivel, titulo, url in videos_list:
            if descargar_video(competencia, nivel, titulo, url, str(directorio_comp)):
                descargados += 1
    
    print("\n" + "="*60)
    print(f"RESUMEN: {descargados}/{total_videos} videos descargados")
    print("="*60 + "\n")
    
    if descargados == total_videos:
        print("✓ ¡Todos los videos están listos!")
    else:
        print(f"⚠ Faltaron {total_videos - descargados} videos")

if __name__ == '__main__':
    main()
