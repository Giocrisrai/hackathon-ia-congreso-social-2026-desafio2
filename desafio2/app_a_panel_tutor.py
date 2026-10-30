"""Desafío 2 · Variante A · Radar de acompañamiento (panel del tutor).
Los equipos la personalizan en su copia de la planilla (pestañas `config` y `servicios_extra`)."""
import re, sys
from pathlib import Path
AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "comun")); sys.path.insert(0, str(AQUI))
import altair as alt
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
N.acceso()
cfg, extra = N.configuracion(str(AQUI / "planillas" / "Plantilla_config_D2_Variante_A.xlsx"), "servicios_extra", S.validar_servicio)
catalogo = S.catalogo(AQUI, extra)

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
NOMBRES_VAR = {"sexo": "sexo", "sede": "sede", "tipo_establecimiento_origen": "tipo de colegio", "jornada": "jornada", "edad": "edad",
               "anios_desde_egreso_media": "años desde la media", "primera_generacion": "primera generación", "gratuidad": "gratuidad",
               "tiempo_traslado_min": "traslado", "cuida_dependientes": "cuidado de personas", "egreso_liceo_tp": "liceo TP", "nem": "NEM",
               "area_carrera": "área", "tipo_carrera": "tipo de carrera"}
GRUPOS = {"jornada": "Jornada", "sexo": "Sexo", "tramo_edad": "Edad", "tipo_establecimiento_origen": "Tipo de colegio", "sede": "Sede"}

@st.cache_resource(show_spinner="Preparando la cohorte…")
def preparar(excluidas: tuple, cupo: int):
    ruta = AQUI / "datos" / "estudiantes_sinteticos_desafio2.csv"
    if not ruta.exists():  # el CSV no se versiona: se regenera igual (semilla fija) la primera vez
        sys.path.insert(0, str(AQUI / "datos")); import generar_estudiantes
        generar_estudiantes.generar().to_csv(ruta, index=False, encoding="utf-8")
    est = pd.read_csv(ruta)
    pasada, actual = train_test_split(est, test_size=0.3, random_state=7, stratify=est.deserta_primer_anio)
    actual = actual.reset_index(drop=True)
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
    # Equidad: a quién incluye la cola (la deserción real solo se conoce en datos sintéticos; en la vida real llega un año después)
    actual["_en_cola"] = False; actual.loc[orden, "_en_cola"] = True
    actual["tramo_edad"] = pd.cut(actual.edad, [0, 19, 24, 34, 120], labels=["17 a 19", "20 a 24", "25 a 34", "35 o más"]).astype(str)
    filas = []
    for col, nom in GRUPOS.items():
        for v, d in actual.groupby(col):
            des = d[d.deserta_primer_anio == 1]
            filas.append({"Grupo": nom, "Valor": str(v), "Estudiantes": len(d), "En la cola (%)": round(100 * d._en_cola.mean(), 1),
                          "Desertores alcanzados (%)": round(100 * des._en_cola.mean(), 1) if len(des) else None})
    equidad = pd.DataFrame(filas)
    cola = actual.iloc[orden].drop(columns=["deserta_primer_anio", "motivo_declarado_salida", "_en_cola"]).reset_index(drop=True)
    cola["n"] = range(1, k + 1)
    cola["orden"] = [f"{i + 1} de {k}" for i in range(k)]
    cola["por_que"] = ["; ".join(ETIQUETAS.get(nombres[j], nombres[j].replace("_", " ")) for j in np.argsort(-fila)[:3] if fila[j] > 0) for fila in contrib]
    return cola, len(actual), equidad

cola, n_actual, equidad = preparar(tuple(EXCLUIDAS), CUPO)
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
   Escríbelo listo para enviar: sin marcadores entre corchetes como [Nombre] (usa solo "Hola,").
5. La decisión final es del tutor.
6. Escribe en español de Chile, tuteando con "tú" (nunca "vos" ni formas como "elegís" o "tenés").
FORMATO: tres secciones con estos títulos: "1. Lo que muestran los datos", "2. Apoyos posibles", "3. Borrador de mensaje"."""
PETICION = """Datos del estudiante (ficticio):
{datos}
Señales que más pesaron en la priorización: {factores}
Check-in de la semana 4 (escrito por el estudiante): "{checkin}"
Catálogo de servicios:
{catalogo}

Recuerda: tutea con "tú" (eliges, puedes, quieres), nunca voseo; para cada apoyo usa solo lo que dice el catálogo."""

PROHIBIDAS_BORRADOR = re.compile(r"riesgo|deser|probabilid|predic|puntaje|\d+ ?%|algoritmo", re.I)
def validar(texto):
    problemas = []
    codigos = set(re.findall(r"\[([A-Z]{1,3}\d{1,3})\]", texto))
    malos = sorted(c for c in codigos if c not in set(catalogo.id_servicio))
    if malos: problemas.append(f"cita servicios que no existen en el catálogo: {', '.join(malos)}")
    if not codigos: problemas.append("no cita ningún servicio del catálogo con su código")
    borrador = texto.split("3.", 1)[1] if "3." in texto else texto
    if PROHIBIDAS_BORRADOR.search(borrador): problemas.append("el borrador menciona riesgo, deserción, porcentajes o predicciones")
    return problemas

def secciones(texto):
    """Separa la propuesta en sus tres secciones para mostrarlas como tarjetas (si la IA no respetó el formato, devuelve None)."""
    partes = re.split(r"(?m)^\s*\**\s*([123])\.\s*", texto or "")
    if len(partes) < 7: return None
    d = {partes[i]: partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}
    limpiar = lambda s: re.sub(r"^(Lo que muestran los datos|Apoyos posibles|Borrador de mensaje)\**\s*:?\s*", "", s, flags=re.I).strip()
    return [limpiar(d.get(k, "")) for k in "123"] if set(d) >= {"1", "2", "3"} else None

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

# ------------------------------------------------------------------ pantalla
N.encabezado(cfg["titulo_app"], cfg["texto_bienvenida"],
             [f"👥 {st.session_state.get('_equipo')}", f"🎯 Para: {N.corto(cfg.get('usuario'), 70)}", f"📋 Cupo semanal: {CUPO}%"])
N.aviso_ia()
hechas = int((cola.decision != "Pendiente").sum())
m1, m2, m3, m4 = st.columns(4)
m1.metric("Estudiantes en la cola", len(cola), help=f"{CUPO}% de una cohorte de {n_actual} estudiantes ficticios")
m2.metric("Decisiones registradas", f"{hechas} de {len(cola)}")
m3.metric("Contactar esta semana", int((cola.decision == "Contactar esta semana").sum()))
m4.metric("Consultas a la IA", f"{ia.usadas()} de {ia.limite}")

t1, t2, t3 = st.tabs(["📋 1 · Cola de la semana", "🗂️ 2 · Ficha y decisión", "⚖️ 3 · ¿A quién deja fuera?"])
with t1:
    st.markdown(N.badge("El orden no usa: " + ", ".join(NOMBRES_VAR.get(v, v) for v in EXCLUIDAS), "teal") + N.badge("El orden no es una probabilidad", "gray") +
                N.badge("No se muestra al estudiante", "gray"), unsafe_allow_html=True)
    f1, f2, f3 = st.columns([2, 2, 1], vertical_alignment="bottom")
    fj = f1.pills("Jornada", sorted(cola.jornada.unique()), selection_mode="multi")
    fa = f2.selectbox("Área", ["Todas"] + sorted(cola.area_carrera.unique()))
    solo = f3.toggle("Solo pendientes")
    vista = cola[(cola.jornada.isin(fj) if fj else cola.jornada.notna()) & (cola.area_carrera == fa if fa != "Todas" else cola.area_carrera.notna())]
    if solo: vista = vista[vista.decision == "Pendiente"]
    st.dataframe(vista[["n", "id_estudiante", "area_carrera", "jornada", "por_que", "decision"]].rename(columns={
        "n": "N°", "id_estudiante": "Estudiante", "area_carrera": "Área", "jornada": "Jornada", "por_que": "¿Por qué aparece?", "decision": "Decisión"}),
        hide_index=True, width="stretch", height=430,
        column_config={"N°": st.column_config.NumberColumn(width="small"), "¿Por qué aparece?": st.column_config.TextColumn(width="large")})
    st.caption(f"Mostrando {len(vista)} de {len(cola)}. Para preparar la conversación, ve a la pestaña **2 · Ficha y decisión**.")

with t2:
    NUM = dict(zip(cola.id_estudiante, cola.n))
    sel = st.selectbox("Estudiante", list(cola.id_estudiante), key="est_sel",
                       format_func=lambda i: f"N° {NUM.get(i, '?')} · {i}")
    f = cola[cola.id_estudiante == sel].iloc[0]
    izq, der = st.columns([1, 1.35], gap="large")
    with izq:
        N.tarjeta(f"{sel} · {f['area_carrera']}",
                  N.badge(f"Jornada {str(f['jornada']).lower()}", "teal") + N.badge(f"{int(f['edad'])} años", "gray") +
                  (N.badge("Trabaja por turnos", "amber") if f["trabajo_por_turnos"] == 1 else "") +
                  (N.badge("Personas a su cuidado", "amber") if f["cuida_dependientes"] == 1 else "") +
                  (N.badge("Primera generación", "gray") if f["primera_generacion"] == 1 else "") +
                  "<br>Decisión: " + N.badge(decisiones.get(sel, "Pendiente"), "gray" if sel not in decisiones else "green"), "info")
        a1, a2 = st.columns(2)
        a1.metric("Asistencia sem. 4–6", f"{f['asistencia_s4_s6_pct']:.0f}%", f"{f['asistencia_s4_s6_pct'] - f['asistencia_s1_s3_pct']:+.0f} pts vs. sem. 1–3")
        a2.metric("Nota parcial", f"{f['nota_promedio_parcial']:.1f}")
        a3, a4 = st.columns(2)
        a3.metric("Entregas atrasadas", int(f["entregas_atrasadas"]))
        a4.metric("Días sin plataforma", int(f["dias_desde_ultimo_login"]))
        st.markdown("**¿Por qué aparece?** " + "".join(N.badge(x.strip(), "amber") for x in f["por_que"].split(";") if x.strip()), unsafe_allow_html=True)
        st.markdown("**Check-in de la semana 4**")
        st.markdown(f'<div class="quote">{N.md(checkin(f))}</div>', unsafe_allow_html=True)
        with st.expander("Ver todos los datos"): st.text(datos_txt(f))
    with der:
        clave = f"prop_{sel}"
        if st.button(cfg["texto_boton"], type="primary", width="stretch"):
            sistema = REGLAS + "\n\n" + N.personalizacion(cfg)
            pet = PETICION.format(datos=datos_txt(f), factores=f["por_que"], checkin=checkin(f), catalogo=S.texto(catalogo))
            with st.spinner("La IA está preparando la propuesta…"):
                texto, info = ia.llamar([{"role": "system", "content": sistema}, {"role": "user", "content": pet}], "ficha", sel)
            st.session_state[clave] = (texto, info)
        if clave not in st.session_state:
            N.tarjeta("Propuesta de la IA", "Presiona el botón para que la IA prepare la conversación con este estudiante: "
                      "qué muestran los datos, qué apoyos del catálogo podrían servir y un borrador de mensaje.", "gray")
        else:
            texto, info = st.session_state[clave]
            N.aviso_si_demo(info)
            prob = validar(texto)
            if prob:
                st.error("🔒 La validación detectó problemas. Corrige el texto antes de usarlo: " + "; ".join(prob))
                N.registrar({"tipo": "validacion", "tarea": "ficha", "id_estudiante": sel, "nota": "; ".join(prob)})
            else:
                st.markdown(N.badge("✓ Validación superada: cita servicios del catálogo y el borrador no etiqueta", "green"), unsafe_allow_html=True)
            sec = secciones(texto)
            if sec:
                cods = [c for c in dict.fromkeys(re.findall(r"\[([A-Z]{1,3}\d{1,3})\]", sec[1])) if c in set(catalogo.id_servicio)]
                acceso = "".join(f"<br>{N.badge(c, 'teal')} {N.md(r.como_acceder)}" for c in cods for r in catalogo[catalogo.id_servicio == c].itertuples())
                N.tarjeta("1 · Lo que muestran los datos", N.md(sec[0]), "info")
                N.tarjeta("2 · Apoyos posibles", N.md(sec[1]) + (f"<br><br><b>Cómo se accede:</b>{acceso}" if acceso else ""), "ok")
                N.tarjeta("3 · Borrador de mensaje al estudiante", N.md(sec[2]), "warn" if prob else "ok")
            with st.expander("✏️ Revisar y editar el texto antes de usarlo", expanded=not sec):
                final = st.text_area("Propuesta de la IA", texto, height=260, key=f"ta_{sel}", label_visibility="collapsed")
            with st.container(border=True):
                st.markdown("#### 👤 Decisión humana (obligatoria)")
                dec = st.radio("¿Qué decides?", OPCIONES, index=None, key=f"dec_{sel}", horizontal=True)
                util = st.select_slider("¿La propuesta te ahorró trabajo?", ["Nada", "Poco", "Algo", "Mucho"], value="Algo", key=f"ut_{sel}")
                nota = st.text_input("Nota (opcional)", key=f"nota_{sel}")
                if st.button("Registrar decisión", width="stretch"):
                    if not dec: st.warning("Elige una decisión: la IA no decide por ti.")
                    else:
                        decisiones[sel] = dec
                        N.registrar({"tipo": "decision_humana", "tarea": "ficha", "id_estudiante": sel, "decision": dec, "utilidad": util,
                                     "nota": nota, "salida": st.session_state.get(f"ta_{sel}", texto)})
                        st.session_state["_flash"] = f"Decisión registrada para {sel}: **{dec}**"
                        st.rerun()
                if st.session_state.get("_flash"): st.success(st.session_state.pop("_flash"))

with t3:
    st.markdown("La cola tiene cupo limitado: alguien queda fuera. Aquí se ve **a qué grupos incluye** y **qué parte de quienes terminan desertando "
                "alcanza**, con la configuración actual. Cambien `variables_excluidas` o `cupo_porcentaje` en su planilla y comparen.")
    grupo = st.radio("Comparar por", list(GRUPOS.values()), horizontal=True)
    d = equidad[equidad.Grupo == (grupo or "Jornada")]
    largo = d.melt(id_vars=["Valor", "Estudiantes"], value_vars=["En la cola (%)", "Desertores alcanzados (%)"], var_name="Medida", value_name="Porcentaje")
    base = alt.Chart(largo).encode(
        y=alt.Y("Valor:N", title=None, sort=list(d.Valor)), yOffset=alt.YOffset("Medida:N", sort=["En la cola (%)", "Desertores alcanzados (%)"]),
        x=alt.X("Porcentaje:Q", title="% del grupo", scale=alt.Scale(domain=[0, min(100, 10 * np.ceil(float(largo.Porcentaje.max() or 0) * 1.15 / 10))])),
        color=alt.Color("Medida:N", scale=alt.Scale(domain=["En la cola (%)", "Desertores alcanzados (%)"], range=["#0F766E", "#F59E0B"]),
                        legend=alt.Legend(orient="top", title=None)),
        tooltip=["Valor", "Medida", alt.Tooltip("Porcentaje:Q", format=".1f"), "Estudiantes"])
    graf = (base.mark_bar(cornerRadiusEnd=4) + base.mark_text(align="left", dx=4, fontSize=12, color="#0F172A").encode(text=alt.Text("Porcentaje:Q", format=".1f")))
    st.altair_chart(graf.properties(height=alt.Step(24)).configure_axis(grid=False, labelFontSize=13).configure_view(stroke=None), use_container_width=True)
    if len(d) >= 2:
        alto, bajo = d.loc[d["En la cola (%)"].idxmax()], d.loc[d["En la cola (%)"].idxmin()]
        N.tarjeta("Para discutir en el equipo",
                  f"La cola incluye al <b>{alto['En la cola (%)']:.1f}%</b> del grupo «{N.md(alto.Valor)}» y al <b>{bajo['En la cola (%)']:.1f}%</b> "
                  f"del grupo «{N.md(bajo.Valor)}». ¿Refleja que necesitan más apoyo o es un sesgo? ¿Qué pasa con quien queda fuera?", "warn")
    st.caption("Datos sintéticos. En una institución real, quién deserta se sabe recién al año siguiente: esta comparación sirve para diseñar, no para evaluar personas.")
N.pie(ia)
