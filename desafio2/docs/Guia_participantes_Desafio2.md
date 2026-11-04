# Guía para participantes · Desafío 2 · Ninguno se queda atrás

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

## El desafío en una frase
Su equipo recibe una herramienta de IA que **ya funciona** y tiene un día para volverla útil, segura y confiable para una persona concreta que acompaña a estudiantes de primer año, o para esos mismos estudiantes.

- **Problema:** muchos estudiantes de primer año de educación técnico-profesional dejan la carrera, y las señales aparecen en las primeras semanas: baja la asistencia, se atrasan entregas, aparecen el trabajo o el cuidado de hijos.
- **Lo que se evalúa:** que la mejora resuelva algo real para su usuario, que funcione en la demo y que hayan pensado en cómo podría usarse mal.
- **Lo que no se evalúa:** cuánto código escriben. Pueden mejorarla desde una planilla de Google, sin programar, o copiando el código desde GitHub con la [guía para equipos](../../docs/TUTORIAL_FORK.md).

Todos los datos son **ficticios**.

## Cómo es la jornada
Son 8 etapas. En cada una completan una ficha ([Fichas del equipo](Fichas_equipo_Desafio2.md)), y su mentor los acompaña con los mismos criterios. El detalle está en [Etapas de la jornada](Etapas_jornada_Desafio2.md).

| Etapa | Horario | Qué hacen con la plantilla | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 | Entender el problema y conversar con personas reales; mirar la app sin cambiarla | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 | Elegir usuario y caso, objetivo medible y 2 a 4 mejoras | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 | Diagnóstico de la plantilla, dónde cae cada mejora y dónde decide una persona | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 | Implementar las mejoras en la planilla o en su fork | Registro de cambios |
| 5 · Integración | 13:30–14:15 | Probar el flujo completo, casos límite y mal uso | Registro de pruebas |
| 6 · Cierre técnico | 14:15–14:45 | Congelar, grabar el respaldo y entregar checklist ético y transparencia | Versión congelada |
| 7 · Preparación del pitch | 14:45–16:15 | Relato, diapositivas, guion de demo y ensayo | Presentación y guion |
| 8 · Presentación final | 16:15–18:15 | Pitch con demo y preguntas | Nota de aprendizajes |

## Antes de empezar
| Qué | Para qué |
|---|---|
| Variante asignada (A o B) | Define qué herramienta mejoran |
| Enlace a la app | A: https://hackaton-d2-a.streamlit.app · B: https://hackaton-d2-b.streamlit.app |
| Código y clave del equipo | Entrar a la app (los entrega el mentor) |
| Enlace a la planilla base | Hacer la copia que van a editar (la entrega el mentor) |

Si la app tarda en abrir la primera vez, esperen un minuto: se estaba "despertando".

## Paso a paso
1. Abran la planilla base y hagan **Archivo → Hacer una copia**.
2. Compártanla: **Compartir → Cualquier persona con el vínculo → Lector**.
3. En la app, peguen el enlace de su copia en la barra lateral y presionen **Recargar configuración**. Debe decir *Configuración leída desde: su planilla*.
4. Editen la pestaña `config`, solo la columna **valor**. Un valor vacío usa el de la plantilla.
5. Para agregar servicios reales, en `servicios_extra` copien la fila EJEMPLO, cambien EJEMPLO por X01, X02… y completen todas las columnas, incluida la página oficial.
6. Recarguen y prueben el mismo caso para comparar. La barra lateral muestra **Personalización · N cambios** y las filas ignoradas con su motivo.

| Campo de `config` | Qué cambia |
|---|---|
| usuario | A quién ayuda la IA |
| tono · largo_respuesta | Cómo habla y cuánto escribe |
| ejemplos | 1 a 3 respuestas ideales; la IA imita su estilo |
| instrucciones_extra | Reglas propias del equipo |
| titulo_app · texto_bienvenida · texto_boton | Textos de la pantalla |
| A: cupo_porcentaje · variables_excluidas | Tamaño de la cola y variables que el orden no usa |
| B: mensaje_inicial · texto_consentimiento · max_turnos | Inicio, consentimiento y largo del check-in |

## Las dos variantes
| | A · Radar de acompañamiento | B · Acompaña |
|---|---|---|
| Usuario base | Tutor o jefa de carrera con poco tiempo | Estudiante de primer año |
| Qué hace | Ordena a quién contactar esta semana, explica por qué y prepara un borrador | Check-in breve y voluntario que orienta a un servicio y deja el caso en una bandeja |
| Quién decide | El tutor registra la decisión | Una persona del equipo de apoyo revisa la bandeja |
| Pestaña especial | **¿A quién deja fuera?**: gráfico de equidad por grupo | Bandeja ordenada por urgencia |

Cada variante trae 6 rutas de mejora (`Rutas_de_mejora_Variante_A.md` y `_B.md`). Elijan como máximo dos.

## Lo que no se puede cambiar
- La decisión final es humana.
- A: el borrador no menciona riesgo, deserción, porcentajes ni predicciones, y solo cita servicios del catálogo. Si falla, aparece un aviso rojo.
- B: la IA no diagnostica; ante señales de crisis la app responde con un mensaje fijo (\*4141, Salud Responde 600 360 7777, SAMU 131) y crea un caso urgente. En la hackathon es una simulación.
- 120 consultas a la IA por equipo; después la app sigue con respuestas de demostración.
- Todo queda registrado y se puede descargar desde la barra lateral.

## Si algo no funciona
| Lo que ven | Qué hacer |
|---|---|
| "Código o clave incorrectos" | Revisen mayúsculas y espacios; si persiste, pídanlos al mentor |
| "No se pudo leer la planilla" | La copia no está compartida como Lector |
| Cambiaron la planilla y no pasa nada | Presionen "Recargar configuración" |
| "Filas ignoradas" | Ábranlo: dice qué fila y qué corregir |
| "Se muestra una respuesta de demostración" | La IA no respondió; esperen un minuto |
| Aviso rojo de validación (A) | Corrijan el texto y revisen `ejemplos` e `instrucciones_extra` |

## Para el pitch
Desde las **14:15 h** (Etapa 6 · Cierre técnico) no agregan nada nuevo: corrigen lo visible, graban un video de respaldo y congelan la versión. Antes de las **14:45 h** entreguen el checklist ético y la declaración de transparencia. Pitch entre las **16:15 y las 18:15 h**: **5 minutos de pitch con demo y 3 de preguntas del jurado**. Se evalúa la versión congelada al **cierre técnico (14:45 h)**: lo que cambien después no cuenta.

- [ ] Usuario y problema en una frase
- [ ] La app lee su planilla, sin filas ignoradas
- [ ] Antes y después con el mismo caso
- [ ] Al menos 5 intentos de mal uso probados
- [ ] 3 indicadores de impacto
- [ ] Checklist ético y declaración de transparencia entregados
- [ ] Registro descargado y video de respaldo
