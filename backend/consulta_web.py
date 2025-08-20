import requests
import time
import tldextract
from bs4 import BeautifulSoup
import re
import unicodedata
import whois

def consulta_web(url_web):
    print(f"[consulta_web] Iniciando consulta a: {url_web}")

    # Si la URL no tiene esquema, le ponemos https://
    if not url_web.startswith(("http://", "https://")):
        url_web = "http://" + url_web

    try:
        start = time.perf_counter()
        res = requests.get(url_web, timeout=5)
        end = time.perf_counter()
        latency_ms = (end - start) * 1000
        print(f"[consulta_web] Respuesta recibida: {res.status_code}, Latencia: {latency_ms:.2f} ms")
        return {
            'status_code': res.status_code,
            'latency_ms': latency_ms
        }
    except Exception as e:
        print(f"[consulta_web] Error al consultar {url_web}: {e}")
        return None
    

def consulta_fecha_nacional(url_web):
    print(f"[consulta_fecha_nacional] Consultando NIC Chile para: {url_web}")
    url_clear = _limpiar_url(url_web)
    url = f"https://www.nic.cl/registry/Whois.do?d={url_clear}"
    
    headers = { "User-Agent": "Mozilla/5.0" }
    try:
        res = requests.get(url, headers=headers)
        print(f"[consulta_fecha_nacional] Status code NIC Chile: {res.status_code}")
    except Exception as e:
        print(f"[consulta_fecha_nacional] Error al consultar NIC Chile: {e}")
        return None

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        table = soup.find("table", class_="tablabusqueda")

        if table:
            print("[consulta_fecha_nacional] Tabla encontrada, extrayendo datos...")
            data = {}
            for row in table.find_all("tr"):
                tds = row.find_all("td")
                if tds:
                    divs = tds[0].find_all("div")
                    if divs and len(divs) >= 2:
                        key = divs[0].get_text(strip=True)
                        # Normalizar, quitar acentos y caracteres raros
                        key = unicodedata.normalize('NFKD', key).encode('ascii', 'ignore').decode('ascii')
                        key = re.sub(r'[^a-zA-Z0-9_]', '', key.replace(' ', '_'))
                        value = divs[1].get_text(strip=True)
                        data[key] = value
            print(f"[consulta_fecha_nacional] Datos extraídos: {data}")
            return data
        else:
            print("[consulta_fecha_nacional] No se encontró la tabla en el HTML")
            return None
    else:
        print(f"[consulta_fecha_nacional] Error al acceder a la página NIC Chile: {res.status_code}")
        return None
    


def obtener_info_dominio(dominio):
    try:
        print(f"[consulta_fecha_NO_nacional] Consultando WHOIS Chile para: {dominio}")
        w = whois.whois(dominio)

        print(w)
        
        return {
            "Fecha_de_creacion": str(w.creation_date[0]) if w.creation_date[0] else None,
            "Fecha_de_expiracion": str(w.expiration_date[0]) if w.expiration_date[0] else None,
            "Titular": w.org if hasattr(w, "org") else None
        }
    except Exception as e:
        print(f"Error al consultar WHOIS: {e}")
        return None
    

def _limpiar_url(url):
    print(f"[_limpiar_url] Limpiando URL: {url}")
    extracted = tldextract.extract(url)
    domain = f"{extracted.domain}.{extracted.suffix}"
    print(f"[_limpiar_url] Dominio limpio: {domain}")
    return domain

def is_website(url):
    print(f"[is_website] Validando URL: {url}")
    if not url.startswith(('http://', 'https://')):
        url_to_check = 'http://' + url
    else:
        url_to_check = url

    ip_regex = r"^(?:http[s]?://)?(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?(?:/.*)?$"
    url_regex = r"^(http[s]?://)?([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(/.*)?$"

    if re.match(ip_regex, url_to_check):
        print(f"[is_website] Es una IP, no un dominio: {url_to_check}")
        return False
    if re.match(url_regex, url_to_check):
        print(f"[is_website] Es una URL válida de dominio: {url_to_check}")
        return True
    print(f"[is_website] No es una URL válida: {url_to_check}")
    return False

def is_national(url):
    print(f"[is_national] Verificando si el dominio es nacional (.cl): {url}")
    extracted = tldextract.extract(url)
    result = extracted.suffix == "cl"
    print(f"[is_national] ¿Es nacional?: {result}")
    return result

def obtener_info_web(URL):
    print(f"[obtener_info_web] Obteniendo información para: {URL}")
    is_valid = is_website(URL)

    if is_valid:
        is_nacional = is_national(URL)
        info = consulta_fecha_nacional(URL) if is_nacional else obtener_info_dominio(URL)
        
        data ={
            'url': URL,
            'is_national': is_nacional,
            'consulta_web': consulta_web(URL),
            'consulta_fecha_nacional': info
        }
        print(f"[obtener_info_web] Datos obtenidos: {data}")
    else:
        
        data ={
            'url': URL,
            'is_national': False,
            'consulta_web': consulta_web(URL),
            'consulta_fecha_nacional': None
        }
        print(f"[obtener_info_web] URL no válida, datos: {data}")

    return data