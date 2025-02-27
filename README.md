# INSTAOSINT 🕵️‍♂️

`INSTAOSINT` es una herramienta de inteligencia OSINT para Instagram que permite realizar diversas operaciones de recopilación de información de perfiles públicos.

## 🚀 Comenzando

Estos son los pasos para empezar a usar `INSTAOSINT`:

### Prerrequisitos

Asegúrate de tener Python instalado en tu sistema. `INSTAOSINT` requiere Python 3.6 o superior.

### Instalación

Clona el repositorio y navega al directorio del proyecto:

```bash
git clone https://tu-repositorio/instaosint.git
cd instaosint

## Configuración

###🔹 Hacer login

1️⃣ **Iniciar sesión**  
Inicia el script `login.py` para generar un `sessionID`.

```bash
python login.py --login

2️⃣ **Ingresa tu usuario y contraseña**

Sigue las instrucciones en consola para ingresar tus credenciales de forma segura.

3️⃣ **Verifica que tu sessionID esté escrito en el archivo `session.json`**
```bash
cat session.json
###🔹  Hacer logout
1️⃣ **Cerrar sesión**
Inicia el script `login.py` con el argumento para limpiar la sesión.
