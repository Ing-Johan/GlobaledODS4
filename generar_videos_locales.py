#!/usr/bin/env python3
"""
Generar videos educativos locales con PIL + imageio
"""

import os
import django
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

os.environ['DJANGO_SETTINGS_MODULE'] = 'globaled.settings'
django.setup()

from competencias.models import Contenido, Nivel

try:
    import imageio
    import numpy as np
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

VIDEO_INFO = {
    1: ("🔢 Números del 1 al 20", "Aprendemos a contar números"),
    2: ("➕ Suma y Resta", "Juntamos y quitamos números"),
    3: ("✖️ Multiplicación", "Sumamos rápido grupos iguales"),
    4: ("📊 Fracciones", "Dividimos en partes iguales"),
    5: ("🧮 Problemas Reales", "Matemáticas en la vida"),
    6: ("📖 Idea Principal", "El mensaje más importante"),
    7: ("👤 Autor y Sentimiento", "¿Qué siente quién escribe?"),
    8: ("📝 Hechos vs Opiniones", "Lo comprobable vs lo personal"),
    9: ("🔍 Entre Líneas", "Lo que no está escrito"),
    10: ("📰 Textos Cotidianos", "Avisos, recetas, noticias"),
    11: ("🤝 Vivir en Comunidad", "Juntos con respeto"),
    12: ("⚖️ Derechos y Deberes", "Lo que tengo y debo hacer"),
    13: ("☮️ Resolver Conflictos", "Soluciones sin violencia"),
    14: ("🗳️ Participación", "Decidimos juntos"),
    15: ("🌈 Diversidad", "Diferentes y valiosos"),
    16: ("🌱 Seres Vivos", "Nacen, crecen, mueren"),
    17: ("❤️ Cuerpo Humano", "Sistemas que nos mantienen"),
    18: ("🌍 Medio Ambiente", "Cuidemos el planeta"),
    19: ("⚛️ Estados de la Materia", "Sólido, líquido, gaseoso"),
    20: ("🪐 Sistema Solar", "El Sol y los planetas"),
}

COMPETENCIAS = {
    (1, 5): ('razonamiento', 'Razonamiento'),
    (6, 10): ('lectura', 'Lectura'),
    (11, 15): ('ciudadana', 'Ciudadana'),
    (16, 20): ('ciencias', 'Ciencias'),
}

def obtener_carpeta(nivel_id):
    """Obtiene la carpeta de competencia para un nivel"""
    for rango, (folder, _) in COMPETENCIAS.items():
        if rango[0] <= nivel_id <= rango[1]:
            return folder
    return 'otros'

def crear_video(titulo, subtitulo, archivo_salida, duracion=3):
    """Crea un video MP4 simple con PIL + imageio"""
    
    if os.path.exists(archivo_salida):
        print(f"  ✓ Ya existe: {os.path.basename(archivo_salida)}")
        return True
    
    try:
        # Crear carpeta si no existe
        Path(archivo_salida).parent.mkdir(parents=True, exist_ok=True)
        
        # Parámetros del video
        fps = 24
        frames = fps * duracion
        width, height = 1280, 720
        
        # Crear lista de frames
        frames_list = []
        
        for frame_idx in range(frames):
            # Crear imagen
            img = Image.new('RGB', (width, height), color=(21, 101, 192))  # Azul
            draw = ImageDraw.Draw(img)
            
            # Intentar usar Arial, si no existe usar default
            try:
                font_big = ImageFont.truetype("arial.ttf", 80)
                font_small = ImageFont.truetype("arial.ttf", 50)
            except:
                font_big = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            # Dibujar títulos
            title_y = height // 3
            bbox = draw.textbbox((0, 0), titulo, font=font_big)
            title_width = bbox[2] - bbox[0]
            draw.text(
                ((width - title_width) // 2, title_y),
                titulo,
                fill=(255, 255, 255),
                font=font_big
            )
            
            subtitle_y = 2 * height // 3
            bbox_sub = draw.textbbox((0, 0), subtitulo, font=font_small)
            sub_width = bbox_sub[2] - bbox_sub[0]
            draw.text(
                ((width - sub_width) // 2, subtitle_y),
                subtitulo,
                fill=(255, 255, 200),
                font=font_small
            )
            
            # Convertir a array
            frame_array = np.array(img)
            frames_list.append(frame_array)
        
        # Guardar video con imageio
        import imageio
        imageio.mimwrite(archivo_salida, frames_list, fps=fps)
        
        tamaño = os.path.getsize(archivo_salida) / 1024 / 1024
        print(f"  ✓ Creado: {os.path.basename(archivo_salida)} ({tamaño:.1f} MB)")
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:80]}")
        return False

def main():
    print("\n" + "="*70)
    print("CREAR VIDEOS LOCALES - GlobalEd")
    print("="*70 + "\n")
    
    creados = 0
    total = len(VIDEO_INFO)
    
    for nivel_id, (titulo, subtitulo) in VIDEO_INFO.items():
        carpeta = obtener_carpeta(nivel_id)
        video_dir = Path('media/videos') / carpeta
        video_dir.mkdir(parents=True, exist_ok=True)
        
        archivo = video_dir / f'nivel_{nivel_id}.mp4'
        
        if crear_video(titulo, subtitulo, str(archivo), duracion=3):
            creados += 1
            
            # Guardar ruta relativa en BD
            try:
                contenido = Contenido.objects.get(nivel_id=nivel_id)
                ruta_relativa = f'videos/{carpeta}/nivel_{nivel_id}.mp4'
                contenido.video_file = ruta_relativa
                contenido.save()
                print(f"    → BD actualizada: {ruta_relativa}\n")
            except Exception as e:
                print(f"    ⚠ BD no actualizada: {e}\n")
    
    print("="*70)
    print(f"RESUMEN: {creados}/{total} videos creados")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
