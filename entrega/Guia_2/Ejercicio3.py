# Solicitar la contraseña al usuario
contrasena_usuario = input("Ingrese su contraseña: ")

contrasena_guardada = "ContraseñaSecreta123"

if contrasena_usuario.lower() == contrasena_guardada.lower():
    print("¡Contraseña correcta! Acceso permitido.")
else:
    print("Contraseña incorrecta. Vuelva a intentar.")