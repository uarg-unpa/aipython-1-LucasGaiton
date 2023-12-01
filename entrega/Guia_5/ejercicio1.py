#1
def multiplicar(a, b):
    return a * b
#2
def multiplicar2(a=1, b=1):
    return a * b
#3
def mensaje_creativo(nombre):
    return f"Hola, {nombre} sos cra como messi"

#4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
#5
def parimpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
#6
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

#7
def maximo_entre_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
#8 (utilizo "slicing")
def invertir_string(texto):
    return texto[::-1]