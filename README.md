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
```
## 🔧 Configuración
### Hacer login

1️⃣ **Iniciar sesión**  
Inicia el script `login.py` para generar un `sessionID`.

```bash
python login.py --login
```
2️⃣ **Ingresa tu usuario y contraseña**

Sigue las instrucciones en consola para ingresar tus credenciales de forma segura.

3️⃣ **Verifica que tu sessionID esté escrito en el archivo `session.json`**
```bash
cat session.json
```
### Hacer logout
1️⃣ **Cerrar sesión**
Inicia el script `login.py` con el argumento para limpiar la sesión.
```bash
python login.py --clear-session
```
## 📜 Ejemplos de Uso

A continuación, te muestro cómo puedes utilizar `INSTAOSINT` para extraer información valiosa de perfiles de Instagram:

- **Obtener información completa del usuario**
Utiliza este comando para obtener detalles completos de un perfil de usuario específico.
```bash
python3 instaosint_v1.py --info
```
- **Obtener lista de seguidores con correos y teléfonos**
Este comando te permite listar los seguidores de un perfil, incluyendo sus correos electrónicos y números de teléfono si están disponibles.
```bash
python3 instaosint_v1.py --followers
```
- **Obtener lista de seguidos con correos y teléfonos **
Con este comando, puedes obtener una lista de los perfiles que un usuario está siguiendo, junto con sus correos y teléfonos.
```bash
python3 instaosint_v1.py --following
```
