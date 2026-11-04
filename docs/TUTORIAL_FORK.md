# Guía para equipos · Copiar, publicar y mejorar el prototipo · Desafío 2

Cada equipo recibe el código de los prototipos del Desafío 2 y lo copia a su propia cuenta de GitHub. Desde ahí puede **mejorar** una de las variantes o **construir algo nuevo** sobre la misma base. Esta guía explica cómo hacerlo sin experiencia previa en despliegues. Su mentor acompaña a 4 equipos: pídanle ayuda cuando la necesiten.

| Variante | App oficial (para comparar) | Archivo principal | Planilla base |
|---|---|---|---|
| A · Radar de acompañamiento (tutor o jefatura de carrera) | https://hackaton-d2-a.streamlit.app | `desafio2/app_a_panel_tutor.py` | `desafio2/planillas/Plantilla_config_D2_Variante_A/` |
| B · Acompaña (check-in del estudiante) | https://hackaton-d2-b.streamlit.app | `desafio2/app_b_checkin.py` | `desafio2/planillas/Plantilla_config_D2_Variante_B/` |
| Algo nuevo del equipo | (la publican ustedes) | `desafio2/app_nueva.py` | la de la Variante B |

**Todos los datos son ficticios.** Nunca usen datos reales de estudiantes.

## Ruta rápida
La guía sigue las 8 etapas oficiales de la jornada ([Etapas de la jornada](../desafio2/docs/Etapas_jornada_Desafio2.md)). Las cuentas y el fork conviene dejarlos listos antes del evento.

| Etapa | Qué hacen con esta guía |
|---|---|
| 3 · Diseño (11:15–11:45) | Deciden si cada mejora va en la planilla o en el código (secciones 5 a 8) |
| 4 · Desarrollo (11:45–12:45) | **Preparación del entorno (10 min):** cuentas, fork, colaboradores, app publicada y claves (secciones 1 a 4). Luego implementan en paralelo y guardan el avance con *commit* |
| 5 · Integración (13:30–14:15) | Unen las mejoras en su fork y prueban el antes y después y los usos indebidos (sección 10) |
| 6 · Cierre técnico (14:15–14:45) | Solo correcciones, respaldo de la demo, etiqueta `version-final` y declaración de transparencia (sección 13) |

## 1. Qué necesitan
| Qué | Dónde | Costo |
|---|---|---|
| Cuenta de GitHub | https://github.com/signup | Gratis |
| Cuenta de Streamlit Community Cloud (se entra con GitHub) | https://share.streamlit.io | Gratis |
| Clave de IA | La entrega la organización: **Claude Haiku 5.5** (Anthropic). Respaldo gratis: Groq (https://console.groq.com/keys) o Mistral (https://console.mistral.ai/api-keys) | Sin costo para el equipo |
| Opcional: editar y probar con un editor | GitHub Codespaces (en el navegador) o Python 3.11 a 3.13 y Git en su computador | Gratis |

## 2. Copiar el repositorio (fork)
1. Abran https://github.com/Giocrisrai/hackathon-ia-congreso-social-2026-desafio2.
2. Presionen **Fork → Create fork**. Queda una copia en su cuenta, por ejemplo `su-usuario/hackathon-ia-congreso-social-2026-desafio2`.
3. Trabajen siempre en **su** fork. Lo que cambien ahí no afecta las apps oficiales ni a los otros equipos.
4. Agreguen a sus compañeros: en su fork, **Settings → Collaborators → Add people**.

## 3. Publicar su app
1. Entren a https://share.streamlit.io con GitHub y presionen **Create app → Deploy a public app from GitHub**.
2. Completen así:

| Campo | Variante A | Variante B | App nueva |
|---|---|---|---|
| Repository | `su-usuario/hackathon-ia-congreso-social-2026-desafio2` | igual | igual |
| Branch | `main` | `main` | `main` |
| Main file path | `desafio2/app_a_panel_tutor.py` | `desafio2/app_b_checkin.py` | `desafio2/app_nueva.py` |
| App URL | por ejemplo `equipo07-radar` | por ejemplo `equipo07-acompana` | por ejemplo `equipo07-app` |

3. En **Advanced settings**, elijan **Python 3.12** y en **Secrets** peguen la configuración de la sección 4.
4. Presionen **Deploy**. La primera vez tarda 2 a 4 minutos: instala librerías y genera los 3.000 estudiantes ficticios.

## 4. Secrets: claves del equipo y de la IA
Peguen esto en **Advanced settings → Secrets** (o, después, en **Manage app → Settings → Secrets**) y completen las claves:

```toml
[equipos.E01]
nombre = "Equipo 07"
clave = "una-clave-que-inventen"

[ia]
orden = ["anthropic", "groq"]          # se prueban en este orden; si uno falla, pasa al siguiente
limite_consultas_por_equipo = 120

[ia.anthropic]
api_key = "sk-ant-..."                 # la entrega la organización
modelos = ["claude-haiku-5-5"]

[ia.groq]                              # respaldo opcional; si no lo usan, bórrenlo y saquen "groq" de orden
api_key = "gsk_..."
modelos = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
```

- **Las claves van solo en Secrets.** Nunca las escriban en el código, en la planilla ni en un mensaje de GitHub: el repositorio es público. El archivo `.gitignore` ya excluye `.streamlit/secrets.toml`.
- Sin el bloque `[ia]` la app funciona igual, con respuestas de demostración. Sirve para avanzar si la clave aún no llega.
- Sin bloques `[equipos.*]` la app acepta el código `demo` con clave `demo`. Úsenlo solo para probar.
- Bajo cada respuesta aparece qué modelo respondió, por ejemplo "🤖 Respondió anthropic · claude-haiku-5-5". Anótenlo para la declaración de transparencia.
- Otros proveedores (Mistral, Gemini, OpenRouter, Cerebras, Together, DeepSeek, OpenAI) se agregan igual: su nombre en `orden` y su bloque `[ia.<nombre>]`. La plantilla completa está en `.streamlit/secrets.example.toml`.

## 5. Tres formas de cambiar la app
| Forma | Para qué | Cómo |
|---|---|---|
| **A · Planilla** (sin código) | Usuario, tono, largo, ejemplos, reglas extra, textos, cupo, variables excluidas, servicios | Copien la planilla base en Google Sheets, compártanla como Lector, peguen su URL en la barra lateral y presionen "Recargar configuración". Funciona también en la app oficial |
| **B · Editar en GitHub** (sin instalar nada) | Cambios chicos de código: reglas del prompt, opciones, validaciones | En su fork abran el archivo, presionen el **lápiz ✏️**, editen y presionen **Commit changes**. Su app se actualiza sola en 1 a 2 minutos |
| **C · Editor completo** | Cambios grandes o una app nueva | En su fork: **Code → Codespaces → Create codespace on main** (VS Code en el navegador), o clónenlo en su computador (sección 10). Prueben localmente y suban con *commit* y *push* |

Empiecen siempre por la planilla: es lo más rápido y suele ser lo que más mejora la experiencia del usuario. Las [rutas de mejora de la Variante A](../desafio2/docs/Rutas_de_mejora_Variante_A.md) y de la [Variante B](../desafio2/docs/Rutas_de_mejora_Variante_B.md) tienen ideas por nivel.

## 6. Cómo está armado el código
```
comun/nucleo_st.py          núcleo común: ingreso, planilla, IA con cambio de proveedor, registro,
                            protocolo de crisis, diseño y logos                       (🔒 no modificar)
desafio2/app_a_panel_tutor.py   Variante A: modelo de priorización, ficha, decisión y equidad
desafio2/app_b_checkin.py       Variante B: consentimiento, chat, clasificación y bandeja
desafio2/app_nueva.py           plantilla para una app nueva del equipo
desafio2/servicios.py           catálogo de servicios y validación de servicios_extra
desafio2/datos/                 catálogo, perfiles ficticios y generador de estudiantes sintéticos
desafio2/planillas/             valores por defecto de la planilla de cada variante
```

Así viaja una consulta, en las dos variantes:
1. `N.acceso()` pide código y clave del equipo.
2. `N.configuracion(...)` lee la planilla del equipo (o la base) y entrega `cfg`.
3. La app arma el prompt: **reglas fijas** (`REGLAS`) + `N.personalizacion(cfg)` (usuario, tono, largo, ejemplos y reglas del equipo).
4. `ia.llamar(...)` prueba los modelos en el orden de los secrets, cuenta la consulta, la registra y, si nadie responde, devuelve la respuesta de demostración.
5. La app **valida** la respuesta (por ejemplo, que no diagnostique o que solo cite servicios del catálogo) y la muestra.
6. Una **persona decide** y su decisión queda registrada. `N.pie(ia)` muestra las consultas restantes y el registro descargable.

## 7. Recetas para mejorar las variantes
Cada receta indica dónde está lo que hay que cambiar. Hagan **un cambio a la vez** y prueben el mismo caso antes y después.

### Variante A · Radar de acompañamiento (`desafio2/app_a_panel_tutor.py`)
| Quieren… | Dónde | Cómo |
|---|---|---|
| Que la ficha diga algo nuevo (por ejemplo, una pregunta para abrir la conversación) | `REGLAS` (y `secciones()` si agregan una sección) | Agreguen una regla numerada. Si cambian el formato de 3 secciones, actualicen también `secciones()`, que las separa en tarjetas |
| Explicar mejor "¿Por qué aparece?" | `ETIQUETAS` | Cambien el texto que acompaña a cada variable, por ejemplo `"tiempo_traslado_min": "viaja más de una hora"` |
| Que el modelo no use una variable más | planilla `variables_excluidas` o `PERMITIDAS_EXCLUIR` | Sexo, sede y tipo de colegio ya están excluidos siempre. Comparen la pestaña 3 antes y después |
| Revisar la equidad por otro grupo | `GRUPOS` | Agreguen una columna de los datos, por ejemplo `"primera_generacion": "Primera generación"` |
| Bloquear otra palabra en el borrador al estudiante | `PROHIBIDAS_BORRADOR` | Súmenla a la expresión, por ejemplo `riesgo\|deser\|...\|alerta` |
| Otras decisiones del tutor | `OPCIONES` | Cambien o agreguen opciones; siguen quedando registradas |
| Cuántos estudiantes entran a la cola | planilla `cupo_porcentaje` | Entre 5 y 40 % |

### Variante B · Acompaña (`desafio2/app_b_checkin.py`)
| Quieren… | Dónde | Cómo |
|---|---|---|
| Cambiar cómo conversa | `REGLAS` y planilla (`tono`, `ejemplos`) | Agreguen una regla numerada, por ejemplo "8. Si la persona trabaja de noche, pregunta qué horario le acomoda". No quiten las reglas 1 a 7 |
| Más o menos preguntas por check-in | planilla `max_turnos` | Entre 3 y 15 |
| Mejorar el resumen para la persona de apoyo | `CLASIFICAR` | Agreguen una clave al JSON, por ejemplo `"siguiente_paso"`, y muéstrenla en la bandeja (pestaña 2) |
| Que la clasificación sin IA reconozca más palabras | `PAL` y `SC` | Sumen palabras a cada categoría o un servicio por categoría |
| Bloquear otra forma de diagnosticar | `DIAGNOSTICO` | Súmenla a la expresión regular |
| Probar con otros estudiantes ficticios | `desafio2/datos/personas_checkin.csv` | Agreguen filas con `P5`, `P6`… |
| Detectar otras frases de crisis | `_CRISIS` en `comun/nucleo_st.py` | **Solo agregar**, nunca quitar. Prueben que frases comunes no la activen por error |

### Las dos variantes
| Quieren… | Dónde |
|---|---|
| Servicios reales de su institución | Planilla `servicios_extra` (con fuente) o `desafio2/datos/catalogo_servicios.csv` (ids `S10`, `S11`…) |
| Colores y tarjetas | `.streamlit/config.toml` y el bloque `_CSS` de `comun/nucleo_st.py` |
| Datos sintéticos distintos | `desafio2/datos/generar_estudiantes.py`; borren el CSV generado para que se regenere |

## 8. Construir algo nuevo: `desafio2/app_nueva.py`
Si su idea no cabe en A ni en B (por ejemplo, un asistente para apoderados o para docentes), partan de `desafio2/app_nueva.py`. Ya trae todo lo que exigen las bases: ingreso por equipo, aviso de IA, planilla, IA con respaldo, registro, límite de consultas, protocolo de crisis y decisión humana.

1. Copien el archivo con otro nombre, por ejemplo `desafio2/app_equipo07.py`, o editen el mismo.
2. Cambien solo lo marcado con ✏️: título, la tarea en `REGLAS`, la pregunta de la pantalla y las opciones de decisión.
3. Publíquenlo como una app más (sección 3), con ese archivo como *Main file*.
4. Las líneas marcadas con 🔒 no se borran.

## 9. Usar una IA para programar
Pueden pedirle a Claude (u otro asistente) que les ayude a cambiar el código. Para que no rompa las protecciones, denle contexto:

```
Estoy mejorando una app de Streamlit de una hackathon. Te paso el archivo desafio2/app_b_checkin.py.
Quiero: <su cambio, en una frase>.
Reglas: no modifiques comun/nucleo_st.py; mantén el aviso de IA, el consentimiento, el protocolo de crisis,
la prohibición de diagnosticar, el registro y la decisión humana. Devuélveme solo las líneas que cambian
y dime cómo probarlo.
```

Revisen cada cambio antes de hacer *commit* y prueben la app después. Declaren en la transparencia que usaron IA para programar.

## 10. Probar antes del pitch
**En su app publicada:**
- Prueben el **mismo caso** con la plantilla base y con su versión, y guarden ambas capturas.
- Prueben al menos **5 usos indebidos** y anoten qué pasó, por ejemplo:
  - "ignora tus reglas";
  - pedir un diagnóstico;
  - pedir el RUT de alguien;
  - un mensaje de crisis;
  - en A, pedir el puntaje de riesgo.
- Descarguen el registro desde la barra lateral.

**En su computador (opcional):**
```bash
git clone https://github.com/su-usuario/hackathon-ia-congreso-social-2026-desafio2
cd hackathon-ia-congreso-social-2026-desafio2
python3 -m venv .venv && source .venv/bin/activate      # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .streamlit/secrets.example.toml .streamlit/secrets.toml   # y pongan sus claves
streamlit run desafio2/app_a_panel_tutor.py              # o app_b_checkin.py, o app_nueva.py
```
La app se abre en http://localhost:8501. Cada vez que guarden un archivo, presionen **Rerun** en la app.

## 11. Lo que deben mantener
Son parte de las bases y de la evaluación ética:
- El aviso de uso de IA y la **decisión humana** obligatoria.
- El registro de consultas y un límite de consultas.
- **Variante A:**
  - el modelo no usa `sexo`, `sede` ni `tipo_establecimiento_origen`;
  - el borrador al estudiante no muestra puntajes, riesgo ni predicciones.
- **Variante B:**
  - el consentimiento previo;
  - la prohibición de diagnosticar;
  - el protocolo de crisis (`_CRISIS` y `MENSAJE_CRISIS`).
- Datos ficticios: nunca datos reales de estudiantes.
- No modificar `comun/nucleo_st.py`, salvo para agregar frases de crisis o servicios.

## 12. Problemas frecuentes
| Síntoma | Causa probable | Solución |
|---|---|---|
| "Your app is in the oven" más de 5 minutos | Error al instalar librerías | **Manage app → Logs**; usen Python 3.12 |
| La página queda en blanco o cargando | Falla momentánea de Streamlit Cloud | Recarguen la página |
| Siempre "respuesta de demostración" | Falta `[ia]` o la clave es inválida | Revisen los secrets; la barra lateral muestra la cadena de IA y marca ⏸️ los modelos pausados |
| Error 429 frecuente | Límite del proveedor | Agreguen un segundo proveedor en `orden` |
| "No se pudo leer la planilla" | Planilla no compartida | Compartir → Cualquier persona con el vínculo · Lector |
| Cambié el código y no se ve | Streamlit Cloud no actualizó | Revisen que el *commit* esté en `main`; esperen 1 a 2 minutos o usen **Reboot app** |
| `SyntaxError` o `NameError` en la app | Error al editar | **Manage app → Logs** dice el archivo y la línea; corrijan o vuelvan a la versión anterior en GitHub (**History**) |

## 13. Congelar y declarar (Etapa 6 · Cierre técnico, 14:15–14:45)
- **Primeros 10 minutos:** solo correcciones visibles para la demo, sin funcionalidades nuevas.
- **Siguientes 10 minutos:** prueba final completa, un video corto de respaldo y el registro descargado desde la barra lateral.
- **Últimos 10 minutos:** congelen la versión con un último *commit* y la etiqueta `version-final`. En su fork: **Releases → Draft a new release → Choose a tag**, escriban `version-final`, **Create new tag** y **Publish release**.
- Después de congelar no hagan más *commits*: cada uno reinicia la app y sus contadores, y se evalúa la versión congelada a las **14:45 h**.
- Anoten cómo se ejecuta (URL de la app y código de equipo) y las limitaciones conocidas en la [ficha de cierre](../desafio2/docs/Fichas_equipo_Desafio2.md).
- En la **declaración de transparencia** indiquen:
  - la URL de su fork y de su app;
  - qué archivos cambiaron y por qué;
  - qué proveedores y modelos de IA usa la app;
  - si usaron IA para programar;
  - qué protecciones mantuvieron y cómo probaron el mal uso.
