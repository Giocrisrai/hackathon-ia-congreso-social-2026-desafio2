"""Desafío 2 · Plantilla para construir una app NUEVA sobre el núcleo común.

Copien este archivo cuando su idea no quepa en las variantes A o B. Ya trae lo que las bases exigen:
ingreso por equipo, aviso de IA, planilla del equipo, IA con cambio de proveedor, registro, límite de
consultas, protocolo de crisis y decisión humana. Cambien solo lo marcado con ✏️.
Para publicarla en Streamlit Cloud, usen como Main file:  desafio2/app_nueva.py"""
import sys
from pathlib import Path
AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "comun")); sys.path.insert(0, str(AQUI))
import streamlit as st
import nucleo_st as N
import servicios as S

# ✏️ Identificador (aparece en el registro), título e ícono
N.iniciar("D2-NUEVA", "Mi herramienta · Desafío 2", "✨")
N.acceso()  # 🔒 código y clave del equipo

# La planilla de la Variante B sirve de base: usuario, tono, largo, ejemplos, textos y servicios_extra
cfg, extra = N.configuracion(str(AQUI / "planillas" / "Plantilla_config_D2_Variante_B.xlsx"), "servicios_extra", S.validar_servicio)
catalogo = S.catalogo(AQUI, extra)

# ✏️ Reglas fijas de su herramienta. Mantengan las que protegen a las personas (1, 2 y 3).
REGLAS = """Eres un asistente que ayuda a estudiantes de primer año de educación superior técnico-profesional en Chile.
✏️ Tu tarea: (describan aquí qué hace su herramienta y para quién).
REGLAS FIJAS:
1. No diagnosticas, no predices y no decides por la persona: una persona del equipo de apoyo decide cualquier contacto.
2. Solo mencionas servicios del catálogo, por su nombre y con su código entre corchetes, por ejemplo [S04].
3. No pides datos personales (RUT, dirección, diagnósticos) y no inventas pasos de acceso: usa solo "Cómo acceder".
4. Escribe en español de Chile, tuteando con "tú".
Catálogo:
{catalogo}"""

# ✏️ Respuesta cuando la IA no responde (modo demostración)
ia = N.IA({"respuesta": {"_por_defecto": "[Demostración] La IA no respondió. Aquí iría la orientación con un servicio del catálogo, por ejemplo **Tutoría entre pares**."}})

N.encabezado(cfg.get("titulo_app", "Mi herramienta"), cfg.get("texto_bienvenida", ""), ["Desafío 2 · Educación"])
N.aviso_ia()  # 🔒 aviso de uso de IA

pregunta = st.text_area("✏️ ¿En qué te podemos orientar?", key="pregunta", height=120)
if st.button("Enviar", type="primary") and pregunta.strip():
    if N.crisis(pregunta):  # 🔒 protocolo de crisis: responde una persona, no la IA
        st.session_state["resultado"] = (N.MENSAJE_CRISIS, {})
        N.registrar({"tipo": "protocolo_crisis", "entrada": pregunta, "salida": N.MENSAJE_CRISIS})
    elif not N.repetido(f"nueva|{pregunta.strip()}"):  # doble clic: no gasta otra consulta
        sistema = REGLAS.format(catalogo=S.texto(catalogo)) + "\n\n" + N.personalizacion(cfg)
        with st.spinner("Pensando…"):
            texto, info = ia.llamar([{"role": "system", "content": sistema}, {"role": "user", "content": pregunta}], "respuesta")
        st.session_state["resultado"] = (texto, info)

if "resultado" in st.session_state:
    texto, info = st.session_state["resultado"]
    st.markdown(texto)
    N.aviso_si_demo(info)
    # 🔒 Decisión humana, registrada
    d = st.radio("¿Qué harás con esta orientación?", ["Pediré que una persona me contacte", "Lo pensaré", "No me sirve"], index=None)
    if d and st.button("Registrar mi decisión"):
        N.registrar({"tipo": "decision_estudiante", "decision": d})
        st.success("Decisión registrada. ¡Gracias!")

N.pie(ia)  # 🔒 consultas restantes, cadena de IA y registro descargable
