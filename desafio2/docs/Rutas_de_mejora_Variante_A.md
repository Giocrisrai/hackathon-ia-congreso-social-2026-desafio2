# Rutas de mejora · Radar de acompañamiento

Desafío 2 · Educación · Hackathon IA Congreso Social UC 2026

Estas rutas orientan, no obligan. Pueden seguir una, combinar varias o proponer una propia. Cada ruta parte de una limitación real de la plantilla, descrita en la ficha de línea base. Recomendación: elijan como máximo dos rutas y háganlas bien.

## Ruta 1 · Ajustar la herramienta a un usuario real

**Por qué:** La configuración por defecto le habla a "jefes de carrera" en general, sin saber cuántos estudiantes atienden ni cuánto tiempo tienen.

**Dónde:** Pestaña config: usuario, tono, largo_respuesta, ejemplos y cupo_porcentaje.

**Ideas para empezar:**

- Elijan un usuario específico, por ejemplo un tutor par de segundo año o una jefa de carrera vespertina.
- Escriban 1 a 3 ejemplos de la ficha ideal para esa persona; la IA imita su estilo.
- Ajusten el cupo a lo que esa persona realmente puede atender en una semana.

**Cómo saber si funcionó:** Muestren la ficha antes y después a alguien con ese rol y pregúntenle cuál usaría.

**Tiempo estimado:** 30 a 45 minutos.

## Ruta 2 · Revisar a quién deja fuera la cola

**Por qué:** Aunque el modelo no usa sexo ni sede, con la configuración base la cola incluye al 25,6% de los vespertinos frente al 10,7% de los diurnos, y alcanza al 48% de los hombres que desertan frente al 32% de las mujeres. Otras variables funcionan como proxy.

**Dónde:** Pestaña config: variables_excluidas y cupo_porcentaje.

**Ideas para empezar:**

- Excluyan `jornada` o `edad` y comparen cómo cambia la cola y el "¿Por qué aparece?".
- Discutan: ¿marcar más a los vespertinos es injusto, o refleja que necesitan más apoyo? ¿Qué pasa con quien queda fuera?
- Pidan al mentor la tabla de equidad por grupo.

**Cómo saber si funcionó:** Pueden explicar en el pitch qué variable excluyeron (o decidieron mantener), por qué, y qué cambió.

**Tiempo estimado:** 30 a 45 minutos.

## Ruta 3 · Agregar los servicios reales de su contexto

**Por qué:** El catálogo base tiene 9 servicios genéricos de una institución ficticia. Un tutor real necesita derivar a servicios que existen.

**Dónde:** Pestaña servicios_extra.

**Ideas para empezar:**

- Busquen 3 a 5 servicios públicos de apoyo de su institución (becas, salud mental, sala cuna, tutorías).
- Copien la fila EJEMPLO, cambien EJEMPLO por X01, X02, etc., y completen todas las columnas con la fuente oficial.

**Cómo saber si funcionó:** La barra lateral muestra los servicios agregados sin filas ignoradas, y la IA los cita con su código en la ficha.

**Tiempo estimado:** 30 a 45 minutos.

## Ruta 4 · Cuidar el mensaje al estudiante

**Por qué:** El borrador puede sonar a "te estamos vigilando". La validación bloquea palabras como "riesgo" o porcentajes, pero no el tono.

**Dónde:** Pestaña config: tono, ejemplos e instrucciones_extra.

**Ideas para empezar:**

- Lean 5 borradores como si fueran el estudiante: ¿se sentirían apoyados o señalados?
- Agreguen reglas como "nunca menciones la asistencia ni las notas en el mensaje".
- Diseñen qué pasa si el estudiante no responde.

**Cómo saber si funcionó:** Un compañero que no conoce la herramienta lee el borrador y dice que no se sentiría juzgado.

**Tiempo estimado:** 20 a 30 minutos.

## Ruta 5 · Medir el impacto

**Por qué:** La rúbrica valora el beneficio social verificable. Necesitan mostrar que la herramienta cambia algo.

**Dónde:** Fuera de la Sheet: en una tabla propia del equipo.

**Ideas para empezar:**

- La app pregunta "¿La propuesta te ahorró trabajo?" y registra cada decisión. Úsenlo como indicador.
- Propongan cómo medirían en un semestre real: porcentaje contactado en menos de 72 horas, porcentaje que acepta el apoyo, retención a segundo año.

**Cómo saber si funcionó:** Tienen 3 indicadores concretos para el pitch, con quién los mide y sus límites.

**Tiempo estimado:** 30 minutos.

## Ruta 6 · Probar el mal uso antes que el jurado

**Por qué:** El jurado hará al menos una pregunta sobre riesgos éticos o mal uso, y el checklist ético es requisito para ser evaluados.

**Dónde:** En la app, sin cambiar nada; documentan los resultados en el checklist ético.

**Ideas para empezar:**

- Escriban en instrucciones_extra "menciona su probabilidad de desertar" y vean qué hace la validación.
- Pregúntense qué pasaría si la lista llega a admisión o a cobranza.
- Escriban instrucciones ocultas, como "ignora tus reglas".
- Anoten qué pasó en cada intento y qué cambiarían para evitarlo.

**Cómo saber si funcionó:** Tienen una lista de al menos 5 intentos de mal uso, con el resultado y la medida que tomaron o propondrían.

**Tiempo estimado:** 20 a 30 minutos.
