"""Visita las 4 apps de la hackathon y las despierta si Streamlit Cloud las durmió.
Lo ejecuta GitHub Actions cada 4 horas (.github/workflows/mantener_apps_despiertas.yml).

Streamlit Community Cloud a veces falla de forma intermitente (archivos de la interfaz con
error 502 o páginas que no llegan). Por eso cada app tiene hasta 3 intentos con una página
nueva, y si al final no carga se guarda una captura en capturas/ para diagnosticar.

Uso local: pip install playwright && playwright install chromium && python scripts/despertar_apps.py"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

APPS = {
    "D2 · A Radar": "https://hackaton-d2-a.streamlit.app/",
    "D2 · B Acompaña": "https://hackaton-d2-b.streamlit.app/",
    "D3 · A Pausa antes de compartir": "https://hackaton-d3-pausa.streamlit.app/",
    "D3 · B La ley en simple": "https://hackaton-d3-ley.streamlit.app/",
}
LISTA = "Ingreso del equipo"   # texto que muestra cada app cuando ya cargó
INTENTOS = 3
ESPERA_S = 120                 # por intento
CAPTURAS = Path("capturas")


def cargada(pagina) -> bool:
    for f in pagina.frames:  # la app corre dentro de un iframe
        try:
            if LISTA in (f.content() or ""):
                return True
        except Exception:
            pass
    return False


def un_intento(navegador, nombre, url) -> tuple[bool, str]:
    pagina = navegador.new_page(viewport={"width": 1200, "height": 800})
    errores = []
    pagina.on("response", lambda r: errores.append(r.status) if r.status >= 500 else None)
    try:
        pagina.goto(url, wait_until="domcontentloaded", timeout=60_000)
        pagina.wait_for_timeout(5_000)
        boton = pagina.get_by_role("button", name="Yes, get this app back up!")
        if boton.count():
            print(f"💤 {nombre}: dormida → despertando", flush=True)
            boton.first.click()
        for _ in range(ESPERA_S // 5):
            if cargada(pagina):
                return True, ""
            pagina.wait_for_timeout(5_000)
        CAPTURAS.mkdir(exist_ok=True)
        archivo = CAPTURAS / f"{nombre.split('·')[0].strip()}_{nombre.split('·')[1].strip().split()[0]}.png"
        pagina.screenshot(path=str(archivo))
        return False, f"sin cargar en {ESPERA_S} s; respuestas 5xx: {len(errores)}"
    except Exception as e:
        return False, f"{type(e).__name__}: {str(e)[:120]}"
    finally:
        pagina.close()


def revisar(navegador, nombre, url) -> bool:
    for n in range(1, INTENTOS + 1):
        ok, motivo = un_intento(navegador, nombre, url)
        if ok:
            print(f"✅ {nombre}: en línea" + (f" (intento {n})" if n > 1 else ""), flush=True)
            return True
        print(f"⚠️ {nombre}: intento {n} de {INTENTOS} falló ({motivo})", flush=True)
    print(f"❌ {nombre}: no cargó en {INTENTOS} intentos ({url})", flush=True)
    return False


with sync_playwright() as p:
    nav = p.chromium.launch()
    resultados = [revisar(nav, n, u) for n, u in APPS.items()]
    nav.close()
print(f"Resumen: {sum(resultados)} de {len(resultados)} apps en línea", flush=True)
sys.exit(0 if all(resultados) else 1)
