# Tutorial · Tu propia versión de las apps del Desafío 2

Este tutorial es para un equipo que quiere ir más allá de la planilla: copiar el repositorio (fork), desplegar **su propia app** y cambiar el código. Sirve para las dos variantes. Tiempo: 20 a 30 minutos, sin experiencia previa en despliegues.

> **Antes de empezar.** En la competencia se evalúa la mejora sobre la plantilla oficial. Un fork está permitido si lo declaran en la **declaración de transparencia** (qué cambiaron y qué modelos usan) y si mantienen las protecciones de la sección 6. Si tienen dudas, confírmenlo con su mentor.

## 1. Qué necesitan
| Qué | Dónde | Costo |
|---|---|---|
| Cuenta de GitHub | https://github.com/signup | Gratis |
| Cuenta de Streamlit Community Cloud (se entra con GitHub) | https://share.streamlit.io | Gratis |
| Una clave de IA compatible con OpenAI | Groq: https://console.groq.com/keys (plan gratis) · Mistral: https://console.mistral.ai/api-keys | Gratis con límites |
| Opcional, para probar en su computador | Python 3.11 a 3.13 y Git | Gratis |

## 2. Hacer el fork
1. Abran https://github.com/Giocrisrai/hackathon-ia-congreso-social-2026-desafio2.
2. Presionen **Fork → Create fork**. Queda una copia en su cuenta, por ejemplo `su-usuario/hackathon-ia-congreso-social-2026-desafio2`.
3. Todo lo que cambien en su fork no afecta las apps oficiales.

## 3. Desplegar su app (sin instalar nada)
1. Entren a https://share.streamlit.io con GitHub y presionen **Create app → Deploy a public app from GitHub**.
2. Completen:

| Campo | Variante A · Radar | Variante B · Acompaña |
|---|---|---|
| Repository | `su-usuario/hackathon-ia-congreso-social-2026-desafio2` | igual |
| Branch | `main` | `main` |
| Main file path | `desafio2/app_a_panel_tutor.py` | `desafio2/app_b_checkin.py` |
| App URL | por ejemplo `equipo07-radar` | por ejemplo `equipo07-acompana` |

3. En **Advanced settings**, elijan **Python 3.12** y en **Secrets** peguen la configuración de la sección 4.
4. Presionen **Deploy**. La primera vez tarda 2 a 4 minutos: instala librerías y genera los 3.000 estudiantes sintéticos.

## 4. Secrets mínimos
Peguen esto en **Settings → Secrets** de su app, con su clave:

```toml
[equipos.E01]
nombre = "Equipo 07"
clave = "una-clave-que-inventen"

[ia]
orden = ["groq"]
limite_consultas_por_equipo = 120

[ia.groq]
api_key = "gsk_..."
modelos = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
```

- Sin el bloque `[ia]` la app funciona igual, con respuestas de demostración.
- Sin bloques `[equipos.*]` la app acepta el código `demo` con clave `demo`. Úsenlo solo para probar.
- **Nunca suban `secrets.toml` a GitHub.** El archivo `.gitignore` ya lo excluye.

### Usar varios proveedores de IA
La app prueba los proveedores en el orden de `orden` y, dentro de cada uno, los modelos de `modelos`. Si uno falla o se satura, pasa al siguiente. Para sumar otra clave, agreguen su nombre a `orden` y su bloque:

```toml
[ia]
orden = ["groq", "mistral", "gemini"]

[ia.mistral]
api_key = "..."
modelos = ["mistral-small-latest", "ministral-8b-latest"]

[ia.gemini]
api_key = "..."
modelos = ["gemini-2.5-flash"]
```

Ya traen dirección: `groq`, `mistral`, `openai`, `gemini`, `openrouter`, `cerebras`, `together` y `deepseek`. Cualquier otro proveedor compatible con OpenAI necesita además `url = "https://.../v1/chat/completions"`.

## 5. Probar en su computador (opcional)
```bash
git clone https://github.com/su-usuario/hackathon-ia-congreso-social-2026-desafio2
cd hackathon-ia-congreso-social-2026-desafio2
python3 -m venv .venv && source .venv/bin/activate      # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .streamlit/secrets.example.toml .streamlit/secrets.toml   # y pongan su clave
streamlit run desafio2/app_a_panel_tutor.py              # Variante A
streamlit run desafio2/app_b_checkin.py                  # Variante B
```
La app se abre en http://localhost:8501. Cada vez que guarden un archivo, presionen **Rerun** en la app.

## 6. Qué pueden cambiar y qué deben mantener
| Quieren cambiar | Archivo | Qué tocar |
|---|---|---|
| Textos, tono, usuario, ejemplos | (sin código) planilla | Pestaña `config` de su copia |
| Servicios del catálogo base | `desafio2/datos/catalogo_servicios.csv` | Filas nuevas con id `S10`, `S11`… |
| Valores por defecto de la planilla | `desafio2/planillas/Plantilla_config_D2_Variante_A/` o `_B/` | `config.csv` y `servicios_extra.csv` |
| Diseño (colores, tarjetas) | `.streamlit/config.toml` y `comun/nucleo_st.py` | Tema y bloque `_CSS` |
| Proveedores y reintentos de IA | `comun/nucleo_st.py` | `PROVEEDORES`, clase `IA` |
| **A ·** reglas del prompt | `desafio2/app_a_panel_tutor.py` | `REGLAS`, `PETICION` |
| **A ·** modelo de priorización | `desafio2/app_a_panel_tutor.py` | función `preparar()`; etiquetas en `ETIQUETAS` |
| **A ·** validación del borrador | `desafio2/app_a_panel_tutor.py` | `PROHIBIDAS_BORRADOR`, `validar()` |
| **A ·** gráfico de equidad | `desafio2/app_a_panel_tutor.py` | `GRUPOS` y pestaña 3 |
| **B ·** reglas del check-in | `desafio2/app_b_checkin.py` | `REGLAS`, `CLASIFICAR` |
| **B ·** perfiles ficticios | `desafio2/datos/personas_checkin.csv` | Filas nuevas |
| **B ·** bandeja | `desafio2/app_b_checkin.py` | `URG`, pestaña 2 |
| Datos sintéticos | `desafio2/datos/generar_estudiantes.py` | Borren el CSV generado para que se regenere |

**Deben mantener** (son parte de la evaluación ética y de las bases):
- El aviso de uso de IA y la decisión humana obligatoria.
- En A, la exclusión de `sexo`, `sede` y `tipo_establecimiento_origen`, y que el borrador al estudiante no muestre puntajes, riesgo ni predicciones.
- En B, el consentimiento, la prohibición de diagnosticar y el protocolo de crisis (`_CRISIS` y `MENSAJE_CRISIS` en `comun/nucleo_st.py`).
- El registro de consultas y un límite de consultas.
- Datos ficticios: nunca datos reales de estudiantes.

## 7. Problemas frecuentes
| Síntoma | Causa probable | Solución |
|---|---|---|
| La app queda en "Your app is in the oven" más de 5 minutos | Error al instalar librerías | Revisen **Manage app → Logs**; usen Python 3.12 |
| Siempre "respuesta de demostración" | Falta `[ia]` o la clave es inválida | Revisen los secrets; la barra lateral muestra la cadena de IA y marca ⏸️ los modelos pausados |
| `model_not_found` en los registros | El proveedor retiró ese modelo | Cambien `modelos` en los secrets |
| Error 429 frecuente | Límite del plan gratis | Agreguen un segundo proveedor o un segundo modelo |
| "No se pudo leer la planilla" | Planilla no compartida | Compartir → Cualquier persona con el vínculo · Lector |
| Cambié el código y no se ve | Streamlit Cloud no actualizó | Hagan *commit* en `main`; la app se actualiza sola en 1 a 2 minutos o con **Reboot app** |

## 8. Qué declarar en la transparencia
- URL de su fork y de su app.
- Qué archivos cambiaron y por qué.
- Qué proveedores y modelos de IA usan.
- Qué protecciones mantuvieron y cómo probaron el mal uso.
