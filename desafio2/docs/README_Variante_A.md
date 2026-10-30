# README · Radar de acompañamiento

Desafío 2 · Educación · Hackathon IA Congreso Social UC 2026

## ¿Qué es?

Un panel que ayuda a un tutor o jefe de carrera a decidir a quién contactar primero esta semana. Un modelo explicable ordena una cohorte ficticia de 900 estudiantes según señales de las semanas 1 a 6 (asistencia, notas, plataforma, trabajo, cuidado…), muestra solo a quienes caben en el cupo del tutor y dice **por qué aparece cada uno**. La IA prepara la conversación: qué muestran los datos, apoyos del catálogo y un borrador de mensaje. **La IA no decide**: el tutor edita la propuesta y registra su decisión. Su desafío es adaptar la herramienta a un usuario real.

## Cómo empezar (10 minutos)

1. Abran la app: https://hackaton-d2-a.streamlit.app
2. Ingresen con el código y la clave de su equipo, que les entrega su mentor.
3. Hagan una copia de la Sheet plantilla (su mentor les entrega el enlace): Archivo → Hacer una copia.
4. Compartan su copia: botón Compartir → Acceso general → "Cualquier persona con el vínculo" → Lector.
5. Peguen la URL de su copia en la barra lateral de la app y presionen "Recargar configuración".
6. Revisen la cola de la semana, elijan un estudiante y presionen el botón principal para preparar la conversación.

## Qué pueden cambiar

- **Pestaña config:** a quién apoya la IA, su tono, el largo de las respuestas, ejemplos de respuesta ideal, reglas propias, los textos de la pantalla, el cupo semanal y qué variables **no** puede usar el modelo (`variables_excluidas`).
- **Pestaña servicios_extra:** agregar servicios de apoyo de su institución u otros, copiando la fila EJEMPLO. Si el servicio es real, debe tener una fuente oficial.

Después de cada cambio: presionen "Recargar configuración" y prueben de nuevo con el mismo estudiante para comparar.

## Qué no pueden cambiar

El aviso de uso de IA, el registro de consultas, el límite de 120 consultas por equipo, la exclusión permanente de sexo, sede y tipo de establecimiento, las reglas fijas (no etiquetar, no mostrar puntajes ni predicciones al estudiante, citar solo servicios del catálogo) y la validación de las respuestas.

## Si algo falla

- Si aparece "Se muestra una respuesta de demostración", la IA no respondió: esperen un minuto y prueben de nuevo. Si persiste, avisen a su mentor.
- Si un cambio en la Sheet no se ve, revisen que esté compartida y presionen "Recargar configuración".
- Si la barra lateral muestra filas ignoradas, ábranla: dice qué corregir en cada fila.
- Si aparece "La validación detectó problemas", la IA citó un servicio que no existe o el borrador menciona riesgo o predicciones: corrijan el texto antes de usarlo y, si se repite, refuercen sus `instrucciones_extra`.

## Qué deben entregar

Además del pitch: la declaración de transparencia (qué modelos usaron y qué cambiaron respecto de esta plantilla) y el checklist ético completo antes de las 14:45. Usen el registro descargable de la barra lateral como evidencia.
