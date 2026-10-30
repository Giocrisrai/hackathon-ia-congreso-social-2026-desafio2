# Ficha de línea base · Variante A · Radar de acompañamiento

**Versión:** 4.0 (mismo formato que el Desafío 3) · 30 de octubre de 2026 · **Demostración grabada:** 76 s, en modo demostración (la tiene el coordinador)

Esta ficha describe el estado inicial de la plantilla. El jurado evalúa lo que cada equipo **agrega** sobre esta base.

## Qué hace (al entregarla)
| Componente | Estado inicial |
|---|---|
| Entorno | Una app Streamlit pública por variante (Streamlit Community Cloud). Cada equipo ingresa con código y clave y personaliza la IA en su copia de una planilla de Google (pestañas `config` y `servicios_extra`). Sin instalación ni programación |
| Datos | 3.000 estudiantes sintéticos: 2.100 como "cohorte pasada" para entrenar y 900 como "cohorte actual" para priorizar. Catálogo de 9 servicios ficticios, ampliable por el equipo en `servicios_extra` |
| Priorización | Regresión logística con 21 variables. Excluye siempre `sexo`, `sede` y `tipo_establecimiento_origen`; el equipo puede excluir otras en `variables_excluidas`. En la cohorte actual: AUC 0,86; con cupo de 15% (135 estudiantes), el 83% de la cola efectivamente desertó y la cola alcanza al 43% de quienes desertan |
| Explicación | 3 factores por estudiante, en lenguaje claro (coeficiente × valor) |
| IA generativa | Cadena de proveedores configurable por la organización (por defecto Groq gpt-oss-120b → gpt-oss-20b → Mistral small → ministral-8b). La clave queda oculta en la configuración de la app. Redacta una ficha en 3 secciones a partir de los datos, el check-in y el catálogo. Reglas fijas en el prompt; el equipo solo agrega usuario, tono, largo, ejemplos e instrucciones extra |
| Validación | Marca la propuesta si cita servicios que no existen, si no cita ninguno o si el borrador menciona riesgo, deserción, porcentajes o predicciones |
| Decisión humana | 4 opciones obligatorias más una nota, y la pregunta "¿La propuesta te ahorró trabajo?" como indicador. La propuesta es editable antes de registrar |
| Salvaguardas | Aviso de IA, código de equipo, registro de entradas y salidas (descargable y, si se configura, copiado a una planilla central), límite de 120 consultas por equipo |
| Contingencia | Modo demostración automático sin claves o sin red. Respuestas precalculadas para los 135 estudiantes de la cola |

## Qué NO hace (trabajo abierto para los equipos)
- No define un usuario real concreto ni su flujo semanal: la configuración es genérica.
- No audita sesgos. **Dato de la línea base:** con la configuración inicial, la cola incluye al 25,6% de los vespertinos y al 10,7% de los diurnos, y alcanza al 48% de los hombres que desertan frente al 32% de las mujeres.
- La validación revisa códigos y palabras, pero no el tono del borrador ni si la ficha es fiel a los datos.
- No tiene vista para el estudiante, opción de no ser perfilado ni flujo de consentimiento.
- No define indicadores de impacto ni un modelo de operación.
- No usa datos reales ni se integra con sistemas institucionales.

## Limitaciones conocidas
- Los datos son sintéticos: las relaciones entre variables fueron diseñadas, no observadas. **No sirven para sacar conclusiones sobre estudiantes reales.**
- El puntaje se entrena con clases balanceadas: sirve para **ordenar**, no es una probabilidad.
- El modo demostración no usa el texto del check-in. Solo la IA real personaliza con él.
- Streamlit Cloud borra los archivos locales cuando la app se reinicia o se duerme (tras 12 horas sin uso). El registro debe descargarse o configurarse la copia en planilla central. Hay que abrir la app antes de cada sesión.
- Los proveedores tienen límites por minuto. Con muchos equipos sobre la misma clave pueden aparecer demoras; el núcleo reintenta y cambia de proveedor.
- Si se usa el plan gratuito de Mistral, según documentación de terceros puede usar los datos para mejorar sus modelos: otra razón para usar solo datos sintéticos.
- Las decisiones registradas en la cola se guardan en la memoria de la app: se pierden si la app se reinicia.
