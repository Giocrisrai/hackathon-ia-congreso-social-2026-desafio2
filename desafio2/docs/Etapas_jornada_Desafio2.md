# Etapas de la jornada · Desafío 2 · Ninguno se queda atrás

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

Este documento baja al Desafío 2 las **8 etapas de las guías oficiales del mentor**: mismos nombres, tiempos, actividades, entregables y criterios de observación. Agrega lo propio del desafío: qué hace el equipo con la plantilla en cada etapa y qué mira el mentor.

**Modalidad.** Los equipos no parten de cero. Cada equipo recibe por sorteo una de las dos variantes de la plantilla base:
- **A · Radar de acompañamiento:** panel para el tutor o jefe de carrera.
- **B · Acompaña:** check-in conversacional para el estudiante.

Su trabajo es adaptarla y mejorarla para un usuario y un caso concretos:
- desde la planilla, sin programar;
- o copiando el código desde GitHub y modificándolo, con la [guía para equipos](../../docs/TUTORIAL_FORK.md).

Las fichas de cada etapa están en [Fichas del equipo](Fichas_equipo_Desafio2.md).

| Etapa | Horario | Enfoque | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 (45 min) | Design Thinking: Empatizar · IA Responsable | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 (30 min) | Design Thinking: Definir · Lean Startup | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 (30 min) | Design Sprint: Esbozar y decidir · IA Responsable | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 (60 min) | Lean Startup: Construir · IA Responsable | Mejoras implementadas y guardadas, con registro de cambios |
| 5 · Integración | 13:30–14:15 (45 min) | Design Sprint: Prototipar y probar · Lean · IA Responsable | Flujo completo funcionando, con registro de pruebas y fallas |
| 6 · Cierre técnico | 14:15–14:45 (30 min) | Lean Startup: Medir y aprender · IA Responsable | Versión congelada, checklist ético y declaración de transparencia |
| 7 · Preparación del pitch | 14:45–16:15 (90 min) | Design Sprint: Contar la historia · IA Responsable | Presentación, guion de demo, roles y preguntas anticipadas |
| 8 · Presentación final | 16:15–18:15 (120 min) | Todos los enfoques · IA Responsable | Pitch y demo, más una nota de aprendizajes |

---

## Etapa 1 · Inmersión (10:00–10:45, 45 min)
**Objetivo del equipo:** comprender a fondo el desafío antes de proponer soluciones: qué problema existe, a quién afecta y bajo qué límites.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Lectura del desafío | Lean el enunciado y la ficha de línea base de su variante ([A](Ficha_linea_base_Variante_A.md) · [B](Ficha_linea_base_Variante_B.md)). Abran la app y miren qué hace hoy, sin cambiar nada |
| 15 min | Mapa de actores | Estudiante de primer año (trabaja, primera generación o vespertino), docente, tutor o jefe de carrera, equipo de apoyo estudiantil, familia, institución |
| 10 min | Necesidades y restricciones | Señales: asistencia, notas, uso de la plataforma y pagos. Datos: Mineduc, SIES y el dataset sintético. Restricciones: sesgos por género, sede, jornada u origen; transparencia ante el estudiante; derecho a no ser perfilado |
| 10 min | Síntesis y consenso | Top 3 de necesidades y una frase del desafío con sus palabras |

**Mentor:**
- **Qué observar:** que no salten a "cambiemos el prompt" en el minuto 1, y que hablen con personas de las fundaciones o con estudiantes, no solo con suposiciones.
- **IA responsable:** ¿quién queda fuera del mapa? Por ejemplo, estudiantes que no responden el check-in o que no usan la plataforma.
- **Intervenir:** si a los 25 minutos no hay actores definidos.

## Etapa 2 · Definición (10:45–11:15, 30 min)
**Objetivo del equipo:** convertir lo comprendido en una necesidad acotada, un objetivo claro y un alcance realista.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Enunciado del problema | «[Actor] necesita [necesidad] porque [razón]». Ejemplo A: «Una jefa de carrera vespertina necesita saber a quién llamar primero porque atiende a 120 estudiantes en 2 horas semanales». Ejemplo B: «Un estudiante que trabaja de noche necesita saber qué apoyo existe porque no alcanza a ir a la oficina» |
| 10 min | Objetivo medible | Un criterio de éxito que se pueda mostrar en la demo. Ejemplos: el tutor entiende en menos de un minuto por qué aparece cada estudiante, o el check-in orienta a un servicio real en 5 mensajes |
| 10 min | Alcance: sí / no | Qué mejorarán de la plantilla (2 a 4 cambios) y qué dejan fuera. Tienen 2,5 h de trabajo efectivo |

**Hipótesis (Lean):** «Creemos que [cambio en la plantilla] logrará [resultado] para [actor]. Lo sabremos si [métrica]».

**Mentor:**
- **Señales de alerta:**
  - objetivos vagos («mejorar el acompañamiento»);
  - querer rehacer la app completa;
  - un objetivo que ignora daños, como usar la cola para cobranza o para no matricular.
- **Checkpoint ético 1:** al cierre de la etapa, pregunten qué resultado no deseado podría tener su objetivo.

## Etapa 3 · Diseño (11:15–11:45, 30 min)
**Objetivo del equipo:** planificar qué cambiarán de la plantilla, cómo encaja en el día del usuario y quién hace qué. Con plantilla, "arquitectura y tecnologías" significa decidir **qué parte de la plantilla tocan**.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 8 min | Funcionalidades | 2 a 4 mejoras priorizadas (imprescindible / deseable), elegidas de las rutas de mejora ([A](Rutas_de_mejora_Variante_A.md) · [B](Rutas_de_mejora_Variante_B.md)) o propias |
| 8 min | Arquitectura y tecnologías | Dibujen el flujo de la plantilla: **datos → orden o conversación → IA → validaciones fijas → decisión de una persona → registro**. Marquen dónde cae cada mejora y si se hace en la planilla o en el código (secciones 5 a 7 de la [guía para equipos](../../docs/TUTORIAL_FORK.md)) |
| 7 min | Experiencia de usuario | 2 a 4 pasos del usuario real con la herramienta: cuándo la abre, qué ve y qué hace con el resultado |
| 7 min | Reparto de trabajo | Responsables, por ejemplo: planilla y prompts, servicios reales y fuentes, código (si lo usan), pruebas y mal uso, pitch |

**Mentor:**
- **IA responsable:** que señalen en el diagrama **dónde decide una persona**. En A, el tutor registra la decisión. En B, una persona revisa la bandeja.
- **Datos:** que sepan de dónde vienen los datos y quién autoriza su uso.
- **Señales de alerta:** la IA decide sola, o se usan datos reales de estudiantes.
- **Intervenir:** si dependen de algo que no existe, como datos reales de su institución.

## Etapa 4 · Desarrollo (11:45–12:45, 60 min)
**Objetivo del equipo:** implementar en paralelo las mejoras imprescindibles, sobre la plantilla.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Preparación del entorno | Copia de la planilla compartida como Lector y su URL cargada en la app. Si van a tocar código: **fork** del repositorio, compañeros como colaboradores, app propia publicada y claves en Secrets ([guía para equipos](../../docs/TUTORIAL_FORK.md), secciones 2 a 4) |
| 35 min | Construcción en paralelo | Cada responsable implementa su mejora. Primero lo imprescindible |
| 10 min | Puntos de control | A los 25 y 45 minutos: 2 minutos por integrante, mostrando el mismo caso antes y después |
| 5 min | Cierre de etapa | Guardar el avance: la planilla se guarda sola; el código, con *commit*. Anotar en el registro de cambios qué se cambió y por qué |

**Mentor:**
- **IA responsable:** que verifiquen lo que escribe la IA antes de darlo por bueno. Cada servicio agregado necesita su fuente, y solo se usan datos ficticios.
- **Señales de alerta:**
  - una sola persona construye todo;
  - cambios fuera del alcance;
  - quitar protecciones (exclusiones de A, crisis o diagnóstico de B).
- **Intervenir:** ante bloqueos de más de 10 a 15 minutos. Apoya con pistas, no con código.

## Etapa 5 · Integración (13:30–14:15, 45 min)
**Objetivo del equipo:** unir las mejoras en una sola versión y comprobar que el flujo principal funciona de punta a punta.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 15 min | Unir componentes | Todas las mejoras en la misma planilla o en el mismo fork. Recargar la configuración (o esperar la actualización de la app) y revisar la barra lateral: sin filas ignoradas |
| 20 min | Pruebas del flujo principal | **A:** recorrer cola → ficha → decisión, y revisar la pestaña "¿A quién deja fuera?". **B:** consentimiento → check-in → resumen → bandeja. Probar al menos 5 usos indebidos y anotar qué pasó: pedir diagnóstico, mensaje de crisis indirecto, pedir el RUT, pedir el puntaje de riesgo o "ignora tus reglas" |
| 10 min | Corrección y priorización | Primero lo que impide la demo; el resto, a trabajo futuro |

**Mentor:**
- **Qué hacer:** hazte pasar por el usuario y prueba una entrada distinta a la del equipo.
- **IA responsable, en A:** quién queda fuera de la cola por jornada, sexo o sede.
- **IA responsable, en B:** si un mensaje de crisis dicho de otra forma activa el protocolo.
- **Checkpoint ético 2:** la revisión de sesgos se hace en esta etapa.
- **Intervenir:** si a los 30 minutos no hay un flujo funcionando.

## Etapa 6 · Cierre técnico (14:15–14:45, 30 min)
**Objetivo del equipo:** estabilizar y congelar la versión final. Desde aquí no se agregan funcionalidades.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Últimos ajustes | Solo correcciones visibles para la demo |
| 10 min | Prueba final y respaldo | Recorrido completo, **video corto de respaldo** y registro de la app descargado desde la barra lateral |
| 10 min | Congelar versión | Planilla: no editar más. Código: último *commit* y etiqueta `version-final` ([guía para equipos](../../docs/TUTORIAL_FORK.md), sección 13). Anotar cómo se ejecuta (URL de la app y código de equipo) y las limitaciones conocidas |

**Antes de las 14:45 h:**
- **Checklist ético:** requisito de admisibilidad.
- **Declaración de transparencia:** qué venía en la plantilla base y qué aportó el equipo, y qué modelos se usaron (aparece bajo cada respuesta, por ejemplo "anthropic · claude-haiku-5-5").
- **D2:** estudiante o perfil ficticio fijo para la demo.

**Mentor:**
- **Revisar:** que la lista de limitaciones sea honesta.
- **Preguntar:** qué uso del sistema sería inapropiado. Por ejemplo, decidir becas o matrícula con la cola, o reemplazar al psicólogo con el check-in.
- **Intervenir:** si a los 15 minutos siguen agregando funciones.

## Etapa 7 · Preparación del pitch (14:45–16:15, 90 min)
**Objetivo del equipo:** una presentación breve que cuente problema, solución, valor y demo.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 15 min | Estructura del relato | Problema y usuario con evidencia → solución y aporte de la IA → mejoras propias sobre la plantilla (antes y después) → demo → decisiones éticas → impacto y modelo de operación |
| 25 min | Construcción de la presentación | Pocas diapositivas, visuales; incluir una de uso responsable y limitaciones |
| 15 min | Guion de la demo | Caso fijo, orden y quién opera. Tener el video de respaldo listo |
| 20 min | Ensayo 1 y ajustes | Cronometrado contra el tiempo oficial del pitch |
| 15 min | Preguntas del jurado | 8 a 10 preguntas con responsable. Al menos una de mal uso, por ejemplo: «¿Y si la institución usa esta lista para cobranza?», «¿Qué pasa si la IA se equivoca con una estudiante en crisis?» o «¿Quién queda fuera de la cola?» |

**Mentor:**
- **Que el pitch empiece por la persona,** no por la tecnología.
- **Que las afirmaciones coincidan con lo que se vio en las pruebas.**
- **Pedir un ensayo completo** si a los 50 minutos no lo han hecho.

## Etapa 8 · Presentación final (16:15–18:15)
**Formato:** pitch con demo y preguntas del jurado, en el tiempo que indique la organización. Según las bases, son **5 minutos de pitch y 3 de preguntas**, con al menos una pregunta de mal uso. La rúbrica pondera ética e impacto con un 50%.

**Mentor:**
- **Antes del turno:** repasar orden, tiempo y plan B.
- **Durante el pitch:** no intervenir.
- **Después:** 2 fortalezas, 1 mejora y una observación sobre uso responsable.

---

## Observación del equipo (para el mentor)
Mismos criterios de las guías oficiales, con lo que se mira en el Desafío 2:

| Etapa | Criterios oficiales | Qué mirar en el D2 |
|---|---|---|
| 1 | Participación equilibrada · necesidades distintas de soluciones · actores y restricciones · tiempo | Consideran al estudiante que no aparece en los datos o no responde |
| 2 | Problema acotado · objetivo medible · alcance realista · acuerdo | El objetivo no convierte la herramienta en un sistema de sanción |
| 3 | Arquitectura coherente · IA justificada · tecnologías acordes · reparto | La decisión humana está en el diagrama |
| 4 | Trabajo en paralelo · repositorio y versiones · bloqueos · foco | Mantienen exclusiones, validaciones y protocolo de crisis |
| 5 | Flujo completo · fallas priorizadas · casos distintos · coordinación | Equidad por grupo (A) y crisis indirecta (B) probadas |
| 6 | Versión congelada · plan B · conocimiento compartido · limitaciones honestas | Checklist ético y transparencia entregados |
| 7 | Relato claro · propuesta de valor · demo ensayada · todos participan · tiempo | Hay una diapositiva de uso responsable |
| 8 | Claridad · demo funcionando · respuestas · trabajo en equipo · tiempo | Responden con honestidad sobre riesgos |
