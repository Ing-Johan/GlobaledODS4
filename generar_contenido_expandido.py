#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expander contenido educativo para GlobalEd
Genera fixture JSON con contenido pedagógico completo
"""

import json
from pathlib import Path

CONTENIDO_EXPANDIDO = {
    "razonamiento": [
        {
            "nivel": 1,
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
        {
            "nivel": 2,
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
        }
    ],
    "lectura": [
        {
            "nivel": 1,
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
        {
            "nivel": 2,
            "titulo": "Adivina el significado",
            "cuerpo": """Cuando encuentras una palabra que no conoces, no te preocupes. El contexto (las palabras a su alrededor) te da pistas sobre su significado.

Lee la oración completa y observa: ¿Qué tipo de palabra es? ¿Sustantivo, verbo, adjetivo? ¿Qué sentido tiene la oración?

También puedes buscar si la palabra tiene partes que reconoces (prefijos o raíces).

**Estrategias para descubrir significados:**
- Lee la frase completa
- Mira las imágenes si hay
- Piensa en palabras parecidas
- Pide ayuda si es necesario""",
            "ejemplo": "'El niño estaba muy alborozado cuando vio sus regalos.' Alborozado: el niño estaba así al ver algo bueno → significa muy feliz o emocionado.",
            "tip": "Cuando leas un libro, anota las palabras nuevas y busca su significado. Tu vocabulario crecerá cada día.",
            "actividades": """<ol>
<li><strong>Adivina la palabra:</strong> El maestro da pistas. Tú adivinas qué palabra es.</li>
<li><strong>Oraciones incompletas:</strong> Lee: "Era un día muy ___ (alegre). Los niños jugaban y reían." ¿Qué palabra falta?</li>
<li><strong>Categorías:</strong> Agrupa palabras por tema: frutas, animales, colores.</li>
<li><strong>Mi diccionario:</strong> Crea un cuaderno con palabras nuevas y sus significados.</li>
</ol>""",
            "faq": """<strong>¿Necesito memorizar todas las palabras nuevas?</strong> No. Es mejor entender el contexto y poco a poco las aprenderás.<br><br>
<strong>¿Puedo usar el diccionario siempre?</strong> Sí, pero primero intenta adivinar del contexto. Después confirma en el diccionario.<br><br>
<strong>¿Cuántas palabras nuevas debo aprender?</strong> Aprende las palabras que uses frecuentemente. No todas son igualmente importantes."""
        }
    ],
    "ciudadana": [
        {
            "nivel": 1,
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
        {
            "nivel": 2,
            "titulo": "Derechos y deberes de los niños",
            "cuerpo": """Todos los niños del mundo tienen derechos fundamentales, reconocidos por la ONU en 1989.

Algunos derechos: educación, salud, familia, juego, protección y participación.

Pero también tenemos deberes: respetar a los demás, cuidar el ambiente, estudiar y obedecer las normas del hogar y la escuela.

**Derechos importantes:**
- Derecho a vivir con una familia
- Derecho a la salud
- Derecho a la educación
- Derecho a jugar
- Derecho a la protección""",
            "ejemplo": "Tienes derecho a estudiar, y tu deber es asistir a clases y esforzarte. Tienes derecho a jugar, y tu deber es respetar el turno de otros.",
            "tip": "Los derechos y deberes van de la mano. Cuando respetas los derechos de otros, también proteges los tuyos.",
            "actividades": """<ol>
<li><strong>Mis derechos y deberes:</strong> Haz dos listas: una de derechos, otra de deberes.</li>
<li><strong>Historias de derechos:</strong> Lee historias donde se respetan o se violan derechos.</li>
<li><strong>Responsabilidad:</strong> Identifica un deber que cumlas bien y otro que necesitas mejorar.</li>
<li><strong>Campaña de conciencia:</strong> Crea un afiche sobre los derechos de los niños.</li>
</ol>""",
            "faq": """<strong>¿Todos los niños del mundo tienen los mismos derechos?</strong> Sí, según la ONU. Pero algunos países aún no los cumplen completamente.<br><br>
<strong>¿Qué pasa si alguien viola mis derechos?</strong> Puedes decirle a un adulto de confianza: papás, maestro o policía.<br><br>
<strong>¿Tengo más derechos que deberes?</strong> Deben estar equilibrados. Más derechos significan más responsabilidad."""
        }
    ],
    "ciencias": [
        {
            "nivel": 1,
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
        },
        {
            "nivel": 2,
            "titulo": "Nuestro cuerpo por dentro",
            "cuerpo": """El cuerpo humano tiene sistemas que trabajan juntos para mantenernos vivos.

El sistema digestivo procesa los alimentos. El sistema respiratorio lleva oxígeno a las células. El sistema circulatorio transporta la sangre. El sistema nervioso controla todo el cuerpo.

Cuidar el cuerpo con buena alimentación, ejercicio y descanso es esencial.

**Sistemas importantes:**
- Sistema digestivo: descompone comida
- Sistema respiratorio: trae oxígeno
- Sistema circulatorio: transporta sangre
- Sistema óseo: sostiene tu cuerpo
- Sistema muscular: te permite moverte""",
            "ejemplo": "Cuando corres, tu corazón late más rápido para enviar más sangre y oxígeno a tus músculos. ¡Tu cuerpo es inteligente!",
            "tip": "Toma agua durante el día, duerme 8-10 horas y mueve tu cuerpo. Así tus sistemas funcionarán bien.",
            "actividades": """<ol>
<li><strong>Palpa tu cuerpo:</strong> Siente tu corazón, pulso, músculos. ¿Cómo están?</li>
<li><strong>El viaje del alimento:</strong> Traza el camino que hace la comida desde tu boca al estómago.</li>
<li><strong>Hábitos saludables:</strong> Anota 5 cosas que haces para cuidar tu cuerpo.</li>
<li><strong>Respiración profunda:</strong> Respira profundamente 10 veces. ¿Cómo te sientes?</li>
</ol>""",
            "faq": """<strong>¿Por qué necesitamos oxígeno?</strong> Las células de nuestro cuerpo lo necesitan para funcionar y producir energía.<br><br>
<strong>¿Por qué el corazón late rápido al correr?</strong> Necesita bombear más sangre para llevar oxígeno a los músculos que trabajan.<br><br>
<strong>¿Cuántos huesos tengo?</strong> Los adultos tenemos 206 huesos. Los bebés nacen con más, pero algunos se fusionan."""
        }
    ]
}

def generar_fixture():
    """Genera el JSON actualizado con contenido expandido"""
    
    fixture = []
    
    # Mantener competencias y niveles como están
    competencias = [
        {"model": "competencias.competencia", "pk": 1, "fields": {"nombre": "Razonamiento Cuantitativo", "slug": "razonamiento", "descripcion": "Aprende a usar los números para resolver problemas del mundo real.", "color": "#1565C0", "icono": "🔢", "orden": 1}},
        {"model": "competencias.competencia", "pk": 2, "fields": {"nombre": "Lectura Crítica", "slug": "lectura", "descripcion": "Lee, comprende y analiza textos de forma inteligente.", "color": "#2E7D32", "icono": "📖", "orden": 2}},
        {"model": "competencias.competencia", "pk": 3, "fields": {"nombre": "Competencia Ciudadana", "slug": "ciudadana", "descripcion": "Aprende a vivir en comunidad, respetar y ejercer tus derechos.", "color": "#E65100", "icono": "🌍", "orden": 3}},
        {"model": "competencias.competencia", "pk": 4, "fields": {"nombre": "Ciencias Naturales", "slug": "ciencias", "descripcion": "Explora y entiende la naturaleza y el mundo que te rodea.", "color": "#6A1B9A", "icono": "🔬", "orden": 4}},
    ]
    fixture.extend(competencias)
    
    # Niveles
    niveles = [
        {"model": "competencias.nivel", "pk": 1, "fields": {"competencia": 1, "numero": 1, "titulo": "Contemos juntos", "descripcion": "Aprende a contar y reconocer números del 1 al 20"}},
        {"model": "competencias.nivel", "pk": 2, "fields": {"competencia": 1, "numero": 2, "titulo": "Sumas y restas", "descripcion": "Opera con números para resolver problemas sencillos"}},
        {"model": "competencias.nivel", "pk": 3, "fields": {"competencia": 1, "numero": 3, "titulo": "Multiplicación básica", "descripcion": "Aprende las tablas y aplícalas en situaciones reales"}},
        {"model": "competencias.nivel", "pk": 4, "fields": {"competencia": 1, "numero": 4, "titulo": "Fracciones simples", "descripcion": "Divide y comparte: entiende las partes de un todo"}},
        {"model": "competencias.nivel", "pk": 5, "fields": {"competencia": 1, "numero": 5, "titulo": "Problemas del mundo real", "descripcion": "Usa las matemáticas para resolver situaciones cotidianas"}},
        
        {"model": "competencias.nivel", "pk": 6, "fields": {"competencia": 2, "numero": 1, "titulo": "¿Qué dice el texto?", "descripcion": "Identifica la idea principal de un texto corto"}},
        {"model": "competencias.nivel", "pk": 7, "fields": {"competencia": 2, "numero": 2, "titulo": "Palabras nuevas", "descripcion": "Aprende a descubrir el significado de palabras desconocidas"}},
        {"model": "competencias.nivel", "pk": 8, "fields": {"competencia": 2, "numero": 3, "titulo": "¿Qué opina el autor?", "descripcion": "Distingue los hechos de las opiniones en un texto"}},
        {"model": "competencias.nivel", "pk": 9, "fields": {"competencia": 2, "numero": 4, "titulo": "Entre líneas", "descripcion": "Lee lo que el texto no dice directamente"}},
        {"model": "competencias.nivel", "pk": 10, "fields": {"competencia": 2, "numero": 5, "titulo": "Textos del entorno", "descripcion": "Lee y analiza textos de la vida diaria: avisos, noticias, cartas"}},
        
        {"model": "competencias.nivel", "pk": 11, "fields": {"competencia": 3, "numero": 1, "titulo": "Vivir en comunidad", "descripcion": "Aprende qué es la convivencia y por qué es importante"}},
        {"model": "competencias.nivel", "pk": 12, "fields": {"competencia": 3, "numero": 2, "titulo": "Mis derechos y deberes", "descripcion": "Conoce los derechos de los niños y tus responsabilidades"}},
        {"model": "competencias.nivel", "pk": 13, "fields": {"competencia": 3, "numero": 3, "titulo": "Resolución de conflictos", "descripcion": "Aprende a solucionar problemas de forma pacífica"}},
        {"model": "competencias.nivel", "pk": 14, "fields": {"competencia": 3, "numero": 4, "titulo": "Participación ciudadana", "descripcion": "Cómo participar y tomar decisiones en tu comunidad"}},
        {"model": "competencias.nivel", "pk": 15, "fields": {"competencia": 3, "numero": 5, "titulo": "Diversidad y respeto", "descripcion": "Valora las diferencias y construye una sociedad igualitaria"}},
        
        {"model": "competencias.nivel", "pk": 16, "fields": {"competencia": 4, "numero": 1, "titulo": "Seres vivos", "descripcion": "Aprende qué es un ser vivo y sus características básicas"}},
        {"model": "competencias.nivel", "pk": 17, "fields": {"competencia": 4, "numero": 2, "titulo": "El cuerpo humano", "descripcion": "Conoce los órganos y sistemas que te mantienen vivo"}},
        {"model": "competencias.nivel", "pk": 18, "fields": {"competencia": 4, "numero": 3, "titulo": "El medio ambiente", "descripcion": "Entiende los ecosistemas y cómo cuidar el planeta"}},
        {"model": "competencias.nivel", "pk": 19, "fields": {"competencia": 4, "numero": 4, "titulo": "La materia y la energía", "descripcion": "Explora los estados de la materia y las fuentes de energía"}},
        {"model": "competencias.nivel", "pk": 20, "fields": {"competencia": 4, "numero": 5, "titulo": "El universo", "descripcion": "Viaja al espacio y aprende sobre el sistema solar"}},
    ]
    fixture.extend(niveles)
    
    # Contenidos expandidos
    contenido_pk = 1
    for comp_slug, contenidos in CONTENIDO_EXPANDIDO.items():
        for i, cont in enumerate(contenidos, 1):
            nivel_pk = {"razonamiento": 1, "lectura": 6, "ciudadana": 11, "ciencias": 16}[comp_slug] + i - 1
            fixture.append({
                "model": "competencias.contenido",
                "pk": contenido_pk,
                "fields": {
                    "nivel": nivel_pk,
                    "titulo": cont["titulo"],
                    "cuerpo": cont["cuerpo"],
                    "ejemplo": cont["ejemplo"],
                    "tip": cont["tip"],
                    "actividades": cont["actividades"],
                    "faq": cont["faq"],
                    "video_file": ""  # Listo para videos futuros
                }
            })
            contenido_pk += 1
    
    return fixture

if __name__ == '__main__':
    fixture = generar_fixture()
    
    # Guardar JSON
    output_file = Path('competencias/fixtures/datos_iniciales_expandido.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(fixture, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Fixture expandida generada: {output_file}")
    print(f"✓ Total de items: {len(fixture)}")
    print(f"✓ Contenidos con estructura pedagógica completa")
    print(f"\nUso:")
    print(f"  python manage.py loaddata competencias/fixtures/datos_iniciales_expandido.json\n")
