inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))

print(f"Números entre {inicio} y {fin}:")
for numero in range(inicio + 1, fin):
    print(numero, end=" ")