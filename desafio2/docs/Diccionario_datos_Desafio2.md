# Diccionario de datos · Desafío 2

**Todos los datos son sintéticos (inventados).** Ninguna fila corresponde a una persona, sede o institución real. Las proporciones se calibraron a grandes rasgos con cifras públicas (SIES, retención de 1er año; Mineduc, Ficha de Caracterización Única piloto 2024) solo para que se vean verosímiles. Licencia: CC BY 4.0.

## estudiantes_sinteticos_desafio2.csv (3.000 filas · usado por la Variante A)

Un estudiante ficticio de primer año por fila. El perfil se parece al de un IP o CFT (donde más se concentra la deserción). El desafío abarca toda la educación superior: los equipos pueden discutir cómo cambiaría el perfil en una universidad. Origen de todos los campos: **generados por script** (`src/` del kit de mentoría), con semilla fija.

| Campo | Significado | Valores |
|---|---|---|
| id_estudiante | Identificador ficticio | EST-00001… |
| sede | Sede genérica (**solo para auditar sesgos, no para predecir**) | Sede Centro, Norte, Sur, Oriente, Poniente, Regional |
| area_carrera | Área de la carrera | 7 áreas |
| tipo_carrera | Técnica o profesional | Técnica / Profesional |
| sexo | **Solo para auditar sesgos** | Femenino / Masculino / No binario |
| edad | Edad al ingresar | 17–58 |
| jornada | Jornada de estudio | Diurna / Vespertina |
| tipo_establecimiento_origen | Liceo de origen (**solo para auditar**) | Municipal/SLEP, Particular subvencionado, Particular pagado |
| egreso_liceo_tp | Egresó de liceo técnico-profesional | 0 / 1 |
| anios_desde_egreso_media | Años desde que terminó la media | 0–40 |
| nem | Notas de enseñanza media | 4,0–7,0 (4% vacío) |
| primera_generacion | Primera generación en educación superior | 0 / 1 |
| gratuidad | Tiene gratuidad | 0 / 1 |
| horas_trabajo_semana | Horas de trabajo remunerado | 0–50 |
| trabajo_por_turnos | Trabaja por turnos | 0 / 1 |
| cuida_dependientes | Tiene personas a su cuidado | 0 / 1 |
| tiempo_traslado_min | Minutos de traslado a la sede | 5–150 (6% vacío) |
| asistencia_s1_s3_pct | Asistencia semanas 1 a 3 | % |
| asistencia_s4_s6_pct | Asistencia semanas 4 a 6 | % |
| evaluaciones_rendidas_pct | Evaluaciones rendidas a la semana 6 | % |
| nota_promedio_parcial | Promedio de notas parciales | 1,0–7,0 |
| entregas_atrasadas | Entregas atrasadas a la semana 6 | conteo |
| logins_lms_semana | Ingresos semanales a la plataforma | promedio (3% vacío) |
| dias_desde_ultimo_login | Días sin entrar a la plataforma | conteo |
| uso_tutoria | Ha usado tutorías | 0 / 1 |
| contacto_bienestar | Ha contactado a bienestar | 0 / 1 |
| arancel_atrasado | Arancel atrasado (sin gratuidad) | 0 / 1 |
| beneficio_en_riesgo | Gratuidad en riesgo | 0 / 1 |
| respuesta_checkin_s4 | Texto libre del check-in de la semana 4 | texto (43% no responde) |
| deserta_primer_anio | **Resultado:** no se matriculó en 2º año | 0 / 1 (29,1%) |
| motivo_declarado_salida | Motivo declarado al salir (**se conoce después: no usar para predecir**) | 7 categorías |

## Catálogo de servicios (base fija en la app, 9 filas · ambas variantes)
Servicios de apoyo **genéricos de una institución ficticia**, redactados por el tutor del desafío. Campos: `id_servicio` (S01–S09, el código que la IA debe citar), `categoria`, `nombre`, `para_que_sirve`, `cuando_sugerirlo`, `como_acceder`.

## Pestaña `servicios_extra` (planilla del equipo · ambas variantes)
Servicios que agrega el equipo. La fila EJEMPLO se ignora. Si una fila no cumple, la barra lateral la muestra como "ignorada" y dice qué corregir.

| Columna | Valores permitidos |
|---|---|
| id_servicio | Identificador propio corto (X01, X02…). No puede repetir S01–S09 |
| categoria | academico, economico, laboral, cuidado, bienestar, vocacional, organizacion, traslado |
| nombre, para_que_sirve, cuando_sugerirlo, como_acceder | Texto (obligatorios) |
| fuente_url | Enlace (http…) a la página oficial del servicio |
| origen_dato | real o sintético |

## Pestaña `config` (planilla del equipo)
Columnas `campo` · `valor` · `qué es` · `ejemplo`. Se edita solo `valor`; si queda vacío, se usa el valor de la plantilla base.
- **Ambas variantes:** usuario, tono, largo_respuesta, ejemplos, instrucciones_extra, titulo_app, texto_bienvenida, texto_boton.
- **Variante A:** cupo_porcentaje (5 a 40) y variables_excluidas (separadas por ;).
- **Variante B:** mensaje_inicial, texto_consentimiento y max_turnos (3 a 15).

## personas_checkin.csv (6 filas · Variante B · fijo en la app)
Personas **ficticias** para simular conversaciones, redactadas por el tutor a partir de perfiles frecuentes de la FCU 2024. Campos: `id_persona`, `nombre_ficticio`, `edad`, `carrera`, `jornada` y `contexto_para_simular` (no se envía a la IA).

## Registro de uso (lo genera la app)
Una línea por evento: `marca_tiempo`, `app`, `equipo`, `planilla`, `tipo` (ingreso, recarga_configuracion, llamada_ia, validacion, decision_humana, consentimiento, caso_creado, protocolo_crisis…), `tarea`, `modo` (real o demo), `proveedor`, `entrada`, `salida`, `decision`, `utilidad`, `nota`. Cada equipo descarga el suyo desde la barra lateral.
