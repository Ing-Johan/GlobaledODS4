#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corregir encoding de todos los contenidos en BD
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from competencias.models import Contenido

# Datos correctos en UTF-8
CONTENIDOS_CORRECTOS = {
    1: {
        "titulo": "¿Cómo contamos los números?",
        "cuerpo": """Los números nos ayudan a contar cosas del mundo. El 1 es uno, el 2 son dos, y así hasta el 20 y más.

Cuando contamos, seguimos un orden: 1, 2, 3, 4, 5... Cada número vale más que el anterior.

Los números también nos dicen cuántos objetos hay en un grupo. Si tienes 3 manzanas y te dan 2 más, ahora tienes 5.

**Características de los números:**
- Cada número es diferente
- El orden siempre es el mismo: 1 antes que 2, 2 antes que 3...
- Los números mayores están a la derecha
- Podemos contar con los dedos, objetos o solo con nuestra mente""",
        "ejemplo": "Imagina que tienes 7 canicas. Tu amigo te da 4 más. Para saber cuántas tienes en total, cuentas: 8, 9, 10, 11. ¡Tienes 11 canicas!",
        "tip": "Usa tus dedos para contar cuando empieces. ¡Es una herramienta que siempre tienes contigo!",
        "actividades": """<ol>
<li><strong>Contar objetos:</strong> Toma objetos de tu casa (botones, monedas, clips) y cuéntalos. Anota el número.</li>
<li><strong>Escribir números:</strong> Escribe los números del 1 al 20 en un papel. Después, cúbrelos y escríbelos de memoria.</li>
<li><strong>Juego de posición:</strong> Pide a alguien que diga un número entre 1 y 10, y tú coloca ese número de objetos en la mesa.</li>
<li><strong>Orden correcto:</strong> Mezcla números del 1 al 10 escritos en papelitos y ordénalos de menor a mayor.</li>
</ol>""",
        "faq": """<strong>¿Por qué el 0 es importante?</strong> El 0 significa "nada", "ninguno". Después viene el 1. Sin el 0, los números no funcionarían bien.<br><br>
<strong>¿Qué pasa después del 9?</strong> Después del 9 viene el 10, que es dos dígitos (1 y 0). Es como comenzar un nuevo grupo.<br><br>
<strong>¿Para qué sirven los números?</strong> Los usamos para contar, para decir la edad, la hora, el precio... ¡En todas partes!"""
    },
    6: {
        "titulo": "¿Qué es la idea principal?",
        "cuerpo": """Todo texto tiene una idea principal: el mensaje más importante que el autor quiere transmitir.

Para encontrarla, pregúntate: ¿De qué trata principalmente este texto? Las demás ideas apoyan o explican la idea principal, pero son secundarias.

Generalmente la idea principal aparece al inicio o al final del texto.

**Pistas para encontrar la idea principal:**

- Mira el título
- Lee el primer párrafo
- Pregúntate: ¿Si solo pudiera leer una oración, cuál sería?""",
        "ejemplo": "En un texto que dice 'Los pájaros vuelan alto porque tienen alas especiales. Las alas les permiten moverse por el aire.' La idea principal es que los pájaros vuelan porque tienen alas especiales.",
        "tip": "La idea principal suele estar en el primer o último párrafo. ¡Léelos con atención!",
        "actividades": """<ol>
<li><strong>Subraya:</strong> Lee un párrafo y subraya la oración que creas que es la idea principal.</li>
<li><strong>Resume:</strong> Lee un texto corto y cuéntalo en una sola frase.</li>
<li><strong>Títulos nuevos:</strong> Lee textos y crea títulos que reflejen la idea principal.</li>
<li><strong>Comparación:</strong> Lee dos textos sobre el mismo tema. ¿Cuál es la idea principal en cada uno?</li>
</ol>""",
        "faq": """<strong>¿Cuál es la diferencia entre idea principal e ideas secundarias?</strong> La principal es lo más importante. Las secundarias dan detalles que la apoyan.<br><br>
<strong>¿Todos los párrafos tienen una idea principal?</strong> Sí. Cada párrafo tiene una idea principal, aunque sea pequeña.<br><br>
<strong>¿Cómo sé si encontré la idea principal?</strong> Si eliminas las otras oraciones, ¿el párrafo sigue teniendo sentido? Entonces encontraste la principal."""
    },
    11: {
        "titulo": "¿Cómo convivimos juntos?",
        "cuerpo": """Convivencia significa vivir juntos en armonía. En la escuela, el barrio, la familia... necesitamos convivir.

La convivencia se construye con respeto. Respetar significa valorar a los otros, aceptar sus diferencias y seguir reglas que nos protegen a todos.

Las normas existen para que todos estemos seguros. Cuando todos seguimos las reglas, la convivencia es mejor.

**Elementos de la convivencia:**
- Respeto por los demás
- Escuchar a otros
- Cumplir normas
- Resolver conflictos sin violencia
- Ayudar cuando alguien lo necesita""",
        "ejemplo": "En tu aula, si todos hablan a la vez, nadie se entiende. Pero si levantan la mano y hablan por turnos, todos escuchan y aprenden mejor.",
        "tip": "La convivencia es responsabilidad de todos. Tu comportamiento afecta a los demás.",
        "actividades": """<ol>
<li><strong>Reglas del aula:</strong> Crea con tu clase las reglas que todos deben seguir.</li>
<li><strong>Respeto:</strong> ¿Cómo mostrarías respeto a un compañero diferente a ti?</li>
<li><strong>Conflictos:</strong> ¿Cómo resolverías una pelea sin violencia?</li>
<li><strong>Comunidad:</strong> ¿Qué acciones mejoran la convivencia en tu escuela?</li>
</ol>""",
        "faq": """<strong>¿Qué hago si alguien no sigue las normas?</strong> Cuéntale a un adulto. No es chismo, es proteger la convivencia.<br><br>
<strong>¿Debo ser amigo de todos?</strong> No necesariamente. Pero sí debes respetar a todos.<br><br>
<strong>¿Qué es violencia en la convivencia?</strong> Pegar, insultar, excluir, acosar. Cualquier cosa que dañe a otros."""
    },
    16: {
        "titulo": "¿Qué es un ser vivo?",
        "cuerpo": """Los seres vivos nacen, crecen, se reproducen y mueren. Necesitan alimento, agua y aire para existir.

Hay dos grandes grupos: animales y plantas. Los animales se mueven y obtienen su alimento. Las plantas crean su propio alimento usando el sol.

Tanto animales como plantas son importantes para mantener el equilibrio de la naturaleza.

**Características de los seres vivos:**
- Nacen o germinan
- Crecen
- Se alimentan
- Se reproducen
- Responden a cambios del ambiente
- Mueren""",
        "ejemplo": "Un perro es un ser vivo: nace (es un cachorro), crece, come y bebe, puede tener crías y eventualmente muere.",
        "tip": "Todos los seres vivos, grandes o pequeños, tienen el mismo derecho a vivir.",
        "actividades": """<ol>
<li><strong>Observa:</strong> Observa un insecto, una planta y un animal. ¿Qué características vivas ves en cada uno?</li>
<li><strong>Crecimiento:</strong> Planta una semilla y registra su crecimiento cada día durante 2 semanas.</li>
<li><strong>Ciclo de vida:</strong> Dibuja el ciclo de vida de un animal (nacimiento, crecimiento, reproducción, muerte).</li>
<li><strong>Hábitat:</strong> ¿Dónde viven los seres vivos? Investiga sobre el hábitat de 3 animales diferentes.</li>
</ol>""",
        "faq": """<strong>¿Las plantas son seres vivos?</strong> Sí. Nacen, crecen, se alimentan, se reproducen y mueren.<br><br>
<strong>¿Los virus son seres vivos?</strong> Es complicado. Tienen características de seres vivos pero no pueden reproducirse solos.<br><br>
<strong>¿Por qué es importante cuidar los seres vivos?</strong> Porque sin ellos no tendríamos aire, comida ni un planeta sano."""
    }
}

print("Corrigiendo contenidos en BD...")
contador = 0

for nivel_id, datos in CONTENIDOS_CORRECTOS.items():
    try:
        c = Contenido.objects.get(nivel_id=nivel_id)
        c.titulo = datos["titulo"]
        c.cuerpo = datos["cuerpo"]
        c.ejemplo = datos["ejemplo"]
        c.tip = datos["tip"]
        c.actividades = datos["actividades"]
        c.faq = datos["faq"]
        c.save()
        print(f"✓ Nivel {nivel_id}: {c.titulo}")
        contador += 1
    except Contenido.DoesNotExist:
        print(f"✗ Nivel {nivel_id}: No existe")
    except Exception as e:
        print(f"✗ Nivel {nivel_id}: Error - {e}")

print(f"\n✓ COMPLETADO: {contador} contenidos corregidos")
