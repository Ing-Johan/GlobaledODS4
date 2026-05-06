#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actualizar todos los 20 contenidos de competencias
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globaled.settings')
django.setup()

from competencias.models import Contenido

CONTENIDOS_COMPLETOS = {
    3: {
        "titulo": "La multiplicación: sumar rápido",
        "cuerpo": """Multiplicar es una forma rápida de sumar grupos iguales. 3 × 4 significa sumar 3 cuatro veces: 3+3+3+3 = 12.

Las tablas de multiplicar son como atajos. Si las memorizas, puedes calcular muy rápido.

La tabla del 2: 2,4,6,8,10,12,14,16,18,20. La del 5: 5,10,15,20,25,30,35,40,45,50.

**Patrones en las tablas:**
- Tabla del 2: todos pares
- Tabla del 5: termina en 0 o 5
- Tabla del 10: termina en 0
- Tabla del 9: los dígitos suman 9""",
        "ejemplo": "En una caja hay 6 huevos. Si tienes 4 cajas, ¿cuántos huevos tienes? 6 × 4 = 24 huevos en total.",
        "tip": "La tabla del 9 tiene un truco: los dígitos del resultado siempre suman 9. Ejemplo: 9×3=27, y 2+7=9.",
        "actividades": """<ol>
<li><strong>Grupos iguales:</strong> Imagina 3 grupos de 5 flores. ¿Cuántas flores en total? 3 × 5</li>
<li><strong>Memorizar tablas:</strong> Practica una tabla cada día. La del 2, luego del 3, etc.</li>
<li><strong>Juego de cartas:</strong> Escribe multiplicaciones en tarjetas. Di la respuesta rápido.</li>
<li><strong>Aplicación real:</strong> Si un paquete tiene 12 colores y tienes 5 paquetes, ¿cuántos colores?</li>
</ol>""",
        "faq": """<strong>¿Por qué multiplicamos si podemos sumar?</strong> Multiplicar es más rápido. Sumar 7+7+7+7+7 es lento. Mejor: 7 × 5.<br><br>
<strong>¿El orden importa en la multiplicación?</strong> No. 3 × 4 = 4 × 3. Ambos dan 12.<br><br>
<strong>¿Cuál es el truco para memorizar?</strong> Práctica todos los días. Primero con objetos, luego sin objetos."""
    },
    4: {
        "titulo": "Las fracciones: partes de un todo",
        "cuerpo": """Una fracción representa una parte de algo entero. Si divides una pizza en 4 partes iguales y comes 1, comiste 1/4 de la pizza.

El número de abajo (denominador) dice en cuántas partes está dividido el todo. El de arriba (numerador) dice cuántas partes tomaste.

Medias (1/2), tercios (1/3) y cuartos (1/4) son las fracciones más comunes.

**Partes de una fracción:**
- Numerador (arriba): cuántas partes tomaste
- Línea: divide
- Denominador (abajo): en cuántas partes se divide""",
        "ejemplo": "Tienes una barra de chocolate con 8 cuadros. Comes 3 cuadros. Comiste 3/8 del chocolate.",
        "tip": "Si el numerador y el denominador son iguales (como 4/4), eso equivale a 1 entero completo.",
        "actividades": """<ol>
<li><strong>Divide y comparte:</strong> Corta un papel en 4 partes iguales. Toma 1. ¿Qué fracción es? 1/4</li>
<li><strong>Visualización:</strong> Dibuja 6 puntos. Colorea 2. ¿Qué fracción coloreaste? 2/6</li>
<li><strong>Fracciones de comida:</strong> Una pizza dividida en 8 partes. ¿Cuánta comiste? Expresa en fracción.</li>
<li><strong>Comparación:</strong> ¿Cuál es mayor: 1/2 o 1/4? (Dibuja para ver)</li>
</ol>""",
        "faq": """<strong>¿Todos los números pueden dividirse?</strong> Sí, en fracciones iguales. Pero algunos son divisibles en más partes que otros.<br><br>
<strong>¿1/2 es lo mismo que 2/4?</strong> Sí. Son fracciones equivalentes: representan la misma cantidad.<br><br>
<strong>¿Se pueden comer fracciones?</strong> No literalmente, pero sí puedes comerte una fracción de comida. Por ejemplo, 1/4 de pizza."""
    },
    5: {
        "titulo": "Matemáticas en la vida real",
        "cuerpo": """Las matemáticas están en todas partes: en el mercado, en el tiempo, en los deportes y en la cocina.

Cuando compras algo, usas la resta para saber el cambio. Cuando cocinas, usas fracciones para medir ingredientes. Cuando juegas fútbol, cuentas los goles.

Un problema matemático tiene datos (lo que sabes) y una pregunta (lo que debes encontrar). Léelo con calma y decide qué operación usar.

**Pasos para resolver problemas:**
1. Lee con calma
2. Subraya los datos importantes
3. Pregúntate: ¿Qué debo encontrar?
4. Elige la operación (suma, resta, multiplicación)
5. Calcula
6. Comprueba tu respuesta""",
        "ejemplo": "Tienes $5.000. Compras un cuaderno por $3.200. ¿Cuánto te sobra? $5.000 - $3.200 = $1.800 de cambio.",
        "tip": "Antes de calcular, subraya los datos importantes del problema. ¡Eso evita errores!",
        "actividades": """<ol>
<li><strong>Problemas de dinero:</strong> Si un helado cuesta $2.500 y tienes $10.000, ¿cuántos helados puedes comprar?</li>
<li><strong>Problemas de tiempo:</strong> La película empieza a las 3pm y dura 2 horas. ¿A qué hora termina?</li>
<li><strong>Problemas deportivos:</strong> Tu equipo anotó 25 goles en 5 partidos. ¿Promedio por partido?</li>
<li><strong>Crea tus problemas:</strong> Inventa un problema con números de tu vida.</li>
</ol>""",
        "faq": """<strong>¿Todos los problemas tienen una solución?</strong> Sí, pero debes leer bien y usar la operación correcta.<br><br>
<strong>¿Qué pasa si me confundo con la operación?</strong> Prueba con la otra. Si daba mal, cambia de operación.<br><br>
<strong>¿Los decimales se usan en la vida real?</strong> Mucho: en dinero (centavos), medidas (altura), etc."""
    },
    7: {
        "titulo": "¿Quién es el autor y qué siente?",
        "cuerpo": """El autor es la persona que escribió el texto. Cada autor tiene un propósito: contar una historia, informar, convencer o enseñar.

Para entender al autor, pregúntate: ¿Qué siente? ¿Está feliz, triste, enojado? ¿Quiere que yo crea algo?

Las palabras que elige el autor revelan sus sentimientos.

**Indicios del sentimiento del autor:**
- Palabras alegres o tristes
- Punto de vista (cuenta en primera o tercera persona)
- Si usa muchos detalles o pocos
- El tono (serio, divertido, sarcástico)""",
        "ejemplo": "'Este libro es increíble, emocionante y no puedo dejarlo.' El autor está emocionado, le encanta el libro.",
        "tip": "Lee entre líneas. Las palabras dicen lo que el autor PIENSA, pero el tono muestra lo que SIENTE.",
        "actividades": """<ol>
<li><strong>Analiza el tono:</strong> Lee estas frases: "Hoy fue un día hermoso" vs "Hoy fue un día cualquiera". ¿Cuál muestra más felicidad?</li>
<li><strong>Propósito del autor:</strong> Lee un párrafo. ¿Intenta informar, entretener o convencer?</li>
<li><strong>Palabras emocionales:</strong> Anota palabras que muestran sentimientos: alegre, triste, furioso.</li>
<li><strong>Escribe con sentimiento:</strong> Cuenta un evento con tono triste. Ahora con tono feliz. ¿Cambia algo?</li>
</ol>""",
        "faq": """<strong>¿El autor siempre dice la verdad?</strong> No siempre. A veces miente o exagera para contar una historia mejor.<br><br>
<strong>¿Puedo saber qué siente el autor?</strong> Generalmente sí, por las palabras y el tono que usa.<br><br>
<strong>¿Los autores de noticias son neutrales?</strong> Deberían serlo, pero a veces tienen opiniones que cuelan en el texto."""
    },
    8: {
        "titulo": "Hechos vs. opiniones",
        "cuerpo": """Un hecho es algo que se puede comprobar. Una opinión es lo que alguien piensa o siente, y puede variar.

Hecho: 'Colombia tiene 32 departamentos.' Esto es verificable.
Opinión: 'Colombia es el país más bonito del mundo.' Esto depende de quien lo dice.

Palabras como 'creo', 'pienso', 'me parece', 'deberían' suelen indicar una opinión.

**Características:**
- Hechos: se pueden comprobar, son verdaderos o falsos
- Opiniones: son personales, no se pueden comprobar directamente""",
        "ejemplo": "'El agua hierve a 100°C' es un hecho. 'El té es la mejor bebida del mundo' es una opinión.",
        "tip": "Pregúntate: ¿Puedo comprobar esto con evidencia? Si sí, es un hecho. Si no, es una opinión.",
        "actividades": """<ol>
<li><strong>Clasifica frases:</strong> Lee: "París es la capital de Francia" vs "París es la mejor ciudad". ¿Cuál es hecho? ¿Opinión?</li>
<li><strong>Busca evidencia:</strong> Lee un texto. ¿Qué hechos puedo verificar en internet?</li>
<li><strong>Opina tú:</strong> Expresa una opinión sobre un libro, película o comida. Otros pueden tener opiniones diferentes.</li>
<li><strong>Análisis de noticias:</strong> Lee una noticia. Separa hechos de opiniones del periodista.</li>
</ol>""",
        "faq": """<strong>¿Las opiniones pueden estar mal?</strong> No exactamente. Son personales. Pero se deben basar en hechos reales.<br><br>
<strong>¿Qué pasa si dos personas tienen opiniones diferentes?</strong> Ambas pueden estar bien. Las opiniones varían según la persona.<br><br>
<strong>¿Cómo sé si es un hecho?</strong> Si aparece en múltiples fuentes confiables, probablemente es un hecho."""
    },
    9: {
        "titulo": "Lo que no está escrito",
        "cuerpo": """Los autores no siempre dicen todo directamente. A veces debes inferir: llegar a una conclusión usando las pistas del texto más tu conocimiento.

Leer entre líneas significa entender lo que el texto sugiere, aunque no lo diga con palabras exactas.

Observa el tono del texto, las emociones de los personajes y los detalles que el autor elige mencionar.

**Pistas para inferir:**
- El estado emocional de los personajes
- Las acciones que hacen
- Lo que NO dicen (el silencio también habla)
- Los detalles que el autor describe""",
        "ejemplo": "'María llegó a casa con los ojos rojos y no quiso cenar.' El texto no dice que María estaba triste, pero lo inferimos por las pistas.",
        "tip": "Hazte preguntas mientras lees: ¿Por qué el autor escribió esto? ¿Qué siente el personaje?",
        "actividades": """<ol>
<li><strong>Inferencias simples:</strong> "Juan cerró la puerta rápido y se sentó." ¿Qué puedes inferir? ¿Estaba cansado? ¿Apurado?</li>
<li><strong>Emociones escondidas:</strong> Lee: "Ana no habló en toda la comida." ¿Qué podrías inferir?</li>
<li><strong>Contexto es clave:</strong> "El portero vio llover." En qué contexto? ¿Feliz o triste?</li>
<li><strong>Tu propia historia:</strong> Lee un párrafo. Infiere qué pasará después sin leer más.</li>
</ol>""",
        "faq": """<strong>¿Mis inferencias pueden estar mal?</strong> Sí, por eso se llama inferencia. Otros pueden llegar a conclusiones diferentes.<br><br>
<strong>¿Cómo sé si mi inferencia es razonable?</strong> Basándote en pistas del texto. Si hay evidencia, tu inferencia es mejor.<br><br>
<strong>¿Es lo mismo inferencia que adivinanza?</strong> No. Una inferencia se basa en datos. Una adivinanza es suerte."""
    },
    10: {
        "titulo": "Textos de todos los días",
        "cuerpo": """En la vida diaria leemos muchos tipos de textos: avisos, recetas, noticias, carteles, etiquetas y cartas.

Cada texto tiene un propósito: informar, convencer, instruir o entretener. Saber el propósito te ayuda a leerlo mejor.

Las noticias buscan informar. Los avisos publicitarios buscan convencer. Las recetas buscan instruir.

**Tipos de textos cotidianos:**
- Noticias: informar qué pasó
- Avisos: convencer de comprar algo
- Recetas: instruir cómo hacer algo
- Cartas: comunicar un mensaje personal
- Etiquetas: informar datos (ingredientes, precio)""",
        "ejemplo": "Un aviso que dice '¡Oferta! 2x1 en pan hoy' busca convencerte de comprar. Una receta de torta busca enseñarte a prepararla.",
        "tip": "Antes de leer, mira el título y las imágenes. Te dan una idea de qué tipo de texto es y para qué sirve.",
        "actividades": """<ol>
<li><strong>Recapacita:</strong> Lee una receta simple. ¿Cuál es su propósito? ¿A quién va dirigida?</li>
<li><strong>Avisos alrededor:</strong> Busca avisos en tu barrio. ¿Qué intentan vender o convencer?</li>
<li><strong>Escribe una receta:</strong> Enseña a alguien a hacer tu comida favorita.</li>
<li><strong>Carta personal:</strong> Escribe una carta a un amigo. ¿Cuál es su propósito?</li>
</ol>""",
        "faq": """<strong>¿Todos los textos tienen el mismo propósito?</strong> No. Varía según el tipo: informar, entretener, convencer, instruir.<br><br>
<strong>¿Cómo identifico el propósito?</strong> Lee el título, introducción y piensa: ¿Qué intenta el autor que haga o crea?<br><br>
<strong>¿Un texto puede tener múltiples propósitos?</strong> Sí. Por ejemplo, una noticia informa pero a veces intenta convencer."""
    },
    12: {
        "titulo": "Mis derechos y deberes",
        "cuerpo": """Todos los niños del mundo tienen derechos fundamentales, reconocidos por la ONU en 1989.

Algunos derechos: educación, salud, familia, juego, protección y participación.

Pero también tenemos deberes: respetar a los demás, cuidar el ambiente, estudiar y obedecer las normas del hogar y la escuela.

**Tus derechos fundamentales:**
- Derecho a la vida y protección
- Derecho a la educación
- Derecho a la salud
- Derecho al nombre e identidad
- Derecho a la familia
- Derecho a jugar y recrearse""",
        "ejemplo": "Tienes derecho a estudiar, y tu deber es asistir a clases y esforzarte. Tienes derecho a jugar, y tu deber es respetar el turno de otros.",
        "tip": "Los derechos y deberes van de la mano. Cuando respetas los derechos de otros, también proteges los tuyos.",
        "actividades": """<ol>
<li><strong>Mis derechos y deberes:</strong> Haz dos listas: una de derechos que tienes, otra de deberes que cumples.</li>
<li><strong>Historias de derechos:</strong> Lee historias donde se respetan o se violan derechos.</li>
<li><strong>Responsabilidad:</strong> Identifica un deber que cumples bien y otro que necesitas mejorar.</li>
<li><strong>Campaña de conciencia:</strong> Crea un afiche sobre los derechos de los niños.</li>
</ol>""",
        "faq": """<strong>¿Todos los niños del mundo tienen los mismos derechos?</strong> Sí, según la ONU. Pero algunos países aún no los cumplen completamente.<br><br>
<strong>¿Qué pasa si alguien viola mis derechos?</strong> Puedes decirle a un adulto de confianza: papás, maestro o policía.<br><br>
<strong>¿Tengo más derechos que deberes?</strong> Deben estar equilibrados. Más derechos significan más responsabilidad."""
    },
    13: {
        "titulo": "Solucionar conflictos sin violencia",
        "cuerpo": """Los conflictos son desacuerdos que ocurren cuando las personas quieren cosas diferentes. Son normales, pero debemos resolverlos bien.

Pasos para resolver un conflicto: 1) Cálmate. 2) Escucha al otro. 3) Explica cómo te sientes. 4) Busquen una solución juntos.

La violencia (física o verbal) nunca es la solución. El diálogo y el respeto sí lo son.

**Estrategias de resolución:**
- Hablar con calma
- Escuchar el punto de vista del otro
- Buscar puntos en común
- Comprometerse o ceder
- Pedir ayuda de un adulto si es necesario""",
        "ejemplo": "Tú y tu amigo quieren jugar juegos diferentes. En vez de pelear, pueden turnarse: primero un juego, luego el otro. ¡Los dos ganan!",
        "tip": "Cuando estés enojado, cuenta hasta 10 antes de hablar. Respirar profundo ayuda a pensar con calma.",
        "actividades": """<ol>
<li><strong>Rol play:</strong> Actúa un conflicto simple. Luego resuélvelo de forma pacífica.</li>
<li><strong>Diario de conflictos:</strong> Anota un conflicto que tuviste. ¿Cómo lo resolviste?</li>
<li><strong>Habilidades de escucha:</strong> Practica escuchar a alguien sin interrumpir.</li>
<li><strong>Mediación:</strong> Ayuda a dos amigos a resolver un conflicto siendo neutral.</li>
</ol>""",
        "faq": """<strong>¿Siempre se pueden resolver conflictos sin violencia?</strong> Sí, con diálogo y respeto. La violencia solo empeora las cosas.<br><br>
<strong>¿Qué hago si alguien es violento conmigo?</strong> Aléjate y cuéntale a un adulto. Tu seguridad es lo primero.<br><br>
<strong>¿Ceder significa perder?</strong> No. Ceder es buscar la paz. A veces ambos ganan un poco."""
    },
    14: {
        "titulo": "¿Cómo participamos en la sociedad?",
        "cuerpo": """Participar es tomar parte activa en las decisiones de tu comunidad. Todos podemos participar, incluso los niños.

Formas de participar: votar en el gobierno estudiantil, opinar en clase, cuidar los espacios públicos, proponer ideas.

La democracia es el sistema donde todos pueden participar y elegir a sus representantes.

**Formas de participación:**
- Voto (elegir representantes)
- Opinión (hablar en clase, debates)
- Organización (participar en grupos)
- Acción (cuidar espacios, proyectos)
- Propuestas (sugerir cambios)""",
        "ejemplo": "En tu escuela hay elecciones para personero estudiantil. Participar votando o siendo candidato es ejercer la democracia.",
        "tip": "Participar también es hablar cuando algo está mal. Tu voz importa y puede cambiar las cosas.",
        "actividades": """<ol>
<li><strong>Vota en tu clase:</strong> Realiza una votación sobre algo importante para todos.</li>
<li><strong>Tu propuesta:</strong> Piensa en algo que mejoraría tu escuela. Propónlo.</li>
<li><strong>Gobierno estudiantil:</strong> Aprende qué hace el personero, tesorero, etc.</li>
<li><strong>Proyecto comunitario:</strong> Participa en algo que beneficie a tu comunidad.</li>
</ol>""",
        "faq": """<strong>¿Qué es la democracia?</strong> Es un sistema donde el poder está en el pueblo. Todos tienen voz y voto.<br><br>
<strong>¿Puede un niño participar en decisiones?</strong> Claro. En tu escuela, barrio y país tienes derecho a participar.<br><br>
<strong>¿Mi opinión realmente cuenta?</strong> Sí. Cuando muchos opinamos igual, podemos cambiar cosas."""
    },
    15: {
        "titulo": "Todos somos diferentes, todos somos iguales",
        "cuerpo": """La diversidad es la variedad de personas que existen: diferentes culturas, colores de piel, idiomas, religiones y formas de pensar.

Ser diferentes no nos hace mejores ni peores. Todos merecemos el mismo respeto y las mismas oportunidades.

Discriminar a alguien por ser diferente está mal y va en contra de los derechos humanos.

**Tipos de diversidad:**
- Raza y color de piel
- Género
- Religión
- Cultura y tradiciones
- Capacidades físicas
- Orientación de pensar""",
        "ejemplo": "En Colombia vivimos indígenas, afrocolombianos, mestizos y muchos más. Cada grupo tiene su cultura, y todas son valiosas.",
        "tip": "Conocer otras culturas enriquece tu propia vida. ¡La diversidad hace al mundo más interesante!",
        "actividades": """<ol>
<li><strong>Culturas del mundo:</strong> Investiga sobre una cultura diferente a la tuya.</li>
<li><strong>Respeto e inclusión:</strong> ¿Cómo incluirías a alguien diferente en tus juegos?</li>
<li><strong>Tradiciones:</strong> Comparte una tradición de tu familia con la clase.</li>
<li><strong>Combate discriminación:</strong> ¿Qué harías si ves que discriminan a alguien?</li>
</ol>""",
        "faq": """<strong>¿Es malo ser diferente?</strong> No. Es natural y bonito. Nos hace únicos.<br><br>
<strong>¿Qué es discriminación?</strong> Tratar mal a alguien por ser diferente. Es injusto y está prohibido.<br><br>
<strong>¿Debo pensar igual que todos?</strong> No. La diversidad de opiniones también es valiosa."""
    },
    17: {
        "titulo": "Nuestro cuerpo por dentro",
        "cuerpo": """El cuerpo humano tiene sistemas que trabajan juntos para mantenernos vivos.

El sistema digestivo procesa los alimentos. El sistema respiratorio lleva oxígeno a las células. El sistema circulatorio transporta la sangre. El sistema nervioso controla todo el cuerpo.

Cuidar el cuerpo con buena alimentación, ejercicio y descanso es esencial.

**Sistemas principales:**
- Sistema digestivo: procesa comida, extrae nutrientes
- Sistema respiratorio: trae oxígeno, expulsa CO2
- Sistema circulatorio: transporta sangre con oxígeno
- Sistema óseo: sostiene y protege órganos
- Sistema muscular: permite movimiento""",
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
    },
    18: {
        "titulo": "Cuidemos nuestro planeta",
        "cuerpo": """El medio ambiente es todo lo que nos rodea: el aire, el agua, el suelo, las plantas y los animales.

Un ecosistema es un conjunto de seres vivos que viven en el mismo lugar y se relacionan entre sí. Ejemplo: el bosque, el río, el mar.

Las acciones humanas como la contaminación y la deforestación dañan los ecosistemas. Todos podemos ayudar a cuidarlos.

**Problemas ambientales:**
- Contaminación del aire
- Contaminación del agua
- Deforestación
- Cambio climático
- Extinción de especies""",
        "ejemplo": "Un río limpio tiene peces, aves y plantas que dependen unos de otros. Si lo contaminamos, todo ese ecosistema se daña.",
        "tip": "Las 3R: Reducir, Reutilizar, Reciclar. Son acciones simples que tú puedes hacer hoy para cuidar el planeta.",
        "actividades": """<ol>
<li><strong>Ecosistema local:</strong> Identifica un ecosistema cerca de ti (parque, jardín). ¿Qué seres vivos hay?</li>
<li><strong>Reduce desperdicios:</strong> Esta semana, usa menos plástico. Anota qué lograste.</li>
<li><strong>Planta un árbol:</strong> Si es posible, planta una semilla. Cuídala.</li>
<li><strong>Campaña de limpieza:</strong> Organiza una limpieza de tu barrio o parque.</li>
</ol>""",
        "faq": """<strong>¿Mi acción importa si muchos contaminan?</strong> Claro. Si todos hacemos un poco, el cambio es enorme.<br><br>
<strong>¿Reciclar realmente ayuda?</strong> Sí. Reduce la cantidad de basura que va a los rellenos.<br><br>
<strong>¿Qué es el cambio climático?</strong> Es el aumento de temperatura mundial causado por contaminación. Afecta el clima global."""
    },
    19: {
        "titulo": "La materia y sus estados",
        "cuerpo": """La materia es todo lo que tiene masa y ocupa espacio. Todo lo que puedes tocar es materia.

La materia puede estar en tres estados: sólido (forma fija, como el hielo), líquido (toma la forma del recipiente, como el agua) y gaseoso (se expande, como el vapor).

El calor puede cambiar el estado de la materia: el hielo se derrite con calor, el agua se evapora al hervir.

**Estados de la materia:**
- Sólido: forma y volumen fijos
- Líquido: forma variable, volumen fijo
- Gaseoso: forma y volumen variables
- Cambios: fusión (sólido→líquido), vaporización (líquido→gaseoso)""",
        "ejemplo": "El agua es el mejor ejemplo: en el congelador es hielo (sólido), en el vaso es agua (líquido), cuando hierve es vapor (gaseoso).",
        "tip": "La materia nunca desaparece, solo cambia de estado o de forma. ¡Eso se llama conservación de la materia!",
        "actividades": """<ol>
<li><strong>Experimento de fusión:</strong> Coloca un cubo de hielo sobre un plato. Observa cómo se derrite.</li>
<li><strong>Vaporización:</strong> Hierve agua en una olla. ¿Ves el vapor (gaseoso)?</li>
<li><strong>Clasifica objetos:</strong> ¿Es sólido, líquido o gaseoso? Tabla, agua, aire.</li>
<li><strong>Cambios en la naturaleza:</strong> Observa hielo, agua, nieve. ¿Qué cambios de estado ves?</li>
</ol>""",
        "faq": """<strong>¿Existe un cuarto estado de la materia?</strong> Sí: el plasma. Pero es muy raro y se ve en estrellas y rayos.<br><br>
<strong>¿Por qué el hielo flota en el agua?</strong> Porque el hielo es menos denso que el agua. Un fenómeno raro pero real.<br><br>
<strong>¿El aire es materia?</strong> Sí, aunque no lo veamos. Tiene masa y ocupa espacio."""
    },
    20: {
        "titulo": "Nuestro sistema solar",
        "cuerpo": """El universo es todo lo que existe: galaxias, estrellas, planetas y más. Nuestra galaxia se llama Vía Láctea.

Nuestro sistema solar tiene 8 planetas que giran alrededor del Sol. En orden: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano y Neptuno.

La Tierra es el único planeta donde sabemos que existe vida. Tiene agua líquida, atmósfera y la temperatura adecuada.

**Nuestro sistema solar:**
- El Sol: estrella central
- 8 planetas: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno
- Lunas: satélites que orbitan planetas
- Asteroides y cometas""",
        "ejemplo": "El Sol es una estrella enorme: caben más de un millón de Tierras dentro de él. Sin embargo, es solo una estrella entre miles de millones en la Vía Láctea.",
        "tip": "Truco para recordar los planetas: 'Mi Vecina Tierra Muy Juiciosa Siempre Usa Normas'. (Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno)",
        "actividades": """<ol>
<li><strong>Modelo del sistema solar:</strong> Haz una maqueta con bolitas de plastilina.</li>
<li><strong>Investiga un planeta:</strong> Elige uno. Aprende: tamaño, distancia al Sol, satélites.</li>
<li><strong>Observa el cielo:</strong> Por la noche, ¿ves la Luna? ¿Planetas?</li>
<li><strong>Fases de la Luna:</strong> Durante un mes, dibuja la Luna cada noche. ¿Cambia de forma?</li>
</ol>""",
        "faq": """<strong>¿Hay vida en otros planetas?</strong> Posiblemente, pero aún no la hemos encontrado. La Tierra es el único confirmed.<br><br>
<strong>¿Por qué la Tierra es especial?</strong> Tiene agua, atmósfera, y está a la distancia perfecta del Sol para vida.<br><br>
<strong>¿Qué es una luna?</strong> Un satélite natural que orbita un planeta. La Tierra tiene una: nuestra Luna."""
    }
}

def actualizar_todos():
    """Actualiza todos los 20 contenidos"""
    print("\n" + "="*70)
    print("ACTUALIZAR TODOS LOS CONTENIDOS - GlobalEd")
    print("="*70 + "\n")
    
    actualizados = 0
    errores = 0
    
    for nivel_id, datos in CONTENIDOS_COMPLETOS.items():
        try:
            contenido = Contenido.objects.get(nivel_id=nivel_id)
            contenido.titulo = datos["titulo"]
            contenido.cuerpo = datos["cuerpo"]
            contenido.ejemplo = datos["ejemplo"]
            contenido.tip = datos["tip"]
            contenido.actividades = datos["actividades"]
            contenido.faq = datos["faq"]
            contenido.save()
            print(f"✓ Nivel {nivel_id}: {datos['titulo']}")
            actualizados += 1
        except Contenido.DoesNotExist:
            print(f"✗ Nivel {nivel_id}: No encontrado")
            errores += 1
        except Exception as e:
            print(f"✗ Nivel {nivel_id}: {str(e)[:60]}")
            errores += 1
    
    print("\n" + "="*70)
    print(f"✓ COMPLETADO: {actualizados} contenidos actualizados")
    if errores:
        print(f"⚠ {errores} errores")
    print("="*70 + "\n")

if __name__ == '__main__':
    actualizar_todos()
