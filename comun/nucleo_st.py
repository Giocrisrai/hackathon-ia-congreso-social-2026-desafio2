"""
🔒 NÚCLEO COMÚN · Plantillas Hackathon IA Congreso Social UC 2026 · Desafío 2
Misma lógica que las plantillas del Desafío 3 (G. Pinto): app pública + código y clave de
equipo + planilla de Google por equipo (pestaña `config` con campos + pestaña de extras).

Los equipos NO editan este código. Protecciones fijas:
  · aviso de uso de IA                 · código/clave de equipo y clave de IA ocultos (secrets)
  · registro de consultas y respuestas · límite de consultas por equipo
  · reglas fijas en los prompts        · validación de respuestas · modo demostración
"""
from __future__ import annotations
import datetime, hashlib, io, json, os, re, threading, time
from pathlib import Path
import pandas as pd
import requests
import streamlit as st

AVISO_IA = ("⚠️ **Esta herramienta usa inteligencia artificial.** Puede equivocarse y **no reemplaza el criterio "
            "de una persona**: la decisión final siempre es humana. Lo que se consulta y responde queda registrado "
            "para la revisión de la hackathon. Prototipo con datos ficticios.")
AVISO_DEMO = ("Se muestra una respuesta de demostración: la IA no respondió. Esperen un minuto y prueben de nuevo; "
              "si persiste, avisen a su mentor.")
URLS = {"openai": "https://api.openai.com/v1/chat/completions",
        "groq": "https://api.groq.com/openai/v1/chat/completions",
        "mistral": "https://api.mistral.ai/v1/chat/completions"}
MODELOS = {"openai": "gpt-4o-mini", "groq": "llama-3.3-70b-versatile", "mistral": "mistral-small-latest"}
REGISTRO = Path(os.environ.get("REGISTRO_IA", "registro_ia.jsonl"))

def _secret(ruta, defecto=None):
    try:
        n = st.secrets
        for p in ruta.split("."):
            n = n[p]
        return n
    except Exception:
        return defecto

@st.cache_resource
def _global():
    return {"lock": threading.Lock(), "consultas": {}, "equipos": {}}

def estado_equipo(clave: str) -> dict:
    g = _global()
    with g["lock"]:
        return g["equipos"].setdefault(f"{st.session_state.get('_app')}|{st.session_state.get('_equipo')}|{clave}", {})

# ------------------------------------------------------------------ registro
_lock = threading.Lock()
def registrar(ev: dict):
    ev = {"marca_tiempo": datetime.datetime.now().isoformat(timespec="seconds"), "app": st.session_state.get("_app"),
          "equipo": st.session_state.get("_equipo"), "planilla": st.session_state.get("_sheet_url", ""), **ev}
    with _lock:
        with open(REGISTRO, "a", encoding="utf-8") as f:
            f.write(json.dumps(ev, ensure_ascii=False, default=str) + "\n")
    _copiar_central(ev)

def _copiar_central(ev):
    sid, cred = _secret("registro.sheet_id"), _secret("gcp_service_account")
    if not sid or not cred:
        return
    try:
        import gspread  # type: ignore
        if "_ws" not in st.session_state:
            st.session_state["_ws"] = gspread.service_account_from_dict(dict(cred)).open_by_key(sid).sheet1
        st.session_state["_ws"].append_row([str(ev.get(k, ""))[:45000] for k in
                                            ("marca_tiempo", "app", "equipo", "tipo", "tarea", "modo", "proveedor", "entrada", "salida", "decision", "nota")])
    except Exception as e:
        st.session_state["_aviso_reg"] = f"No se pudo copiar el registro a la planilla central: {str(e)[:80]}"

def registro_equipo() -> pd.DataFrame:
    if not REGISTRO.exists():
        return pd.DataFrame()
    filas = []
    for l in REGISTRO.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(l)
        except Exception:
            continue
        if e.get("equipo") == st.session_state.get("_equipo") and e.get("app") == st.session_state.get("_app"):
            filas.append(e)
    return pd.DataFrame(filas)

# ------------------------------------------------------------------ página y acceso
def iniciar(app_id: str, titulo: str, icono: str):
    st.set_page_config(page_title=titulo, page_icon=icono, layout="wide")
    st.session_state["_app"] = app_id

def aviso_ia():
    st.info(AVISO_IA)

def acceso() -> str:
    """Código y clave de equipo, guardados en secrets:
    [equipos.E01]  nombre = "Equipo 01"  clave = "..."   (sin secrets: código 'demo', clave 'demo')."""
    if st.session_state.get("_equipo"):
        return st.session_state["_equipo"]
    equipos = {k: dict(v) for k, v in dict(_secret("equipos", {}) or {}).items() if hasattr(v, "keys")}
    st.subheader("🔐 Ingreso del equipo")
    c1, c2 = st.columns(2)
    cod = c1.text_input("Código de equipo").strip().upper()
    cla = c2.text_input("Clave", type="password").strip()
    if st.button("Entrar", type="primary"):
        if cod in equipos and cla == str(equipos[cod].get("clave", "")):
            st.session_state["_equipo"] = equipos[cod].get("nombre", cod)
            registrar({"tipo": "ingreso"}); st.rerun()
        elif not equipos and cod == "DEMO" and cla == "demo":
            st.session_state["_equipo"] = "demo"; st.rerun()
        else:
            st.error("Código o clave incorrectos. Los entrega su mentor.")
    if not equipos:
        st.caption("Instalación de prueba: código `demo`, clave `demo`.")
    st.stop()

# ------------------------------------------------------------------ planilla del equipo
_ID = re.compile(r"/spreadsheets/d/([a-zA-Z0-9-_]+)")

@st.cache_data(ttl=600, show_spinner=False)
def _descargar(sheet_id: str) -> dict:
    """Descarga la planilla completa como .xlsx (todas las pestañas, texto tal cual)."""
    r = requests.get(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", timeout=25)
    if r.status_code in (401, 403) or "text/html" in r.headers.get("Content-Type", "") or not r.content.startswith(b"PK"):
        raise ValueError("No se pudo leer la planilla: compártanla como 'Cualquier persona con el vínculo · Lector'.")
    r.raise_for_status()
    return {k.strip(): v.fillna("").astype(str) for k, v in pd.read_excel(io.BytesIO(r.content), sheet_name=None, dtype=str).items()}

@st.cache_data(show_spinner=False)
def _base(ruta: str) -> dict:
    """Plantilla base: carpeta con un CSV por pestaña (versionable en GitHub) o, si no existe, el .xlsx."""
    carpeta = Path(ruta).with_suffix("")
    if carpeta.is_dir():
        return {f.stem: pd.read_csv(f, dtype=str).fillna("") for f in sorted(carpeta.glob("*.csv"))}
    return {k: v.fillna("").astype(str) for k, v in pd.read_excel(ruta, sheet_name=None, dtype=str).items()}

def configuracion(ruta_plantilla: str, pestana_extra: str, validar_fila) -> tuple[dict, pd.DataFrame]:
    """Devuelve (config: campo→valor, filas_extra válidas). Valores vacíos → valor de la plantilla base.
    validar_fila(fila) devuelve '' si la fila es válida, o el motivo para ignorarla."""
    base = _base(ruta_plantilla)
    with st.sidebar:
        st.markdown(f"**Equipo:** {st.session_state.get('_equipo')}")
        url = st.text_input("🔗 URL de la copia de su planilla", value=st.session_state.get("_sheet_url", ""))
        if st.button("🔄 Recargar configuración", width="stretch"):
            st.session_state["_sheet_url"] = url.strip()
            _descargar.clear()
            registrar({"tipo": "recarga_configuracion", "entrada": url.strip()})
    hojas, origen = {}, "plantilla base"
    m = _ID.search(st.session_state.get("_sheet_url", ""))
    if m:
        try:
            hojas, origen = _descargar(m.group(1)), "su planilla"
        except Exception as e:
            st.sidebar.error(str(e)[:160])
    cfg_base = dict(zip(base["config"]["campo"].str.strip(), base["config"]["valor"]))
    cfg = dict(cfg_base)
    if "config" in hojas and {"campo", "valor"} <= set(hojas["config"].columns):
        for c, v in zip(hojas["config"]["campo"].str.strip(), hojas["config"]["valor"]):
            if c in cfg and str(v).strip():
                cfg[c] = str(v).strip()
    extra = hojas.get(pestana_extra, base.get(pestana_extra, pd.DataFrame()))
    validas, ignoradas = [], []
    for i, fila in extra.iterrows():
        idf = str(fila.iloc[0]).strip() if len(fila) else ""
        if not idf or idf.upper() == "EJEMPLO":
            continue
        motivo = validar_fila(fila)
        (ignoradas.append(f"Fila {i + 2} ({idf}): {motivo}") if motivo else validas.append(fila))
    extra_ok = pd.DataFrame(validas).reset_index(drop=True) if validas else pd.DataFrame(columns=extra.columns)
    with st.sidebar:
        st.caption(f"Configuración leída desde: **{origen}**")
        st.caption(f"Pestaña `{pestana_extra}`: {len(extra_ok)} fila(s) agregada(s)")
        if ignoradas:
            with st.expander(f"⚠️ {len(ignoradas)} fila(s) ignorada(s) · qué corregir"):
                for x in ignoradas: st.write("• " + x)
    return cfg, extra_ok

def personalizacion(cfg: dict) -> str:
    """Bloque que se agrega al prompt fijo con los campos que edita el equipo."""
    return (f"PERSONALIZACIÓN DEL EQUIPO (no puede contradecir las reglas fijas anteriores):\n"
            f"- Usuario: {cfg.get('usuario', '')}\n- Tono: {cfg.get('tono', '')}\n- Largo de la respuesta: {cfg.get('largo_respuesta', '')}\n"
            f"- Reglas extra del equipo: {cfg.get('instrucciones_extra', '') or '(ninguna)'}\n"
            f"- Ejemplos de respuesta ideal (imita el estilo, NO copies los datos): {cfg.get('ejemplos', '') or '(ninguno)'}")

# ------------------------------------------------------------------ IA
class IA:
    def __init__(self, respuestas_demo: dict | None = None):
        self.orden = list(_secret("ia.orden", ["openai", "groq", "mistral"]))
        self.prov = {p: {"clave": _secret(f"ia.{p}.api_key", ""), "modelo": _secret(f"ia.{p}.modelo", MODELOS.get(p, "")),
                         "url": _secret(f"ia.{p}.url", URLS.get(p, ""))} for p in self.orden}
        self.limite = int(_secret("ia.limite_consultas_por_equipo", 120))
        self.sin_claves = not any(v["clave"] for v in self.prov.values())
        self.demo = respuestas_demo or {}

    def _k(self): return f"{st.session_state.get('_app')}|{st.session_state.get('_equipo')}"
    def usadas(self): return _global()["consultas"].get(self._k(), 0)

    def estado(self):
        if self.sin_claves: return "🟡 Modo demostración (sin conexión a la IA)"
        if self.usadas() >= self.limite: return f"🟠 Límite de {self.limite} consultas alcanzado: modo demostración"
        return f"🟢 Consultas del equipo: {self.usadas()}/{self.limite}"

    def llamar(self, mensajes, tarea, clave_demo="", json_mode=False, temperatura=0.3, max_tokens=700):
        info = {"tipo": "llamada_ia", "tarea": tarea, "entrada": mensajes[-1]["content"],
                "prompt_hash": hashlib.sha1(mensajes[0]["content"].encode()).hexdigest()[:10]}
        motivo = "demo (sin claves)"
        if not self.sin_claves:
            if self.usadas() >= self.limite:
                motivo = "demo (límite de consultas)"
            else:
                for p in self.orden:
                    c = self.prov[p]
                    if not c["clave"]: continue
                    t0 = time.time()
                    try:
                        texto = self._post(c, mensajes, json_mode, temperatura, max_tokens)
                        g = _global()
                        with g["lock"]: g["consultas"][self._k()] = g["consultas"].get(self._k(), 0) + 1
                        info.update(modo="real", proveedor=p, modelo=c["modelo"], latencia_s=round(time.time() - t0, 2), salida=texto)
                        registrar(info); return texto, info
                    except Exception as e:
                        info.setdefault("errores", []).append(f"{p}: {str(e)[:150]}")
                motivo = "demo (falla de conexión)"
        b = self.demo.get(tarea, {})
        texto = (b.get(str(clave_demo)) or b.get("_por_defecto") or "[Demostración] Sin respuesta preparada.") if isinstance(b, dict) else str(b)
        info.update(modo=motivo, proveedor="-", salida=texto); registrar(info)
        return texto, info

    @staticmethod
    def _post(c, mensajes, json_mode, temperatura, max_tokens):
        cuerpo = {"model": c["modelo"], "messages": mensajes, "temperature": temperatura, "max_tokens": max_tokens}
        if json_mode: cuerpo["response_format"] = {"type": "json_object"}
        for i in range(2):
            r = requests.post(c["url"], json=cuerpo, timeout=45, headers={"Authorization": f"Bearer {c['clave']}"})
            if r.status_code == 429 and i == 0:
                time.sleep(3); continue
            r.raise_for_status()
            return r.json()["choices"][0]["message"]["content"].strip()
        r.raise_for_status()

def aviso_si_demo(info: dict):
    modo = str(info.get("modo", ""))
    if modo == "real" or not modo:
        return
    if "límite" in modo:
        st.warning("Se alcanzó el límite de consultas del equipo: se muestra una respuesta de demostración. Avisen a su mentor.")
    elif "sin claves" in modo:
        st.caption("🟡 Respuesta de demostración (instalación sin conexión a la IA).")
    else:
        st.warning(AVISO_DEMO)

def extraer_json(texto):
    m = re.search(r"(\{.*\}|\[.*\])", texto or "", re.S)
    if not m: return None
    try: return json.loads(m.group(1))
    except Exception: return None

# ------------------------------------------------------------------ filtros fijos
_CRISIS = [r"suicid", r"matarme", r"quitarme la vida", r"no quiero (seguir )?vivir", r"hacerme da[ñn]o", r"autolesi", r"cortarme",
           r"terminar con todo", r"me quiero morir", r"me pega", r"me golpea", r"abus[oa]", r"violaci"]
MENSAJE_CRISIS = (
    "Gracias por contarlo. Lo que describes es importante y mereces apoyo de una persona ahora, no de una IA.\n\n"
    "• Si piensas en hacerte daño, llama a la **Línea de Prevención del Suicidio \\*4141** (gratuita, desde celulares) "
    "o a **Salud Responde 600 360 7777**.\n• En una emergencia, llama al **131 (SAMU)** o acude a urgencias.\n\n"
    "Avisé al equipo de apoyo para que una persona te contacte. _(En la hackathon es una simulación: no se contacta a nadie real.)_")
def crisis(texto): return any(re.search(p, (texto or "").lower()) for p in _CRISIS)

# ------------------------------------------------------------------ barra lateral común
def pie(ia: IA):
    with st.sidebar:
        st.divider(); st.caption(ia.estado())
        if st.session_state.get("_aviso_reg"): st.warning(st.session_state["_aviso_reg"])
        df = registro_equipo()
        st.download_button("📥 Descargar registro del equipo", df.to_csv(index=False).encode("utf-8"),
                           file_name=f"registro_{st.session_state.get('_app')}_{st.session_state.get('_equipo')}.csv",
                           mime="text/csv", width="stretch", disabled=df.empty)
        if st.button("Salir", width="stretch"):
            for k in ["_equipo", "_sheet_url"]: st.session_state.pop(k, None)
            st.rerun()
