# Guía para mentores · Desafío 2 · Ninguno se queda atrás

Tu trabajo es que cada equipo llegue a las **14:45 h** con **una** mejora bien hecha, probada y argumentada. Los equipos no programan: cambian la herramienta desde su copia de la planilla.

| Variante | App | Planilla base |
|---|---|---|
| A · Radar de acompañamiento | https://hackaton-d2-a.streamlit.app | La entrega la organización |
| B · Acompaña | https://hackaton-d2-b.streamlit.app | La entrega la organización |

A cada equipo le entregas su variante, el enlace a la app, su código y clave y el enlace a la planilla base.

## Antes de la jornada
- [ ] Entrar a ambas apps con un código de prueba y recorrer un caso completo (A: ficha y decisión; B: check-in y bandeja)
- [ ] Probar un mensaje de crisis indirecto en B
- [ ] Tener la tabla de códigos y claves con la variante de cada equipo
- [ ] Revisar las rutas de mejora y `Riesgos_eticos_Desafio2.md`
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
4. **A las 14:15 h sin demo estable:** congelar, grabar un minuto y argumentar.

## Preguntas del jurado para ensayar
- "¿Y si la institución usa esta lista para no matricular a alguien o para cobranza?"
- "¿Qué pasa si la IA se equivoca con una estudiante en crisis?"
- "¿Quién queda fuera de la cola y qué hacen con esa persona?"
- "¿Cómo sabrían en un semestre real si esto retuvo a alguien?"
