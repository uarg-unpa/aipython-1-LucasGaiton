# Obtener la edad del usuario
edad_usuario_str = input("Ingrese su edad: ")

# Convertir la entrada a un número entero
edad_usuario = int(edad_usuario_str)

# Defino mi edad
mi_edad = 19  

# Comparar las edades y proporcionar mensajes correspondientes
if edad_usuario > mi_edad:
    diferencia = edad_usuario - mi_edad
    if diferencia == 1:
        print(f"Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif edad_usuario < mi_edad:
    diferencia = mi_edad - edad_usuario
    if diferencia == 1:
        print(f"Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("¡Somos de la misma edad!")