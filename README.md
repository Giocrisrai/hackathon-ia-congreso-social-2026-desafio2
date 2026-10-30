# Hackathon IA Congreso Social UC 2026 · Desafío 2 · Ninguno se queda atrás

Plantillas del Desafío 2 con **la misma lógica que las del Desafío 3** (G. Pinto): app pública con código y clave por equipo, y personalización desde una copia de una planilla de Google.

| Elemento | Cómo funciona |
|---|---|
| Acceso | Una app Streamlit pública por variante, con código y clave por equipo |
| Personalización | Copia de la planilla base: pestaña `config` (campo · valor · qué es · ejemplo) y pestaña `servicios_extra` con fila EJEMPLO |
| Fijo en la app | Aviso de IA, registro de consultas, límite de 120 consultas por equipo, reglas fijas, validación de respuestas y respuesta de demostración ante fallas |
| Botón | "Recargar configuración"; la barra lateral muestra las filas ignoradas y qué corregir |

## Variantes
| Variante | App (Main file) | Planilla base en el repo |
|---|---|---|
| A · Radar de acompañamiento (tutor) | `desafio2/app_a_panel_tutor.py` | `desafio2/planillas/Plantilla_config_D2_Variante_A/` |
| B · Acompaña (check-in del estudiante) | `desafio2/app_b_checkin.py` | `desafio2/planillas/Plantilla_config_D2_Variante_B/` |

Cada planilla base está guardada como una carpeta con un CSV por pestaña. El dataset sintético de 3.000 estudiantes no se versiona: la app lo regenera idéntico la primera vez (`desafio2/datos/generar_estudiantes.py`, semilla fija 2026). Todos los datos son ficticios.

## IA con varios proveedores
La app prueba los proveedores en el orden de `[ia] orden` y, dentro de cada uno, los modelos de su lista `modelos`. Si un modelo falla o se satura, pasa al siguiente sin que el equipo lo note; los modelos saturados se saltan 45 s y los que tienen clave o nombre inválido, 10 min. Si todos fallan, muestra una respuesta de demostración.

| Orden por defecto | Modelos |
|---|---|
| Groq | `openai/gpt-oss-120b` → `openai/gpt-oss-20b` |
| Mistral | `mistral-small-latest` → `ministral-8b-latest` |

Para sumar otra clave no hay que tocar código: agréguenla al final de `orden` y creen su bloque `[ia.<nombre>]` con `api_key` y `modelos`. Gemini, OpenRouter, Cerebras, Together, DeepSeek y OpenAI ya traen su dirección; cualquier otro proveedor compatible con la API de OpenAI necesita además `url`. La barra lateral muestra la cadena en uso y bajo cada respuesta se indica qué modelo respondió.

## Despliegue
1. En share.streamlit.io, crear 2 apps desde este repositorio (rama `main`), una por *Main file*.
2. En cada app, **Settings → Secrets**: pegar `.streamlit/secrets.example.toml` con la clave de la IA (Groq, modelo `openai/gpt-oss-120b`, con `openai/gpt-oss-20b` de respaldo si el principal se satura) y un bloque `[equipos.EXX]` (nombre y clave) por equipo. Nunca subir `secrets.toml` al repositorio.
3. Abrir las apps antes de cada jornada: se duermen tras 12 horas sin uso.

Guías para mentores y participantes, rutas de mejora y riesgos éticos: se entregan por separado a la organización.
