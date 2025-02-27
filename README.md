# INSTAOSINT 🕵️‍♂️

`INSTAOSINT` es una herramienta de inteligencia OSINT para Instagram que permite realizar diversas operaciones de recopilación de información de perfiles públicos.
## ⚠️ Disclaimer

- **Uso del software**: Este software se proporciona "como está" y sin garantías de ningún tipo, expresas o implícitas. Úselo bajo su propio riesgo.
- **Cuentas de Instagram**: No utilice su cuenta personal de Instagram para evitar riesgos de bloqueo o baneo por parte de Meta debido al uso de automatizaciones.
- **Mantenimiento de la cuenta**: Se recomienda iniciar sesión periódicamente en la cuenta utilizada a través de la web oficial o la aplicación móvil para reducir el riesgo de bloqueos automáticos.
- **Responsabilidad del usuario**: Cualquier uso indebido del software que conduzca a actividades maliciosas es responsabilidad exclusiva del usuario.


## 🚀 Comenzando

Estos son los pasos para empezar a usar `INSTAOSINT`:

### Prerrequisitos

Asegúrate de tener Python instalado en tu sistema. `INSTAOSINT` requiere Python 3.6 o superior.

### Instalación

Clona el repositorio y navega al directorio del proyecto:

```bash
git clone https://github.com/MIGMANMX/INSTAOSINT.git
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

![](https://github.com/MIGMANMX/INSTAOSINT/blob/c66826606e3fc5ba0e8f1da80cb715cda6e6f81a/files/login-session.png)

3️⃣ **Verifica que tu sessionID esté escrito en el archivo `session.json`**
```bash
cat session.json
```
![](https://github.com/MIGMANMX/INSTAOSINT/blob/c66826606e3fc5ba0e8f1da80cb715cda6e6f81a/files/sessionID.png)

### Hacer logout
1️⃣ **Cerrar sesión**
Inicia el script `login.py` con el argumento para limpiar la sesión.
```bash
python login.py --clear-session
```
![](https://github.com/MIGMANMX/INSTAOSINT/blob/c66826606e3fc5ba0e8f1da80cb715cda6e6f81a/files/clear-session.png)

## 📜 Ejemplos de Uso

A continuación, te muestro cómo puedes utilizar `INSTAOSINT` para extraer información valiosa de perfiles de Instagram:

- **Obtener información completa del usuario**
Utiliza este comando para obtener detalles completos de un perfil de usuario específico.
```bash
python3 instaosint_v1.py --info
```
![](https://github.com/MIGMANMX/INSTAOSINT/blob/c66826606e3fc5ba0e8f1da80cb715cda6e6f81a/files/info.png)

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
![](https://github.com/MIGMANMX/INSTAOSINT/blob/c66826606e3fc5ba0e8f1da80cb715cda6e6f81a/files/following.png)

## 🤝 Contribuir
Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será muy apreciada.

## ⚖️ Licencia
Distribuido bajo la licencia MIT. Consulta el archivo LICENSE para más información.
