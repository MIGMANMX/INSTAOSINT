import requests
import json
import argparse
import os

# Configurar Headers para simular un navegador
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

SESSION_FILE = "session.json"  # Archivo donde se almacenará la sesión

def login_instagram(username, password):
    """Inicia sesión en Instagram y obtiene la cookie de sesión (sessionid)."""
    session = requests.Session()
    
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    
    # Obtener la cookie csrf
    response = session.get("https://www.instagram.com/", headers=HEADERS)
    csrf_token = response.cookies.get("csrftoken", "")

    payload = {
        "username": username,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{int(0)}:{password}",
        "queryParams": {},
        "optIntoOneTap": "false"
    }
    
    headers = HEADERS.copy()
    headers.update({
        "X-CSRFToken": csrf_token,
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/"
    })
    
    response = session.post(login_url, data=payload, headers=headers)

    if response.status_code == 200 and response.json().get("authenticated"):
        sessionid = session.cookies["sessionid"]
        print("[+] Login exitoso. SessionID obtenido.")
        
        # Guardar sesión en archivo JSON
        with open(SESSION_FILE, "w") as f:
            json.dump({"sessionid": sessionid}, f)
        
        return sessionid
    else:
        print("[-] Error al iniciar sesión:", response.text)
        return None

def load_session():
    """Carga la sesión desde un archivo si existe."""
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            data = json.load(f)
        return data.get("sessionid")
    return None

def clear_session():
    """Elimina la sesión guardada."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
        print("[+] Sesión eliminada con éxito.")
    else:
        print("[-] No hay sesión guardada para eliminar.")

def get_instagram_data(username, sessionid):
    """Consulta la API web de Instagram con autenticación usando sessionid."""
    cookies = {"sessionid": sessionid}
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"
    response = requests.get(url, headers=HEADERS, cookies=cookies)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None



# Argumentos CLI
parser = argparse.ArgumentParser(description="Script OSINT para obtener información de Instagram con autenticación automática.")
parser.add_argument("--login", action="store_true", help="Iniciar sesión en Instagram con usuario y contraseña")
parser.add_argument("--clear-session", action="store_true", help="Eliminar la sesión guardada y volver a iniciar sesión")

args = parser.parse_args()

# Manejo de sesión
if args.clear_session:
    clear_session()
    exit()

if args.login:
    user = input("Instagram Usuario: ")
    password = input("Instagram Contraseña: ")
    sessionid = login_instagram(user, password)
else:
    sessionid = load_session()

if not sessionid:
    print("[-] No hay sesión activa. Usa '--login' para iniciar sesión.")
    exit()
