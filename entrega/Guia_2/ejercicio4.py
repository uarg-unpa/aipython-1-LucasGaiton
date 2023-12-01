# Obtener dos números del usuario
a = float(input("Ingrese el primer número (a): "))
b = float(input("Ingrese el segundo número (b): "))

if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")