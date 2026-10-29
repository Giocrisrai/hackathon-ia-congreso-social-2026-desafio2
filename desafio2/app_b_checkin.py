"""Desafío 2 · Variante B · Acompaña (check-in conversacional del estudiante).
Los equipos la personalizan en su copia de la planilla (pestañas `config` y `servicios_extra`)."""
import json, re, sys
from pathlib import Path
AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "comun")); sys.path.insert(0, str(AQUI))
import pandas as pd, streamlit as st
import nucleo_st as N
import servicios as S

N.iniciar("D2-B", "Acompaña · Check-in", "💬")
N.aviso_ia()
N.acceso()
cfg, extra = N.configuracion(str(AQUI / "planillas" / "Plantilla_config_D2_Variante_B.xlsx"), "servicios_extra", S.validar_servicio)
catalogo = S.catalogo(AQUI, extra)
SERV = dict(zip(catalogo.id_servicio, catalogo.nombre))
personas = pd.read_csv(AQUI / "datos" / "personas_checkin.csv", dtype=str)
try: MAX_TURNOS = max(3, min(15, int(cfg.get("max_turnos", "8"))))
except ValueError: MAX_TURNOS = 8
CATEGORIAS = sorted(S.CATEGORIAS) + ["ninguna"]

st.title(cfg["titulo_app"])
st.markdown(cfg["texto_bienvenida"])

# 🔒 Reglas fijas (los equipos solo agregan personalización desde la planilla)
REGLAS = """Eres "Acompaña", un asistente de check-in para estudiantes de primer año de educación superior en Chile.
Tu objetivo: entender cómo le va a la persona y, si lo necesita, orientarla hacia un servicio del catálogo.
REGLAS FIJAS:
1. NO eres psicólogo: no diagnosticas, no nombras trastornos, no evalúas ni predices nada.
2. Una sola pregunta por mensaje. Valida lo que la persona siente sin exagerar.
3. Solo mencionas servicios del catálogo, por su nombre. No prometes beneficios ni resultados.
4. No pides datos personales (RUT, dirección, diagnósticos). No haces tareas ni evaluaciones del estudiante.
5. Si la persona no quiere seguir, lo respetas y te despides. Una persona del equipo de apoyo decide cualquier contacto.
Catálogo:
{catalogo}"""
CLASIFICAR = """Lee la conversación de check-in y responde SOLO con un JSON con estas claves:
"necesidades": lista con una o más de: {categorias};
"urgencia": "baja", "media" o "alta";
"resumen": 2 frases neutrales, sin juicios ni diagnósticos;
"servicio_sugerido": código del catálogo (ej. "S04") o "ninguno";
"mensaje_al_estudiante": 2 frases cálidas según el tono indicado.
Conversación:
{conv}"""
DIAGNOSTICO = re.compile(r"\b(tienes|sufres|padeces|parece que tienes)\s+(depresi[oó]n|ansiedad|un trastorno|tdah|estr[eé]s postraum)|\bdiagn[oó]stic", re.I)

DEMO = {"chat": {
    "P1_1": "Gracias por contarme, suena a una semana pesada. Compatibilizar turnos, estudio y crianza no es fácil. ¿Qué es lo que más te está costando ahora?",
    "P1_2": "Entiendo. Existe la **Flexibilidad académica para estudiantes que trabajan** y el **Apoyo a estudiantes con responsabilidades de cuidado**. ¿Te gustaría que una persona del equipo te cuente cómo pedirlos?",
    "P1_3": "Perfecto. Al terminar el check-in podrás pedir que alguien del equipo de apoyo te contacte. ¿Algo más que quieras contarme?",
    "P2_1": "Gracias por contarlo. Que la primera prueba salga mal es muy común en programación. ¿Qué parte se te hizo más difícil?",
    "P2_2": "Tiene sentido. Hay **Tutoría entre pares**: estudiantes de cursos superiores que explican sin presión. ¿Te animarías a probar una sesión?",
    "P2_3": "¡Buenísimo! Al terminar el check-in puedes pedir que te ayuden a inscribirte. ¿Algo más?",
    "_por_defecto": "Gracias por contármelo. ¿Podrías contarme un poco más sobre cómo te ha ido estas semanas?"}, "clasificar": {}}
PAL = {"laboral": ["trabaj", "turno", "pega"], "cuidado": ["hij", "niñ", "cuid"], "economico": ["plata", "cuota", "arancel", "gratuidad", "beca", "locomoción"],
       "academico": ["prueba", "nota", "entiendo", "matem", "program", "base"], "vocacional": ["no sé si", "no me gusta", "familia quería"],
       "bienestar": ["estrés", "estres", "ansie", "triste", "desmotiv", "cansad"], "traslado": ["lejos", "traslado", "viaje"], "organizacion": ["no alcanzo", "atrasad"]}
SC = {"laboral": "S04", "cuidado": "S05", "economico": "S03", "academico": "S01", "vocacional": "S07", "bienestar": "S06", "traslado": "S09", "organizacion": "S08"}
def clasif_local(t):
    t = t.lower(); nec = [c for c, ps in PAL.items() if any(p in t for p in ps)] or ["ninguna"]; s = SC.get(nec[0], "ninguno")
    return {"necesidades": nec, "urgencia": "media" if len(nec) > 1 else "baja", "resumen": f"Clasificación por palabras clave: {', '.join(nec)}.",
            "servicio_sugerido": s, "mensaje_al_estudiante": "Gracias por tu tiempo." + (f" Podría servirte: {SERV.get(s, '')}." if s in SERV else "")}
ia = N.IA(DEMO)

bandeja = N.estado_equipo("bandeja").setdefault("casos", [])
ss = st.session_state
ss.setdefault("hist", []); ss.setdefault("turno", 0); ss.setdefault("clasif", None); ss.setdefault("ultimo_info", {})
conv_txt = lambda h: "\n".join(f"{'Estudiante' if m['role'] == 'user' else 'Asistente'}: {m['content']}" for m in h)

def nuevo_caso(pid, c, origen):
    cid = f"C{len(bandeja) + 1:03d}"
    bandeja.append({"caso": cid, "persona": pid, "origen": origen, "urgencia": c.get("urgencia", "-"), "necesidades": ", ".join(c.get("necesidades", [])),
                    "servicio_sugerido": c.get("servicio_sugerido", "-"), "resumen_ia": c.get("resumen", ""), "conversacion": conv_txt(ss.hist), "decision": "Pendiente"})
    N.registrar({"tipo": "caso_creado", "caso": cid, "origen": origen, "urgencia": c.get("urgencia")}); return cid

t1, t2 = st.tabs(["1 · Check-in (vista estudiante)", "2 · Bandeja del equipo de apoyo (vista humana)"])
with t1:
    opciones = ["(escribir libremente)"] + [f"{r.id_persona} · {r.nombre_ficticio}, {r.edad} años, {r.carrera} ({r.jornada})" for r in personas.itertuples()]
    sel = st.selectbox("Simular como (solo para pruebas del equipo)", opciones)
    pid = sel.split(" · ")[0] if sel.startswith("P") else "libre"
    if pid != "libre": st.caption("Contexto para actuar (no se envía a la IA): " + personas[personas.id_persona == pid].iloc[0]["contexto_para_simular"])
    if not ss.hist:
        ok = st.checkbox(cfg["texto_consentimiento"])
        if st.button(cfg["texto_boton"], type="primary"):
            if not ok: st.warning("Para comenzar hay que aceptar el aviso de consentimiento.")
            else:
                N.registrar({"tipo": "consentimiento", "persona": pid})
                ss.hist = [{"role": "assistant", "content": cfg["mensaje_inicial"]}]; st.rerun()
    for m in ss.hist: st.chat_message(m["role"]).markdown(m["content"])
    if ss.ultimo_info: N.aviso_si_demo(ss.ultimo_info)
    if ss.hist and ss.clasif is None:
        msg = st.chat_input("Escribe aquí…")
        if msg:
            ss.hist.append({"role": "user", "content": msg}); ss.turno += 1; ss.ultimo_info = {}
            if N.crisis(msg):  # 🔒 protocolo de crisis
                ss.hist.append({"role": "assistant", "content": N.MENSAJE_CRISIS})
                N.registrar({"tipo": "protocolo_crisis", "entrada": msg, "salida": N.MENSAJE_CRISIS})
                nuevo_caso(pid, {"urgencia": "CRISIS", "necesidades": ["bienestar"], "resumen": "Señal de crisis detectada automáticamente: contacto humano inmediato."}, "protocolo de crisis")
            elif ss.turno > MAX_TURNOS:
                ss.hist.append({"role": "assistant", "content": "Llegamos al final del check-in. Presiona **Terminar check-in**."})
            else:
                sistema = REGLAS.format(catalogo=S.texto(catalogo)) + "\n\n" + N.personalizacion(cfg)
                texto, info = ia.llamar([{"role": "system", "content": sistema}] + ss.hist, "chat", f"{pid}_{ss.turno}", temperatura=0.5, max_tokens=350)
                if DIAGNOSTICO.search(texto):  # 🔒 validación: la IA no diagnostica
                    N.registrar({"tipo": "validacion", "tarea": "chat", "salida": texto, "nota": "lenguaje diagnóstico bloqueado"})
                    texto = "Gracias por contarlo. No puedo darte una opinión de salud, pero sí puedo contarte que existe **Apoyo psicológico y bienestar**. ¿Quieres que te diga cómo acceder?"
                ss.hist.append({"role": "assistant", "content": texto}); ss.ultimo_info = info
            st.rerun()
        if len(ss.hist) > 1 and st.button("Terminar check-in"):
            solo = " ".join(m["content"] for m in ss.hist if m["role"] == "user")
            DEMO["clasificar"]["actual"] = json.dumps(clasif_local(solo), ensure_ascii=False)
            texto, info = ia.llamar([{"role": "system", "content": "Respondes solo JSON válido. " + N.personalizacion(cfg)},
                                     {"role": "user", "content": CLASIFICAR.format(categorias=", ".join(CATEGORIAS), conv=conv_txt(ss.hist))}],
                                    "clasificar", "actual", json_mode=True, temperatura=0)
            c = N.extraer_json(texto) or clasif_local(solo)
            c["necesidades"] = [n for n in c.get("necesidades", []) if n in CATEGORIAS] or ["ninguna"]
            if c.get("servicio_sugerido") not in SERV: c["servicio_sugerido"] = "ninguno"
            ss.clasif = c; ss.ultimo_info = info; st.rerun()
    if ss.clasif:
        c = ss.clasif
        st.markdown("### Resumen del check-in\n" + str(c.get("mensaje_al_estudiante", "")))
        if c["servicio_sugerido"] in SERV: st.markdown(f"**Apoyo que podría servirte:** {SERV[c['servicio_sugerido']]}")
        q = st.radio("¿Quieres que **una persona** del equipo de apoyo te contacte? Es voluntario.", ["Sí, quiero que me contacten", "No, gracias"], index=None)
        util = st.select_slider("¿Te sirvió esta conversación?", ["Nada", "Poco", "Algo", "Mucho"], value="Algo")
        if st.button("Enviar respuesta") and q:
            N.registrar({"tipo": "decision_estudiante", "decision": q, "utilidad": util})
            if q.startswith("Sí"): st.success(f"Listo. Se creó el caso {nuevo_caso(pid, c, 'check-in')}. Una persona lo revisará.")
            else: st.info("Gracias por responder. Si cambias de opinión, puedes escribir al equipo de apoyo cuando quieras.")
        if st.button("Nuevo check-in"):
            ss.hist, ss.turno, ss.clasif, ss.ultimo_info = [], 0, None, {}; st.rerun()
with t2:
    st.caption("Aquí llegan los casos. **La IA no contacta a nadie:** una persona revisa y decide. La bandeja la comparten todos los integrantes del equipo.")
    if not bandeja: st.info("Aún no hay casos.")
    else:
        st.dataframe(pd.DataFrame(bandeja)[["caso", "persona", "origen", "urgencia", "necesidades", "servicio_sugerido", "decision"]], hide_index=True, width="stretch")
        cid = st.selectbox("Caso", [b["caso"] for b in bandeja])
        b = next(x for x in bandeja if x["caso"] == cid)
        st.markdown(f"**Urgencia:** {b['urgencia']} · **Servicio sugerido:** {SERV.get(b['servicio_sugerido'], 'ninguno')}  \n**Resumen de la IA (verifícalo):** {b['resumen_ia']}")
        with st.expander("Conversación completa"): st.text(b["conversacion"])
        dec = st.radio("👤 Decisión humana (obligatoria)", ["Contactar hoy", "Agendar esta semana", "Derivar a otro servicio", "Cerrar sin acción"], index=None, key=f"d_{cid}")
        nota = st.text_input("Nota (opcional)", key=f"n_{cid}")
        if st.button("Registrar decisión"):
            if not dec: st.warning("Elige una decisión: la IA no decide por ti.")
            else: b["decision"] = dec; N.registrar({"tipo": "decision_humana", "caso": cid, "decision": dec, "nota": nota}); st.success(f"{cid}: **{dec}**"); st.rerun()
N.pie(ia)
