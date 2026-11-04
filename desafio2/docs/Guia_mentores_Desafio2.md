# Guía para mentores · Desafío 2 · Ninguno se queda atrás

Tu trabajo es que cada equipo llegue a las **14:45 h** con un prototipo propio, probado y argumentado. Acompañas a 4 equipos con las **guías oficiales del mentor** (8 etapas). Este documento agrega lo propio del Desafío 2.

**Los prototipos A y B son material de referencia,** no una tarea asignada. Los equipos pueden:
- mejorarlos desde la planilla o copiando el código desde GitHub ([guía para equipos](../../docs/TUTORIAL_FORK.md));
- combinarlos;
- construir su propia solución.

Se presentan en la **Etapa 3 · Diseño**. En las etapas 1 y 2 el foco es el desafío y la persona.

| Prototipo de referencia | App | Planilla base |
|---|---|---|
| A · Radar de acompañamiento | https://hackaton-d2-a.streamlit.app | La entrega la organización |
| B · Acompaña | https://hackaton-d2-b.streamlit.app | La entrega la organización |

A cada equipo le entregas su código y clave, que sirven en las dos apps, y en la Etapa 3 los enlaces a las apps y a las planillas base.

## Tu rol en cada etapa
Detalle por etapa (actividades, señales de alerta y criterios de observación) en [Etapas de la jornada](Etapas_jornada_Desafio2.md). Los equipos completan las [Fichas del equipo](Fichas_equipo_Desafio2.md).

| Etapa | Tu foco en el Desafío 2 |
|---|---|
| 1 · Inmersión | Que entiendan el desafío antes de ver los prototipos y conversen con personas reales |
| 2 · Definición | Recortar: objetivo medible y alcance que quepa en el día. Para el checkpoint ético: ¿qué daño podría causar su objetivo? |
| 3 · Diseño | Presentar los prototipos de referencia y ayudar a decidir: partir de uno, combinar o crear el suyo. Que el diagrama muestre dónde decide una persona y cuál es el aporte propio |
| 4 · Desarrollo | Desbloquear sin construir por ellos; que mantengan o mejoren las protecciones (no perfilar, no diagnosticar, protocolo de crisis) |
| 5 · Integración | Probar como usuario: sesgos por grupo y crisis indirecta |
| 6 · Cierre técnico | Congelar, respaldo de la demo, checklist ético y transparencia antes de las 14:45 h |
| 7 · Preparación del pitch | Ensayo cronometrado, diapositiva de uso responsable, preguntas de mal uso |
| 8 · Presentación final | No intervenir; después, 2 fortalezas, 1 mejora y una observación ética |

Los dos **checkpoints éticos** los guía Pastoral; su checklist debe estar completo al cierre técnico.

## Antes de la jornada
- [ ] Entrar a ambas apps con **tu código de mentor** (M01, M02…, lo entrega la organización) y recorrer un caso completo (A: ficha y decisión; B: check-in y bandeja). Tu código tiene cuota propia: no gasta las consultas de ningún equipo
- [ ] Probar un mensaje de crisis indirecto en B
- [ ] Tener la tabla de códigos y claves de tus equipos
- [ ] Revisar las rutas de mejora, `Riesgos_eticos_Desafio2.md` y las [Etapas de la jornada](Etapas_jornada_Desafio2.md)
- [ ] Llevar las fichas de cada etapa para tus 4 equipos (impresas o compartidas)
- [ ] El día del evento, abrir ambas apps antes de las 9:00 h: se duermen tras 12 horas sin uso

## Datos para orientar
Dataset **sintético** de 3.000 estudiantes; deserta el 29,1%.

| Condición | Deserta con | Deserta sin |
|---|---|---|
| Arancel atrasado | 61,4% | 27,0% |
| Trabajo por turnos | 47,9% | 26,1% |
| Jornada vespertina (vs. diurna) | 38,4% | 25,4% |
| Personas a su cuidado | 37,7% | 26,7% |
| Primera generación | 30,2% | 25,9% |

**Sesgo (Variante A):** el modelo no usa sexo, sede ni tipo de colegio (AUC 0,86), pero con cupo del 15% la cola incluye al 25,6% de los vespertinos y al 10,7% de los diurnos, y alcanza al 48% de los hombres que desertan frente al 32% de las mujeres. La pestaña **¿A quién deja fuera?** lo muestra en un gráfico.

## Errores frecuentes
| Error | Qué decir |
|---|---|
| Planilla no compartida | Compartir → Cualquier persona con el vínculo · Lector |
| Editar la columna `campo` o renombrar pestañas | Editar solo `valor` |
| Editar y no recargar | Presionar "Recargar configuración" |
| `instrucciones_extra` contra las reglas | Las reglas fijas mandan: reformular |
| Querer construirlo todo | "Elijan una ruta. ¿Cuál defenderían en 5 minutos?" |
| Pitch que empieza por la tecnología | "Cuéntenme de una persona: ¿quién es y qué le pasa?" |
| "Respuesta de demostración" | Esperar un minuto; si persiste, avisar a la organización |

## Cómo destrabar a un equipo (5 minutos)
1. **Técnico:** revisar la barra lateral (origen de la configuración, filas ignoradas). Si nada carga, borrar la URL y seguir con la base.
2. **Sin dirección:** "**[usuario]** necesita **[algo]** cuando **[momento]**".
3. **Ética trabada:** Ruta 6, "Probar el mal uso antes que el jurado".
4. **Sin flujo funcionando a los 30 minutos de la Etapa 5:** reducir alcance y asegurar un recorrido mínimo.
5. **Al empezar el cierre técnico (14:15 h) sin demo estable:** dejar de agregar, asegurar lo que funciona, grabar un minuto de respaldo y argumentar.

## Preguntas del jurado para ensayar
- "¿Y si la institución usa esta lista para no matricular a alguien o para cobranza?"
- "¿Qué pasa si la IA se equivoca con una estudiante en crisis?"
- "¿Quién queda fuera de la cola y qué hacen con esa persona?"
- "¿Cómo sabrían en un semestre real si esto retuvo a alguien?"
