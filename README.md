# Hackathon IA Aplicada · Congreso Social UC 2026 · Desafío 2 · Ninguno se queda atrás

Plantillas del Desafío 2 (deserción en primer año de educación superior técnico-profesional). Cada equipo recibe una app que **ya funciona** y la adapta a un usuario real desde una planilla de Google, sin programar. Misma lógica que las plantillas del Desafío 3: código y clave por equipo, pestaña `config`, pestaña de extras con fila EJEMPLO, botón "Recargar configuración" y 120 consultas a la IA por equipo.

**Todos los datos son ficticios.**

| Variante | App en línea | Para quién | Qué hace |
|---|---|---|---|
| A · Radar de acompañamiento | https://hackaton-d2-a.streamlit.app | Tutor o jefatura de carrera | Ordena a quién contactar esta semana, explica por qué, prepara un borrador y muestra a quién deja fuera la cola |
| B · Acompaña | https://hackaton-d2-b.streamlit.app | Estudiante de primer año | Check-in conversacional voluntario que orienta a un servicio y deja el caso en una bandeja para una persona |

## Documentación
| Para | Documento |
|---|---|
| Participantes | [Guía para participantes](desafio2/docs/Guia_participantes_Desafio2.md) · README de la [Variante A](desafio2/docs/README_Variante_A.md) y la [Variante B](desafio2/docs/README_Variante_B.md) |
| Mentores | [Guía para mentores](desafio2/docs/Guia_mentores_Desafio2.md) · [Riesgos éticos](desafio2/docs/Riesgos_eticos_Desafio2.md) · [Prueba piloto](desafio2/docs/Prueba_piloto_Desafio2.md) |
| Rutas de mejora | [Variante A](desafio2/docs/Rutas_de_mejora_Variante_A.md) · [Variante B](desafio2/docs/Rutas_de_mejora_Variante_B.md) |
| Línea base y datos | Ficha de línea base [A](desafio2/docs/Ficha_linea_base_Variante_A.md) y [B](desafio2/docs/Ficha_linea_base_Variante_B.md) · [Diccionario de datos](desafio2/docs/Diccionario_datos_Desafio2.md) |
| Quien quiera su propia versión | [Tutorial: fork, despliegue y cambios por variante](docs/TUTORIAL_FORK.md) |

## Estructura
```
comun/nucleo_st.py              núcleo común: acceso por equipo, lectura de la planilla, IA multi-proveedor,
                                registro, validaciones fijas, protocolo de crisis y diseño
desafio2/app_a_panel_tutor.py   Variante A · Radar de acompañamiento
desafio2/app_b_checkin.py       Variante B · Acompaña
desafio2/servicios.py           catálogo de servicios y validación de servicios_extra
desafio2/datos/                 catálogo, perfiles ficticios y generador del dataset sintético (semilla 2026)
desafio2/planillas/             planilla base de cada variante, un CSV por pestaña
desafio2/docs/                  documentación del desafío
.streamlit/                     tema visual y plantilla de secrets (secrets.toml nunca se sube)
```

## IA con varios proveedores
La app prueba los proveedores en el orden de `[ia] orden` y, dentro de cada uno, los modelos de su lista `modelos`. Si un modelo falla o se satura, pasa al siguiente sin que el equipo lo note: los saturados se saltan 45 s y los que tienen clave o nombre inválido, 10 min. Si todos fallan, muestra una respuesta de demostración y la app sigue funcionando.

| Orden por defecto | Modelos |
|---|---|
| Groq | `openai/gpt-oss-120b` → `openai/gpt-oss-20b` |
| Mistral | `mistral-small-latest` → `ministral-8b-latest` |

Para sumar otra clave no hay que tocar código: se agrega al final de `orden` y se crea su bloque `[ia.<nombre>]` con `api_key` y `modelos`. Gemini, OpenRouter, Cerebras, Together, DeepSeek y OpenAI ya traen su dirección; otro proveedor compatible con OpenAI necesita además `url`. La barra lateral muestra la cadena en uso y bajo cada respuesta se indica qué modelo respondió.

## Protecciones fijas (no se cambian desde la planilla)
- Aviso de uso de IA, registro de consultas y respuestas, límite de consultas por equipo.
- Decisión humana obligatoria en ambas variantes.
- A: el orden nunca usa sexo, sede ni tipo de colegio; el borrador al estudiante no menciona riesgo, deserción, porcentajes ni predicciones y solo cita servicios del catálogo.
- B: consentimiento previo, la IA no diagnostica, protocolo de crisis con \*4141, Salud Responde 600 360 7777 y SAMU 131.
- Español de Chile con tuteo y sin inventar pasos de acceso a los servicios.

## Despliegue (organización)
1. En https://share.streamlit.io, crear dos apps desde este repositorio, rama `main`, Python 3.12, con *Main file* `desafio2/app_a_panel_tutor.py` y `desafio2/app_b_checkin.py`.
2. En cada app, **Settings → Secrets**: pegar `.streamlit/secrets.example.toml` con las claves de IA, un bloque `[equipos.EXX]` (nombre y clave) por equipo y uno `[equipos.MXX]` por mentor, para que prueben sin gastar la cuota de los equipos.
3. Subir las planillas base a Google Drive como Hojas de cálculo y compartirlas como Lector.
4. Abrir las apps antes de cada jornada: se duermen tras 12 horas sin uso. Para guardar el registro de forma permanente, configurar `[registro]` y `[gcp_service_account]`.

## Pruebas realizadas
- De punta a punta en navegador real (Chromium): ingreso, ficha y decisión, gráfico de equidad, consentimiento, check-in, protocolo de crisis y bandeja.
- Con IA real (Groq y Mistral, 30 de octubre de 2026): fichas validadas, check-in sin diagnóstico y cambio automático de proveedor en 5 escenarios (normal, proveedor caído, todos caídos, proveedor nuevo y formato antiguo de secrets).

## Licencia
Código bajo licencia MIT; datos sintéticos, planillas y documentación bajo CC BY 4.0. Ver [LICENSE](LICENSE).
