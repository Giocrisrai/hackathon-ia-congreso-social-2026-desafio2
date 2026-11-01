"""Visita las 4 apps de la hackathon y las despierta si Streamlit Cloud las durmió.
Lo ejecuta GitHub Actions cada 4 horas (.github/workflows/mantener_apps_despiertas.yml).
Uso local: pip install playwright && playwright install chromium && python scripts/despertar_apps.py"""
import sys
from playwright.sync_api import sync_playwright

APPS = {
    "D2 · A Radar": "https://hackaton-d2-a.streamlit.app/",
    "D2 · B Acompaña": "https://hackaton-d2-b.streamlit.app/",
    "D3 · A Pausa antes de compartir": "https://hackaton-d3-pausa.streamlit.app/",
    "D3 · B La ley en simple": "https://hackaton-d3-ley.streamlit.app/",
}
LISTA = "Ingreso del equipo"   # texto que muestra cada app cuando ya cargó


def revisar(pagina, nombre, url) -> bool:
    pagina.goto(url, wait_until="domcontentloaded", timeout=60_000)
    pagina.wait_for_timeout(5_000)
    boton = pagina.get_by_role("button", name="Yes, get this app back up!")
    if boton.count():
        print(f"💤 {nombre}: dormida → despertando", flush=True)
        boton.first.click()
    # La app corre dentro de un iframe; se busca el texto en todos los frames durante hasta 4 minutos
    for _ in range(48):
        if any(LISTA in (f.content() or "") for f in pagina.frames):
            print(f"✅ {nombre}: en línea", flush=True)
            return True
        pagina.wait_for_timeout(5_000)
    print(f"❌ {nombre}: no cargó en 4 minutos ({url})", flush=True)
    return False


with sync_playwright() as p:
    nav = p.chromium.launch()
    pagina = nav.new_page()
    resultados = [revisar(pagina, n, u) for n, u in APPS.items()]
    nav.close()
sys.exit(0 if all(resultados) else 1)
