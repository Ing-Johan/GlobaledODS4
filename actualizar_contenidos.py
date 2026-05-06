#!/usr/bin/env python3
"""
Script para actualizar contenidos en la base de datos
Ejecutar: python manage.py shell < actualizar_contenidos.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from competencias.models import Contenido, Nivel

# Datos expandidos por nivel
CONTENIDOS_ACTUALIZAR = {
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
    2: {
        "titulo": "Sumar y restar: fácil y divertido",
        "cuerpo": """Sumar significa juntar grupos de cosas. Cuando sumas 4 + 3, estás juntando 4 objetos con 3 más para obtener 7.

Restar significa quitar. Si tienes 10 galletas y te comes 4, te quedan 6. Eso es 10 - 4 = 6.

Siempre puedes comprobar tu resta sumando: si 10 - 4 = 6, entonces 6 + 4 debe dar 10.

**La suma y la resta son inversas:**
- Sumar suma más cosas
- Restar quita cosas
- Juntos, mantienen el equilibrio""",
        "ejemplo": "En la tienda hay 15 mangos. Se venden 8. ¿Cuántos quedan? 15 - 8 = 7 mangos quedan en la tienda.",
        "tip": "Para restar números grandes, primero resta las unidades y luego las decenas.",
        "actividades": """<ol>
<li><strong>Suma con objetos:</strong> Toma 3 monedas en una mano y 4 en la otra. Junta todas. ¿Cuántas son? 3 + 4 = 7</li>
<li><strong>Resta en la tienda:</strong> Imagina que tienes $50. Si compras un chocolate por $15, ¿cuánto te sobra?</li>
<li><strong>Historias matemáticas:</strong> Inventa problemas: "Tenía 12 caramelos. Le regalé 5 a mi amigo. ¿Cuántos tengo?"</li>
<li><strong>Comprobación:</strong> Haz una suma: 7 + 5 = 12. Ahora comprueba restando: 12 - 5 = ¿da 7?</li>
</ol>""",
        "faq": """<strong>¿Cuál es la diferencia entre suma y resta?</strong> La suma añade más cosas. La resta quita cosas.<br><br>
<strong>¿Cómo sé si debo sumar o restar?</strong> Lee bien el problema. Si dice "en total", "juntos" o "más" = suma. Si dice "quedó", "sobrante" o "menos" = resta.<br><br>
<strong>¿Puede haber un resultado negativo?</strong> No en primaria. Solo restamos cuando podemos, por ejemplo, no podemos restar 10 - 15 porque no tenemos 15 cosas."""
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
        "ejemplo": "Texto: 'Los perros son animales muy leales. Cuidan la casa, acompañan a sus dueños y pueden aprender muchos trucos.' Idea principal: Los perros son animales muy leales y útiles.",
        "tip": "Si puedes resumir el texto en una sola oración, ¡encontraste la idea principal!",
        "actividades": """<ol>
<li><strong>Lee y resume:</strong> Lee un párrafo corto. Resúmelo en una sola oración.</li>
<li><strong>Títulos creativos:</strong> Lee textos y crea un título que represente la idea principal.</li>
<li><strong>Busca en noticias:</strong> Lee un titular de noticias. ¿Cuál es la idea principal?</li>
<li><strong>Juego de preguntas:</strong> Lee un texto y pregúntate: ¿De qué trata? Esa es la idea principal.</li>
</ol>""",
        "faq": """<strong>¿La idea principal siempre está al inicio?</strong> No siempre. Puede estar al inicio, en el medio o al final. Lee todo el texto.<br><br>
<strong>¿Cuántas ideas principales hay por texto?</strong> Generalmente UNA sola idea principal. Las otras son ideas de apoyo.<br><br>
<strong>¿Cómo diferencia idea principal de detalles?</strong> La idea principal es el tema general. Los detalles son ejemplos que la explican."""
    },
    11: {
        "titulo": "¿Qué es vivir en comunidad?",
        "cuerpo": """Una comunidad es un grupo de personas que viven juntas en un lugar y comparten normas, espacios y responsabilidades.

Para vivir bien en comunidad necesitamos: respeto, comunicación, solidaridad y cumplir las normas.

Cada persona tiene un papel en la comunidad: estudiantes, familias, maestros, vecinos... todos somos importantes.

**Características de una buena comunidad:**
- Las personas se respetan
- Hay reglas que todos siguen
- Nos ayudamos unos a otros
- Compartimos espacios comunes""",
        "ejemplo": "En tu salón de clases hay normas: levantar la mano para hablar, no interrumpir, respetar los materiales. Esas normas hacen que todos puedan aprender.",
        "tip": "La convivencia empieza con acciones pequeñas: saludar, escuchar y ayudar a quien lo necesita.",
        "actividades": """<ol>
<li><strong>Reglas del salón:</strong> Crea 3-4 reglas importantes para tu clase. Escríbelas y cumplelas.</li>
<li><strong>Mi comunidad:</strong> Dibuja tu barrio y marca lugares donde la gente se reúne.</li>
<li><strong>Ayuda a otros:</strong> Haz una lista de formas en que puedes ayudar en tu comunidad.</li>
<li><strong>Ejemplo de respeto:</strong> Cuéntale a alguien qué significa para ti vivir con respeto.</li>
</ol>""",
        "faq": """<strong>¿Solo mi escuela es una comunidad?</strong> No. Tu casa, barrio, ciudad y país son también comunidades.<br><br>
<strong>¿Qué pasa si alguien no respeta las normas?</strong> Hay consecuencias, pero el objetivo es ayudar a que entienda por qué la norma existe.<br><br>
<strong>¿Todos tienen que pensar igual en la comunidad?</strong> No. Podemos pensar diferente pero respetarnos mutuamente."""
    },
    16: {
        "titulo": "¿Qué es un ser vivo?",
        "cuerpo": """Los seres vivos nacen, crecen, se reproducen y mueren. Necesitan alimento, agua y aire para existir.

Hay dos grandes grupos: animales y plantas. Los animales se mueven y obtienen su alimento. Las plantas fabrican su alimento con la luz del sol.

También existen los hongos, las bacterias y otros microorganismos que son seres vivos muy pequeños.

**Características de los seres vivos:**
- Nacen o germinan
- Crecen
- Se reproducen
- Respiran
- Se mueven (los animales)
- Mueren""",
        "ejemplo": "Un perro nace, crece, tiene cachorros y muere. Una piedra no hace nada de eso: no es un ser vivo.",
        "tip": "Para recordar las características de los seres vivos: N-C-R-M (Nacen, Crecen, se Reproducen, Mueren).",
        "actividades": """<ol>
<li><strong>Vivo o no vivo:</strong> Haz una lista de cosas: ¿cuáles son vivas? ¿cuáles no?</li>
<li><strong>Observa el cambio:</strong> Planta una semilla. Observa cómo crece cada semana.</li>
<li><strong>El ciclo de vida:</strong> Dibuja las etapas de vida de un animal que conozcas.</li>
<li><strong>Búsqueda en la naturaleza:</strong> Sal al parque o jardín. ¿Cuántos seres vivos puedes encontrar?</li>
</ol>""",
        "faq": """<strong>¿Las plantas respiran?</strong> Sí, pero no como los animales. Respiran mediante la fotosíntesis usando luz solar.<br><br>
<strong>¿Las bacterias son seres vivos?</strong> Sí, aunque son tan pequeñas que no las vemos. Necesitamos un microscopio.<br><br>
<strong>¿Qué es la reproducción?</strong> Es cuando un ser vivo crea otros seres iguales. Puede ser por huevos, crías vivas, semillas, etc."""
    }
}

def actualizar_contenidos():
    """Actualiza los contenidos en la BD"""
    
    print("\n" + "="*70)
    print("ACTUALIZAR CONTENIDOS PEDAGÓGICOS - GlobalEd")
    print("="*70 + "\n")
    
    actualizados = 0
    errores = 0
    
    for nivel_id, datos in CONTENIDOS_ACTUALIZAR.items():
        try:
            contenido = Contenido.objects.get(nivel_id=nivel_id)
            
            # Actualizar campos
            contenido.titulo = datos["titulo"]
            contenido.cuerpo = datos["cuerpo"]
            contenido.ejemplo = datos["ejemplo"]
            contenido.tip = datos["tip"]
            contenido.actividades = datos["actividades"]
            contenido.faq = datos["faq"]
            contenido.save()
            
            print(f"✓ Nivel {nivel_id}: Actualizado - {datos['titulo']}")
            actualizados += 1
            
        except Contenido.DoesNotExist:
            print(f"✗ Nivel {nivel_id}: No encontrado")
            errores += 1
        except Exception as e:
            print(f"✗ Nivel {nivel_id}: Error - {str(e)}")
            errores += 1
    
    print("\n" + "="*70)
    print(f"RESUMEN: {actualizados} actualizados, {errores} errores")
    print("="*70 + "\n")

if __name__ == '__main__':
    actualizar_contenidos()
