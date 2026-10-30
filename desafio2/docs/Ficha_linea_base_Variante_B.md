# Ficha de línea base · Variante B · Acompaña

**Versión:** 4.0 (mismo formato que el Desafío 3) · 30 de octubre de 2026 · **Demostración grabada:** 78 s, en modo demostración (la tiene el coordinador)

Esta ficha describe el estado inicial de la plantilla. El jurado evalúa lo que cada equipo **agrega** sobre esta base.

## Qué hace (al entregarla)
| Componente | Estado inicial |
|---|---|
| Entorno | Una app Streamlit pública por variante. Cada equipo ingresa con código y clave y personaliza la IA en su copia de una planilla de Google (pestañas `config` y `servicios_extra`). Sin instalación ni programación |
| Datos | Catálogo de 9 servicios ficticios, ampliable por el equipo en `servicios_extra`, y 6 personas ficticias para simular |
| Consentimiento | Casilla obligatoria antes de iniciar; queda registrada |
| IA conversacional | Cadena de proveedores configurable por la organización (por defecto Groq → Mistral), con claves ocultas. Reglas fijas en el prompt: no diagnosticar, una pregunta a la vez, solo servicios del catálogo, no pedir datos personales. El equipo agrega usuario, tono, largo, ejemplos e instrucciones extra. Máximo de mensajes configurable (8 por defecto) |
| Validación | Si la respuesta usa lenguaje diagnóstico ("tienes ansiedad…"), se reemplaza por una derivación segura y queda registrada |
| IA clasificadora | Al terminar, resume y clasifica en 9 categorías con urgencia baja, media o alta y un servicio sugerido (JSON). El núcleo descarta categorías y códigos que no existen |
| Decisión del estudiante | El estudiante elige si quiere contacto humano (solo entonces se crea un caso) y responde "¿Te sirvió esta conversación?" como indicador |
| Decisión humana | Bandeja del equipo de apoyo, compartida por los integrantes del equipo: 4 opciones obligatorias más una nota |
| Protocolo de crisis | Detección por palabras clave (no editable). La IA no responde: muestra \*4141, Salud Responde y SAMU, y crea un caso urgente |
| Salvaguardas | Aviso de IA, código de equipo, registro de entradas y salidas (descargable y, si se configura, copiado a una planilla central), límite de 120 consultas por equipo |
| Contingencia | Modo demostración automático: respuestas guionadas para P1 y P2 (3 turnos), respuesta genérica para el resto y clasificación por palabras clave |

## Qué NO hace (trabajo abierto para los equipos)
- No adapta el tono a un perfil de estudiante concreto: el prompt es genérico.
- No valida la respuesta conversacional antes de mostrarla: no tiene filtro de consejos médicos, promesas ni temas fuera de lugar.
- No define criterios de urgencia ni quién atiende la bandeja, en qué plazo ni con qué protocolo.
- No conecta con canales reales como WhatsApp o voz, ni con servicios reales de una institución.
- No tiene opción de borrar la conversación ni de retirar el consentimiento después de enviarla.
- No define indicadores de impacto.

## Limitaciones conocidas
- La detección de crisis por palabras clave tiene **falsos negativos** (frases indirectas) y **falsos positivos** (por ejemplo, "abuso" en otro contexto). Es una red mínima, no un sistema clínico.
- La IA puede equivocarse al clasificar; la persona de la bandeja debe leer la conversación completa.
- El modo demostración es guionado: no responde con sentido a mensajes distintos de los ensayados.
- La bandeja vive en la memoria de la app: se pierde si la app se reinicia o se duerme (tras 12 horas sin uso). El registro debe descargarse.
- Los proveedores tienen límites por minuto. Si se usa el plan gratuito de Mistral, según documentación de terceros puede usar los datos para entrenar: solo deben ingresarse conversaciones simuladas.
