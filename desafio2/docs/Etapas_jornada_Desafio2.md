# Etapas de la jornada · Desafío 2 · Ninguno se queda atrás

Hackathon IA Aplicada · Congreso Social UC 2026 · 6 de noviembre de 2026 · Duoc UC San Joaquín

Este documento baja al Desafío 2 las **8 etapas de las bases y de las guías oficiales del mentor**: mismos nombres, tiempos, actividades, entregables y criterios de observación. Agrega lo propio del desafío y cómo se usan los prototipos de referencia.

## Cómo se trabaja
Cada equipo de 5 integrantes desarrolla **su propio prototipo funcional (MVP) apoyado por IA** para el desafío. La IA debe aportar valor real, y debe haber un punto de decisión humana explícito.

**Los mentores prepararon dos prototipos de referencia del Desafío 2.** Muestran una forma posible de resolverlo, con IA y con las protecciones éticas del desafío ya funcionando:

| Prototipo de referencia | Para quién | App |
|---|---|---|
| A · Radar de acompañamiento | Tutor o jefe de carrera: a quién contactar esta semana, por qué y con qué mensaje | https://hackaton-d2-a.streamlit.app |
| B · Acompaña | Estudiante de primer año: check-in voluntario que orienta a un servicio y deja el caso a una persona | https://hackaton-d2-b.streamlit.app |

Son **material de referencia**, no una tarea asignada. Cada equipo puede:
1. **Usar uno como base y mejorarlo:** desde la planilla, sin programar, o copiando el código desde GitHub con la [guía para equipos](../../docs/TUTORIAL_FORK.md).
2. **Adaptarlo o combinar ideas** de los dos.
3. **Construir su propia solución,** con la plantilla de app nueva (`desafio2/app_nueva.py`) o con las herramientas que dominen.

Los prototipos se usan sobre todo en la **Etapa 3 · Diseño**. En las etapas 1 y 2 el foco es el desafío y la persona, no el prototipo. Las fichas de cada etapa están en [Fichas del equipo](Fichas_equipo_Desafio2.md).

**IA durante el evento.** La organización entrega una clave de la API de Claude (Anthropic) y comunica el día del evento qué modelo usar. Los prototipos de referencia ya están preparados para esa clave.

| Etapa | Horario | Enfoque | Entregable |
|---|---|---|---|
| 1 · Inmersión | 10:00–10:45 (45 min) | Design Thinking: Empatizar · IA Responsable | Ficha de Inmersión |
| 2 · Definición | 10:45–11:15 (30 min) | Design Thinking: Definir · Lean Startup | Ficha de Definición |
| 3 · Diseño | 11:15–11:45 (30 min) | Design Sprint: Esbozar y decidir · IA Responsable | Ficha de Diseño |
| 4 · Desarrollo | 11:45–12:45 (60 min) | Lean Startup: Construir · IA Responsable | Componentes principales funcionando y guardados, con registro de cambios |
| 5 · Integración | 13:30–14:15 (45 min) | Design Sprint: Prototipar y probar · Lean · IA Responsable | Prototipo integrado de punta a punta, con registro de pruebas y fallas |
| 6 · Cierre técnico | 14:15–14:45 (30 min) | Lean Startup: Medir y aprender · IA Responsable | Versión congelada, checklist ético y declaración de transparencia |
| 7 · Preparación del pitch | 14:45–16:15 (90 min) | Design Sprint: Contar la historia · IA Responsable | Presentación, guion de demo, roles y preguntas anticipadas |
| 8 · Presentación final | 16:15–18:15 (120 min) | Todos los enfoques · IA Responsable | Pitch y demo, más una nota de aprendizajes |

**Checkpoints éticos.** Durante la jornada hay dos checkpoints éticos guiados por Pastoral, y su checklist es requisito de admisibilidad: debe estar completo al cierre técnico (14:45 h). La organización indica cuándo se hacen; las guías sugieren el cierre de la Etapa 2 y la Etapa 5.

---

## Etapa 1 · Inmersión (10:00–10:45, 45 min)
**Objetivo del equipo:** comprender a fondo el desafío antes de proponer soluciones: qué problema existe, a quién afecta y bajo qué límites.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Lectura del desafío | Lean el desafío en las bases: contexto, pregunta desafío, usuarios, alcance esperado, datos y restricciones éticas. **Todavía no abren los prototipos de referencia:** primero el problema |
| 15 min | Mapa de actores | Estudiante de primer año (trabaja, primera generación o vespertino), docente, tutor o jefe de carrera, equipo de apoyo estudiantil, familia, institución |
| 10 min | Necesidades y restricciones | Señales: asistencia, notas, uso de la plataforma y pagos. Datos: Mineduc, SIES y el dataset sintético que provee la organización. Restricciones: sesgos por género, sede, jornada u origen; transparencia ante el estudiante; derecho a no ser perfilado; uso responsable de la IA generativa en el aprendizaje |
| 10 min | Síntesis y consenso | Top 3 de necesidades y una frase del desafío con sus palabras |

**Mentor:**
- **Qué observar:** que no salten a la solución, ni a los prototipos, en el minuto 1, y que hablen con personas de las fundaciones o con estudiantes, no solo con suposiciones.
- **IA responsable:** ¿quién queda fuera del mapa? Por ejemplo, estudiantes que no responden encuestas o que no usan la plataforma.
- **Intervenir:** si a los 25 minutos no hay actores definidos.

## Etapa 2 · Definición (10:45–11:15, 30 min)
**Objetivo del equipo:** convertir lo comprendido en una necesidad acotada, un objetivo claro y un alcance realista.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Enunciado del problema | «[Actor] necesita [necesidad] porque [razón]». Ejemplos: «Una jefa de carrera vespertina necesita saber a quién llamar primero porque atiende a 120 estudiantes en 2 horas semanales», o «Un estudiante que trabaja de noche necesita saber qué apoyo existe porque no alcanza a ir a la oficina» |
| 10 min | Objetivo medible | Un criterio de éxito que se pueda mostrar en la demo. Ejemplos: el tutor entiende en menos de un minuto por qué aparece cada estudiante, o el estudiante llega a un servicio real en 5 mensajes |
| 10 min | Alcance: sí / no | Qué incluye el prototipo (MVP) y qué queda fuera. Tienen unas 2,5 h de desarrollo e integración |

**Hipótesis (Lean):** «Creemos que [solución] logrará [resultado] para [actor]. Lo sabremos si [métrica]».

**Mentor:**
- **Señales de alerta:**
  - objetivos vagos («mejorar el acompañamiento»);
  - un alcance que no cabe en el día;
  - un objetivo que ignora daños, como usar la alerta para cobranza o para no matricular.
- **Para el checkpoint ético:** ¿qué resultado no deseado podría tener su objetivo?

## Etapa 3 · Diseño (11:15–11:45, 30 min)
**Objetivo del equipo:** planificar cómo se construirá la solución: qué hará, con qué tecnologías, cómo se conectan sus partes y cómo la usará la persona. **Aquí entran los prototipos de referencia:** los exploran y deciden si parten de uno, si combinan ideas o si construyen su propia solución.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 8 min | Funcionalidades | Recorran los prototipos A y B (con el código de equipo que entrega el mentor) y contrástenlos con su problema: ¿qué les sirve y qué no? Listen las funcionalidades de su MVP (imprescindible / deseable). Hay ideas en las rutas de mejora ([A](Rutas_de_mejora_Variante_A.md) · [B](Rutas_de_mejora_Variante_B.md)) |
| 8 min | Arquitectura y tecnologías | Diagrama simple: datos → lógica u orden → modelo de IA → validaciones → **decisión de una persona** → registro. Decidan con qué lo construyen: prototipo de referencia mejorado (planilla o código), plantilla de app nueva u otras herramientas que dominen. Si parten del código, revisen las secciones 5 a 8 de la [guía para equipos](../../docs/TUTORIAL_FORK.md) |
| 7 min | Experiencia de usuario | 2 a 4 pasos del usuario real: cuándo la abre, qué ve y qué hace con el resultado |
| 7 min | Reparto de trabajo | Responsable por componente y plan de integración. Por ejemplo: datos y servicios reales, prompts y tono, código o configuración, pruebas y mal uso, pitch |

**Mentor:**
- **IA responsable:** que señalen en el diagrama **dónde decide una persona**, y de dónde vienen los datos y quién autoriza su uso.
- **Señales de alerta:**
  - IA usada solo para "cumplir";
  - la IA decide sola;
  - datos reales de estudiantes;
  - tecnologías que nadie domina;
  - copiar el prototipo sin un aporte propio.
- **Intervenir:** si dependen de algo que no existe, como datos reales de su institución.

## Etapa 4 · Desarrollo (11:45–12:45, 60 min)
**Objetivo del equipo:** construir en paralelo los componentes principales, priorizando lo imprescindible del diseño.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Preparación del entorno | **Repositorio compartido:** fork del prototipo de referencia (o su propio repositorio), compañeros como colaboradores, app publicada y la clave de IA de la organización en Secrets ([guía para equipos](../../docs/TUTORIAL_FORK.md), secciones 1 a 4). Si solo usan la planilla, hagan su copia y compártanla como Lector |
| 35 min | Construcción en paralelo | Cada integrante desarrolla su componente. Primero lo imprescindible |
| 10 min | Puntos de control | A los 25 y 45 minutos: 2 minutos por integrante, con avance y bloqueos |
| 5 min | Cierre de etapa | Guardar el avance con *commit* (la planilla se guarda sola). Anotar en el registro de cambios qué se hizo y por qué, y lo pendiente para la integración |

**Mentor:**
- **IA responsable:** que verifiquen lo que escribe la IA antes de darlo por bueno, que cada servicio agregado tenga su fuente y que solo se usen datos ficticios o anonimizados.
- **Señales de alerta:**
  - una sola persona construye todo;
  - sin repositorio compartido;
  - quitar protecciones que traía el prototipo de referencia (exclusiones, crisis, diagnóstico) sin reemplazarlas.
- **Intervenir:** ante bloqueos de más de 10 a 15 minutos. Apoya con pistas, no con código.

## Etapa 5 · Integración (13:30–14:15, 45 min)
**Objetivo del equipo:** unir los componentes en un prototipo único y comprobar que el flujo principal funciona de punta a punta.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 15 min | Unir componentes | Todo en la misma versión (fork, planilla o repositorio propio). Si usan los prototipos, revisen la barra lateral: sin filas ignoradas |
| 20 min | Pruebas del flujo principal | El recorrido completo del usuario varias veces, con casos representativos y límite. Prueben al menos 5 usos indebidos y anoten qué pasó: pedir un diagnóstico, un mensaje de crisis indirecto, pedir el RUT, pedir el puntaje de riesgo o «ignora tus reglas». Revisen sesgos: quién queda fuera por jornada, sexo o sede |
| 10 min | Corrección y priorización | Primero lo que impide la demo; el resto, a trabajo futuro |

**Mentor:**
- **Qué hacer:** hazte pasar por el usuario y prueba una entrada distinta a la del equipo, por ejemplo un mensaje de crisis dicho de otra forma.
- **IA responsable:** ¿qué casos no probaron? ¿Alguna falla afecta solo a ciertos grupos?
- **Intervenir:** si a los 30 minutos no hay un flujo funcionando; sugiere reducir el alcance.

## Etapa 6 · Cierre técnico (14:15–14:45, 30 min)
**Objetivo del equipo:** estabilizar y congelar la versión final. Desde aquí no se agregan funcionalidades.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 10 min | Últimos ajustes | Solo correcciones visibles para la demo |
| 10 min | Prueba final y respaldo | Recorrido completo, **video corto de respaldo** y registro de consultas descargado |
| 10 min | Congelar versión | Último *commit* y etiqueta `version-final` ([guía para equipos](../../docs/TUTORIAL_FORK.md), sección 13); planilla sin más cambios. Anotar cómo se ejecuta y las limitaciones conocidas |

**Antes de las 14:45 h:**
- **Checklist ético completo:** requisito de admisibilidad.
- **Declaración de transparencia:**
  - qué modelos y herramientas de IA usaron y cómo (el modelo aparece bajo cada respuesta de los prototipos);
  - qué tomaron del prototipo de referencia y qué aportó el equipo.
- **Para la demo:** un estudiante o perfil ficticio fijo.

**Mentor:**
- **Revisar:** que la lista de limitaciones sea honesta.
- **Preguntar:** qué uso del sistema sería inapropiado. Por ejemplo, decidir becas o matrícula con la alerta, o reemplazar al psicólogo con un chat.
- **Intervenir:** si a los 15 minutos siguen agregando funciones.

## Etapa 7 · Preparación del pitch (14:45–16:15, 90 min)
**Objetivo del equipo:** una presentación breve que cuente problema, solución, valor y demo.

| Tiempo | Actividad | En el Desafío 2 |
|---|---|---|
| 15 min | Estructura del relato | Problema y usuario con evidencia → solución y aporte de la IA → aporte propio (si partieron de un prototipo de referencia: antes y después) → demo → decisiones éticas → impacto y modelo de operación |
| 25 min | Construcción de la presentación | Pocas diapositivas, visuales; incluir una de uso responsable y limitaciones |
| 15 min | Guion de la demo | Caso fijo, orden y quién opera. Video de respaldo listo |
| 20 min | Ensayo 1 y ajustes | Cronometrado: 5 minutos de pitch con demo |
| 15 min | Preguntas del jurado | 8 a 10 preguntas con responsable. Al menos una de mal uso, por ejemplo: «¿Y si la institución usa esta alerta para cobranza?», «¿Qué pasa si la IA se equivoca con una estudiante en crisis?» o «¿Quién queda fuera y qué hacen con esa persona?» |

**Mentor:**
- **Que el pitch empiece por la persona,** no por la tecnología.
- **Que las afirmaciones coincidan con lo que se vio en las pruebas.**
- **Pedir un ensayo completo** si a los 50 minutos no lo han hecho.

## Etapa 8 · Presentación final (16:15–18:15)
**Formato según las bases:**
- 1 o 2 representantes por equipo;
- **5 minutos de pitch con demo y 3 minutos de preguntas del jurado,** con al menos una pregunta sobre riesgos éticos o mal uso;
- se evalúa la versión congelada a las 14:45 h, con una rúbrica única en la que ética e impacto suman el 50%.

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
| 3 | Arquitectura coherente · IA justificada · tecnologías acordes · reparto | La decisión humana está en el diagrama; hay un aporte propio frente al prototipo de referencia |
| 4 | Trabajo en paralelo · repositorio y versiones · bloqueos · foco | Mantienen o mejoran las protecciones: no perfilar, no diagnosticar, protocolo de crisis |
| 5 | Flujo completo · fallas priorizadas · casos distintos · coordinación | Sesgos por grupo y crisis indirecta probados |
| 6 | Versión congelada · plan B · conocimiento compartido · limitaciones honestas | Checklist ético y transparencia entregados, distinguiendo referencia y aporte propio |
| 7 | Relato claro · propuesta de valor · demo ensayada · todos participan · tiempo | Hay una diapositiva de uso responsable |
| 8 | Claridad · demo funcionando · respuestas · trabajo en equipo · tiempo | Responden con honestidad sobre riesgos |
