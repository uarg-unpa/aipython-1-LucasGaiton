# Solicitar la edad del usuario
edad_str = input("Ingrese su edad: ")

# Convertir la entrada a un número entero
edad = int(edad_str)

if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    anos_faltantes = 18 - edad
    print(f"Le faltan {anos_faltantes} años para poder conducir.")