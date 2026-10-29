"""Desafío 2 · Variante A · Radar de acompañamiento (panel del tutor).
Los equipos la personalizan en su copia de la planilla (pestañas `config` y `servicios_extra`)."""
import re, sys
from pathlib import Path
AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "comun")); sys.path.insert(0, str(AQUI))
import numpy as np, pandas as pd, streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import nucleo_st as N
import servicios as S

N.iniciar("D2-A", "Radar de acompañamiento", "🧭")
N.aviso_ia()
N.acceso()
cfg, extra = N.configuracion(str(AQUI / "planillas" / "Plantilla_config_D2_Variante_A.xlsx"), "servicios_extra", S.validar_servicio)
catalogo = S.catalogo(AQUI, extra)

st.title(cfg["titulo_app"])
st.markdown(cfg["texto_bienvenida"])

try: CUPO = min(40, max(5, int(float(cfg.get("cupo_porcentaje", "15").replace(",", ".")))))
except ValueError: CUPO = 15
PERMITIDAS_EXCLUIR = {"sexo", "sede", "tipo_establecimiento_origen", "jornada", "edad", "anios_desde_egreso_media", "primera_generacion",
                      "gratuidad", "tiempo_traslado_min", "cuida_dependientes", "egreso_liceo_tp", "nem", "area_carrera", "tipo_carrera"}
EXCLUIDAS = sorted({"sexo", "sede", "tipo_establecimiento_origen"} | {v.strip() for v in cfg.get("variables_excluidas", "").split(";") if v.strip() in PERMITIDAS_EXCLUIR})

ETIQUETAS = {"asistencia_s4_s6_pct": "baja asistencia en semanas 4 a 6", "asistencia_s1_s3_pct": "baja asistencia en semanas 1 a 3",
             "nota_promedio_parcial": "notas parciales bajas", "evaluaciones_rendidas_pct": "evaluaciones no rendidas", "entregas_atrasadas": "entregas atrasadas",
             "logins_lms_semana": "poco uso de la plataforma", "dias_desde_ultimo_login": "varios días sin entrar a la plataforma",
             "horas_trabajo_semana": "muchas horas de trabajo", "trabajo_por_turnos": "trabajo por turnos", "cuida_dependientes": "tiene personas a su cuidado",
             "tiempo_traslado_min": "traslado largo", "arancel_atrasado": "arancel atrasado", "beneficio_en_riesgo": "beneficio en riesgo", "nem": "NEM más bajo",
             "uso_tutoria": "no usa tutorías", "edad": "edad", "anios_desde_egreso_media": "años desde que salió de la media", "primera_generacion": "primera generación",
             "gratuidad": "sin gratuidad", "egreso_liceo_tp": "egresó de liceo TP", "contacto_bienestar": "contacto con bienestar",
             "jornada_Vespertina": "jornada vespertina", "tipo_carrera_Técnica": "carrera técnica"}

@st.cache_resource(show_spinner="Preparando la cohorte…")
def preparar(excluidas: tuple, cupo: int):
    ruta = AQUI / "datos" / "estudiantes_sinteticos_desafio2.csv"
    if not ruta.exists():  # el CSV no se versiona: se regenera igual (semilla fija) la primera vez
        sys.path.insert(0, str(AQUI / "datos")); import generar_estudiantes
        generar_estudiantes.generar().to_csv(ruta, index=False, encoding="utf-8")
    est = pd.read_csv(ruta)
    pasada, actual = train_test_split(est, test_size=0.3, random_state=7, stratify=est.deserta_primer_anio)
    actual = actual.drop(columns=["deserta_primer_anio", "motivo_declarado_salida"]).reset_index(drop=True)
    X = [c for c in est.columns if c not in set(excluidas) | {"id_estudiante", "deserta_primer_anio", "motivo_declarado_salida", "respuesta_checkin_s4"}]
    cat = [c for c in X if est[c].dtype == object or str(est[c].dtype).startswith("str")]
    num = [c for c in X if c not in cat]
    pre = ColumnTransformer([("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num),
                             ("cat", OneHotEncoder(handle_unknown="ignore", drop="first"), cat)])
    m = Pipeline([("pre", pre), ("m", LogisticRegression(max_iter=2000, class_weight="balanced"))]).fit(pasada[X], pasada.deserta_primer_anio)
    p = m.predict_proba(actual[X])[:, 1]
    k = max(1, int(len(actual) * cupo / 100)); orden = np.argsort(-p)[:k]
    Z = m.named_steps["pre"].transform(actual[X].iloc[orden]); Z = Z.toarray() if hasattr(Z, "toarray") else Z
    contrib = Z * m.named_steps["m"].coef_[0]
    nombres = [n.split("__", 1)[1] for n in m.named_steps["pre"].get_feature_names_out()]
    cola = actual.iloc[orden].reset_index(drop=True)
    cola["orden"] = [f"{i + 1} de {k}" for i in range(k)]
    cola["por_que"] = ["; ".join(ETIQUETAS.get(nombres[j], nombres[j].replace("_", " ")) for j in np.argsort(-fila)[:3] if fila[j] > 0) for fila in contrib]
    return cola, len(actual)

cola, n_actual = preparar(tuple(EXCLUIDAS), CUPO)
CAMPOS = ["area_carrera", "tipo_carrera", "jornada", "edad", "primera_generacion", "horas_trabajo_semana", "trabajo_por_turnos", "cuida_dependientes",
          "tiempo_traslado_min", "asistencia_s1_s3_pct", "asistencia_s4_s6_pct", "nota_promedio_parcial", "evaluaciones_rendidas_pct",
          "entregas_atrasadas", "dias_desde_ultimo_login", "uso_tutoria", "gratuidad", "arancel_atrasado", "beneficio_en_riesgo"]
datos_txt = lambda f: "\n".join(f"- {c}: {f[c]}" for c in CAMPOS if pd.notna(f[c]))
checkin = lambda f: f["respuesta_checkin_s4"] if isinstance(f["respuesta_checkin_s4"], str) and f["respuesta_checkin_s4"].strip() else "(no respondió)"

# 🔒 Reglas fijas del prompt (los equipos solo agregan la personalización desde la planilla)
REGLAS = """Eres un asistente que apoya a tutores y jefes de carrera de educación superior en Chile a PREPARAR una
conversación de acompañamiento con un estudiante de primer año. No juzgas, no predices y no decides.
REGLAS FIJAS:
1. Lenguaje respetuoso: nunca uses etiquetas como "alumno problema", "desertor" o "en riesgo".
2. Describe lo que muestran los datos sin inventar causas ni datos que no estén.
3. Sugiere SOLO servicios del catálogo, citando su código entre corchetes, por ejemplo [S04].
4. El borrador para el estudiante NO menciona puntajes, porcentajes, predicciones, riesgo ni deserción, y deja claro que es voluntario.
5. La decisión final es del tutor.
FORMATO: tres secciones con estos títulos: "1. Lo que muestran los datos", "2. Apoyos posibles", "3. Borrador de mensaje"."""
PETICION = """Datos del estudiante (ficticio):
{datos}
Señales que más pesaron en la priorización: {factores}
Check-in de la semana 4 (escrito por el estudiante): "{checkin}"
Catálogo de servicios:
{catalogo}"""

PROHIBIDAS_BORRADOR = re.compile(r"riesgo|deser|probabilid|predic|puntaje|\d+ ?%|algoritmo", re.I)
def validar(texto):
    problemas = []
    codigos = set(re.findall(r"\[([A-Z]\w{1,5})\]", texto))
    malos = sorted(c for c in codigos if c not in set(catalogo.id_servicio))
    if malos: problemas.append(f"cita servicios que no existen en el catálogo: {', '.join(malos)}")
    if not codigos: problemas.append("no cita ningún servicio del catálogo con su código")
    borrador = texto.split("3.", 1)[1] if "3." in texto else texto
    if PROHIBIDAS_BORRADOR.search(borrador): problemas.append("el borrador menciona riesgo, deserción, porcentajes o predicciones")
    return problemas

def demo(f):
    sug = {"trabajo": "S04", "turnos": "S04", "cuidado": "S05", "arancel": "S03", "beneficio": "S03", "notas": "S01", "evaluaciones": "S01",
           "asistencia": "S08", "plataforma": "S09", "traslado": "S09", "entregas": "S08"}
    cods = list(dict.fromkeys(c for k, c in sug.items() if k in f["por_que"]))[:2] or ["S01"]
    nom = dict(zip(catalogo.id_servicio, catalogo.nombre))
    return (f"1. Lo que muestran los datos\nEn las primeras semanas aparecen {f['por_que']}. Estudia en jornada {str(f['jornada']).lower()} en "
            f"{f['area_carrera']}. Los datos no dicen por qué ocurre.\n\n2. Apoyos posibles\n" + "\n".join(f"- [{c}] {nom.get(c, '')}" for c in cods) +
            "\n\n3. Borrador de mensaje\nHola, ¿cómo vas en este inicio de semestre? Me gustaría conversar 15 minutos contigo para saber cómo "
            "te está yendo y ver si hay algo en lo que podamos apoyarte. Es voluntario y eliges el horario.")
ia = N.IA({"ficha": {r["id_estudiante"]: demo(r) for _, r in cola.iterrows()}})
decisiones = N.estado_equipo("decisiones")
cola["decision"] = cola.id_estudiante.map(lambda i: decisiones.get(i, "Pendiente"))
OPCIONES = ["Contactar esta semana", "Derivar a un servicio", "Esperar y observar", "No contactar"]

t1, t2 = st.tabs(["1 · Cola de la semana", "2 · Ficha y decisión"])
with t1:
    st.caption(f"Cupo: **{len(cola)} estudiantes** ({CUPO}% de una cohorte de {n_actual}). Variables que el modelo NO usa: {', '.join(EXCLUIDAS)}. "
               "El orden **no es una probabilidad** y no se muestra al estudiante.")
    st.dataframe(cola[["id_estudiante", "orden", "area_carrera", "jornada", "por_que", "decision"]].rename(columns={
        "id_estudiante": "Estudiante", "orden": "Orden", "area_carrera": "Área", "jornada": "Jornada", "por_que": "¿Por qué aparece?", "decision": "Decisión"}),
        hide_index=True, width="stretch", height=460)
with t2:
    sel = st.selectbox("Estudiante", cola.id_estudiante)
    f = cola[cola.id_estudiante == sel].iloc[0]
    st.markdown(f"**{sel}** · {f['area_carrera']} · {f['jornada']}  \n**¿Por qué aparece?** {f['por_que']}  \n**Check-in semana 4:** _{checkin(f)}_")
    with st.expander("Ver todos los datos"): st.text(datos_txt(f))
    clave = f"prop_{sel}"
    if st.button(cfg["texto_boton"], type="primary"):
        sistema = REGLAS + "\n\n" + N.personalizacion(cfg)
        pet = PETICION.format(datos=datos_txt(f), factores=f["por_que"], checkin=checkin(f), catalogo=S.texto(catalogo))
        with st.spinner("La IA está preparando la propuesta…"):
            texto, info = ia.llamar([{"role": "system", "content": sistema}, {"role": "user", "content": pet}], "ficha", sel)
        st.session_state[clave] = (texto, info)
    if clave in st.session_state:
        texto, info = st.session_state[clave]
        N.aviso_si_demo(info)
        prob = validar(texto)
        if prob:
            st.error("🔒 La validación detectó problemas. Corrige el texto antes de usarlo: " + "; ".join(prob))
            N.registrar({"tipo": "validacion", "tarea": "ficha", "id_estudiante": sel, "nota": "; ".join(prob)})
        final = st.text_area("Propuesta de la IA (revísala y edítala antes de usarla)", texto, height=300, key=f"ta_{sel}")
        st.markdown("#### 👤 Decisión humana (obligatoria)")
        dec = st.radio("¿Qué decides?", OPCIONES, index=None, key=f"dec_{sel}")
        util = st.select_slider("¿La propuesta te ahorró trabajo?", ["Nada", "Poco", "Algo", "Mucho"], value="Algo", key=f"ut_{sel}")
        nota = st.text_input("Nota (opcional)", key=f"nota_{sel}")
        if st.button("Registrar decisión"):
            if not dec: st.warning("Elige una decisión: la IA no decide por ti.")
            else:
                decisiones[sel] = dec
                N.registrar({"tipo": "decision_humana", "tarea": "ficha", "id_estudiante": sel, "decision": dec, "utilidad": util, "nota": nota, "salida": final})
                st.success(f"Decisión registrada para {sel}: **{dec}**")
N.pie(ia)
