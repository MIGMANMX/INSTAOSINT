import requests
import json
import argparse
import os
import pandas as pd

# Configuración del User-Agent
HEADERS = {
    "User-Agent": "Instagram 219.0.0.12.117 Android"
}

SESSION_FILE = "session.json"  # Archivo donde se almacenará la sesión

def load_session():
    """Carga la sesión desde un archivo si existe."""
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            data = json.load(f)
        return data.get("sessionid")
    return None

def get_profile_info(username):
    """Obtiene información básica del perfil de Instagram (incluye user_id)."""
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("user", {})
    else:
        print(f"[-] Error: {response.status_code} - {response.text}")
        return None

def get_user_info(user_id, sessionid):
    """Obtiene información detallada del usuario desde la API privada."""
    url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
    cookies = {"sessionid": sessionid}

    response = requests.get(url, headers=HEADERS, cookies=cookies)
    if response.status_code == 200:
        return response.json().get("user", {})
    else:
        print(f"[-] Error al obtener detalles del usuario: {response.status_code} - {response.text}")
        return None

def get_all_followers_or_following(user_id, mode, sessionid):
    """Obtiene TODOS los seguidores o seguidos utilizando paginación."""
    url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{mode}/?count=100"
    cookies = {"sessionid": sessionid}
    all_users = []
    next_max_id = None

    while True:
        if next_max_id:
            url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{mode}/?count=100&max_id={next_max_id}"
        
        response = requests.get(url, headers=HEADERS, cookies=cookies)
        
        if response.status_code == 200:
            data = response.json()
            users = data.get("users", [])
            all_users.extend(users)
            next_max_id = data.get("next_max_id")
            
            if not next_max_id:
                break  # No hay más páginas
        else:
            print(f"[-] Error al obtener {mode}: {response.status_code} - {response.text}")
            break

    return all_users

def get_user_contact(user_id, sessionid):
    """Obtiene correo electrónico y teléfono de un usuario desde la API privada."""
    user_info = get_user_info(user_id, sessionid)
    if not user_info:
        return "No disponible", "No disponible"

    email = user_info.get("public_email", "No disponible")
    phone = user_info.get("contact_phone_number", "No disponible")
    return email, phone

def display_table(data, title):
    """Muestra los datos en formato tabular usando pandas."""
    if not data:
        print(f"[-] No hay datos disponibles para {title}.")
        return
    
    df = pd.DataFrame(data)
    pd.set_option("display.max_columns", None)
    print(f"\n📌 {title} 📌")
    print(df.to_markdown(index=False))

def main():
    parser = argparse.ArgumentParser(description="Script para obtener información detallada de Instagram.")
    parser.add_argument("username", help="Nombre de usuario de Instagram a analizar")
    parser.add_argument("--info", action="store_true", help="Obtener información completa del usuario")
    parser.add_argument("--followers", action="store_true", help="Obtener lista de seguidores con contacto")
    parser.add_argument("--following", action="store_true", help="Obtener lista de seguidos con contacto")
    
    args = parser.parse_args()

    sessionid = load_session()
    if not sessionid:
        print("[-] No hay sesión activa. Usa '--login' para iniciar sesión.")
        return

    user_data = get_profile_info(args.username)
    if not user_data:
        print("[-] No se pudo obtener información básica del usuario.")
        return

    user_id = user_data.get("id")
    if not user_id:
        print("[-] No se pudo obtener el ID del usuario.")
        return

    if args.info:
        user_details = get_user_info(user_id, sessionid)
        if not user_details:
            print("[-] No se pudo obtener información detallada del usuario.")
            return
        
        info_data = [
            {"Campo": "Nombre", "Valor": user_details.get("full_name", "No disponible")},
            {"Campo": "Usuario", "Valor": user_details.get("username", "No disponible")},
            {"Campo": "Biografía", "Valor": user_details.get("biography", "No disponible")},
            {"Campo": "Correo", "Valor": user_details.get("public_email", "No disponible")},
            {"Campo": "Teléfono", "Valor": user_details.get("contact_phone_number", "No disponible")},
            {"Campo": "Dirección", "Valor": user_details.get("address_street", "No disponible")},
            {"Campo": "Total Publicaciones", "Valor": user_details.get("media_count", "No disponible")},
            {"Campo": "Seguidores", "Valor": user_details.get("follower_count", "No disponible")},
            {"Campo": "Siguiendo", "Valor": user_details.get("following_count", "No disponible")},
            {"Campo": "Cuenta Privada", "Valor": "Sí" if user_details.get("is_private") else "No"},
            {"Campo": "Cuenta Verificada", "Valor": "Sí" if user_details.get("is_verified") else "No"},
            {"Campo": "Categoría", "Valor": user_details.get("category", "No disponible")},
        ]
        display_table(info_data, "Información Completa del Usuario")

    if args.followers or args.following:
        if args.followers:
            print("[+] Obteniendo lista completa de seguidores...")
            followers = get_all_followers_or_following(user_id, "followers", sessionid)
            follower_data = []
            for f in followers:
                email, phone = get_user_contact(f["pk"], sessionid)
                follower_data.append({
                    "Usuario": f["username"],
                    "Nombre Completo": f["full_name"],
                    "Privada": "Sí" if f["is_private"] else "No",
                    "Verificada": "Sí" if f["is_verified"] else "No",
                    "Categoría": f.get("category_name", "No disponible"),
                    "Correo": email,
                    "Teléfono": phone,
                })
            display_table(follower_data, f"Lista de Seguidores ({len(followers)} total)")

        if args.following:
            print("[+] Obteniendo lista completa de seguidos...")
            following = get_all_followers_or_following(user_id, "following", sessionid)
            following_data = []
            for f in following:
                email, phone = get_user_contact(f["pk"], sessionid)
                following_data.append({
                    "Usuario": f["username"],
                    "Nombre Completo": f["full_name"],
                    "Privada": "Sí" if f["is_private"] else "No",
                    "Verificada": "Sí" if f["is_verified"] else "No",
                    "Categoría": f.get("category_name", "No disponible"),
                    "Correo": email,
                    "Teléfono": phone,
                })
            display_table(following_data, f"Lista de Seguidos ({len(following)} total)")

if __name__ == "__main__":
    main()

