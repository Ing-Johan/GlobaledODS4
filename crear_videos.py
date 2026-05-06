#!/usr/bin/env python3
"""
Crear videos de demostración educativa para GlobalEd
Genera videos MP4 pequeños para cada nivel
"""

import os
import subprocess
from pathlib import Path
from textwrap import dedent

# Títulos y textos para cada nivel
VIDEOS_INFO = {
    'razonamiento': [
        (1, 'Números del 1 al 20', 'Aprendiendo números: 1, 2, 3... 20'),
        (2, 'Suma y Resta', 'Sumamos: 5 + 3 = 8. Restamos: 8 - 3 = 5'),
        (3, 'Multiplicación', 'La multiplicación es sumar rápido: 3 × 4 = 12'),
        (4, 'Fracciones', 'Una fracción divide un todo en partes iguales'),
        (5, 'Problemas', 'Usando matemáticas para resolver situaciones reales'),
    ],
    'lectura': [
        (1, 'Idea Principal', 'El mensaje más importante del texto'),
        (2, 'Palabras Nuevas', 'Aprendiendo vocabulario del contexto'),
        (3, 'Hechos vs Opiniones', 'Distinguiendo lo que es verificable'),
        (4, 'Lectura Entre Líneas', 'Entendiendo lo que no dice el texto'),
        (5, 'Textos Cotidianos', 'Leyendo avisos, recetas y noticias'),
    ],
    'ciudadana': [
        (1, 'Convivencia', 'Vivir juntos con respeto y normas'),
        (2, 'Derechos y Deberes', 'Todo niño tiene derechos y responsabilidades'),
        (3, 'Conflictos', 'Resolviendo desacuerdos de forma pacífica'),
        (4, 'Participación', 'Todos podemos participar en decisiones'),
        (5, 'Diversidad', 'Respetando nuestras diferencias'),
    ],
    'ciencias': [
        (1, 'Seres Vivos', 'Los seres vivos nacen, crecen y se reproducen'),
        (2, 'Cuerpo Humano', 'Nuestros órganos y sistemas nos mantienen vivos'),
        (3, 'Medio Ambiente', 'Cuidando el planeta para todos'),
        (4, 'Materia', 'Estados: sólido, líquido y gaseoso'),
        (5, 'Universo', 'El sistema solar y el espacio infinito'),
    ],
}

def crear_video(titulo, subtitulo, archivo_salida):
    """Crea un video de demostración MP4 con ffmpeg"""
    
    if os.path.exists(archivo_salida):
        print(f"  ✓ Ya existe: {os.path.basename(archivo_salida)}")
        return True
    
    try:
        # Comando ffmpeg para crear video simple de 3 segundos
        # Con fondo de color, texto y duración
        cmd = [
            'ffmpeg',
            '-f', 'lavfi',
            '-i', 'color=c=blue:s=1280x720:d=3',
            '-vf', f"drawtext=text='{titulo}':fontsize=60:fontcolor=white:x=(w-text_w)/2:y=h/3," + \
                   f"drawtext=text='{subtitulo}':fontsize=40:fontcolor=lightyellow:x=(w-text_w)/2:y=2*h/3",
            '-pix_fmt', 'yuv420p',
            '-c:v', 'libx264',
            '-preset', 'ultrafast',
            archivo_salida,
            '-y',
            '-loglevel', 'error',
        ]
        
        result = subprocess.run(cmd, capture_output=True, timeout=30)
        
        if result.returncode == 0:
            tamaño = os.path.getsize(archivo_salida) / 1024  # KB
            print(f"  ✓ Creado: {os.path.basename(archivo_salida)} ({tamaño:.1f} KB)")
            return True
        else:
            print(f"  ✗ Error: {result.stderr.decode()[:100]}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"  ✗ Timeout al crear video")
        return False
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:100]}")
        return False

def main():
    print("\n" + "="*70)
    print("CREAR VIDEOS DE DEMOSTRACIÓN - GlobalEd")
    print("="*70 + "\n")
    
    base_dir = Path('media/videos')
    base_dir.mkdir(parents=True, exist_ok=True)
    
    total = 0
    creados = 0
    
    for competencia, videos in VIDEOS_INFO.items():
        comp_dir = base_dir / competencia
        comp_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n{competencia.upper()}:")
        
        for nivel, titulo, subtitulo in videos:
            total += 1
            archivo = comp_dir / f'nivel_{nivel}.mp4'
            
            if crear_video(titulo, subtitulo, str(archivo)):
                creados += 1
    
    print("\n" + "="*70)
    print(f"RESUMEN: {creados}/{total} videos creados")
    print("="*70)
    print("\n✓ Videos listos en: media/videos/")
    print("✓ Estructura preparada para descargar videos de YouTube después\n")

if __name__ == '__main__':
    main()
