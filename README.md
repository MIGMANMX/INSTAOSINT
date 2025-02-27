# INSTAOSINT
🔹 Hacer login
1️⃣ Iniciar el script login.py para generar sessionID </br>
python login.py --login
2️⃣ Teclea tu usuario y contraseña</br>

</br></br>
3️⃣ Verifica que tu sessionID este escrto en el archivo "session.json" </br>
cat session.json
</br></br>


🔹 Hacer logout
1️⃣ Iniciar el script login.py para generar sessionID </br>
python login.py --clear-session
2️⃣ Verifica que tu archivo "session.json" se elimino </br>
cat session.json </br></br>


🔹 Comandos



🔹 Ejemplo de uso

1️⃣ Obtener información completa del usuario </br>
python3 instaosint_v1.py <USUARIO> --info </br></br>

2️⃣ Obtener lista de seguidores con correos y teléfonos</br>
python3 instaosint_v1.py <USUARIO> --followers</br></br>

3️⃣ Obtener lista de seguidos con correos y teléfonos</br>
python3 instaosint_v1.py <USUARIO> --following</br></br>
