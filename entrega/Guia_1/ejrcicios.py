# ## #PUNTO 1
# ## #A)
# print("Las máquinas me sorprenden con mucha frecuencia")

# ## #B)

# ## #C)
# print("Tus propios mensajes")

# ###D)
# print("23", 23)
# ## #Lo que sucedio fue que el primer dato mostrados son de distintos tipos uno es un string y el otro es un entero

### #E)
# print("Una computadora puede ser llamada 'inteligente' si logra engañar a una persona haciéndole creer que es un humano.")
# ##F
# print("Lucas", "Gaiton")
## #g
# print("Lucas", "Gaiton", sep=" ")
# ##h
# print("calle", "numero", "codigo postal", sep="\t")
## #i
# print("calle \n numero \n codigo postal ")
# #j
# lineaSalto = "\n"
# tabulacion = "\t"
# print("feliz"+lineaSalto+tabulacion+"Navidad"+lineaSalto+tabulacion+tabulacion+"2023")
# #k
# print("Solo podemos ver poco del futuro,", "pero lo suficiente para darnos cuenta de que hay mucho que hacer")
# #I
# print("    *    ")
# print("   * *   ")
# print("  *   *  ")
# print(" *     * ")
# print("***   ***")
# print("  *   *  ")
# print("  *   *  ")
# print("  *****  ")

###### # PUNTO 3
# nombre="Lucas"
# apellido="Gaiton"
# edad=19
# altura=1.75
# vueloNum=425
# ambienteTem=16
# salarioMen=1800
# endGame=True
# isPar=False

#### #PUNTO 5 
# nombre=input("Ingrese su nombre ")
# apellido=input("Ingrese su apellido ")
# edad=input("Ingrese su edad ")
# print(f"Como estas {nombre} {apellido}. Te ves muy bien para tener {edad} años")

####PUNTO 6
# num1 = int(input("Ingrese el primer número entero: "))
# num2 = int(input("Ingrese el segundo número entero: "))

# suma = num1 + num2
# resta = num1 - num2
# producto = num1 * num2
# potencia = num1 ** num2
# resto = num1 % num2

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Producto: {producto}")
# print(f"Potencia: {potencia}")
# print(f"Resto: {resto}")

### #PUNTO 7
# num1 = int(input("Ingrese el número entero: "))
# num2 = float(input("Ingrese el número decimal: "))

# suma = num1 + num2
# resta = num1 - num2
# producto = num1 * num2
# potencia = num1 ** num2

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Producto: {producto}")
# print(f"Potencia: {potencia}")

# #PUNTO 8

# #Rectangulo:
# base_rectangulo = int(input("Ingrese la base del rectángulo: "))
# altura_rectangulo = int(input("Ingrese la altura del rectángulo: "))

# perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)

# area_rectangulo = base_rectangulo * altura_rectangulo

# print(f"Perímetro del rectángulo: {perimetro_rectangulo}")
# print(f"Área del rectángulo: {area_rectangulo}")

# #Circunferencia:
# radio_circunferencia = float(input("Ingrese el radio de la circunferencia: "))

# perimetro_circunferencia = 2 * math.pi * radio_circunferencia
# area_circunferencia = math.pi * radio_circunferencia ** 2

# print(f"Perímetro de la circunferencia: {perimetro_circunferencia}")
# print(f"Área de la circunferencia: {area_circunferencia}")

# #PUNTO 9

# peso = float(input("Ingrese su peso en kg: "))
# altura = float(input("Ingrese su altura en metros: "))

# imc = peso / (altura ** 2)

# print(f"Tu índice de masa corporal es: {imc}")

# #PUNTO 10
# celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# # Realizo conversión a grados Fahrenheit
# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

# #PUNTO 11

# horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
# costo_por_hora = float(input("Ingrese el costo por hora: "))

# sueldo = horas_trabajadas * costo_por_hora

# print(f"El sueldo correspondiente es: {sueldo}")

# #PUNTO 12

# cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
# interes_anual = float(input("Ingrese el interés anual sin el %: "))
# num_años = int(input("Ingrese el número de años: "))

# # Calcular el capital obtenido en la inversión
# interes_decimal = interes_anual / 100
# capital = cantidad_invertir * (1 + interes_decimal)**num_años

# print(f"El capital obtenido en la inversión es: {capital:.2f}") #Lo ponemos en formato flotante con 2 digitos

# #PUNTO 13

# suma_precios = 0
# cantidad_productos = input("Ingrese la cantidad de productos")
# for i in range(1, cantidad_productos + 1):
#     precio = float(input(f"Ingrese el precio del producto {i}: "))
#     suma_precios += precio

# promedio = suma_precios / cantidad_productos

# print(f"El promedio de precios de los 10 productos es: {promedio:.2f}")

# #PUNTO 14

# resultado = 'Una ambiciosa' + ' Introducción' + ' a Python' + ' Parte 1'
# print(resultado)

# #PUNTO 15

# #a
# sociedad = 'aiPython P1'
# print(sociedad)

# #b
# longitud = len(sociedad)
# print("Longitud de la variable sociedad:", longitud)

# #c
# sociedad_mayusculas = sociedad.upper()
# print("Variable sociedad en mayúsculas:", sociedad_mayusculas)

# #d
# sociedad_minusculas = sociedad.lower()
# print("Variable sociedad en minúsculas:", sociedad_minusculas)

# #PUNTO 16
# cadena = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."

# capitalizada = cadena.capitalize()
# print("Capitalize:", capitalizada)

# titulada = cadena.title()
# print("Title:", titulada)

# intercambiada = cadena.swapcase()
# print("Swapcase:", intercambiada)

# #PUNTO 17

# nombre_completo = input("Por favor, ingresa tu nombre completo: ")
# for _ in range(3):
#     print(nombre_completo)

# #PUNTO 18

# # print("    *****    ")
# # print("   *     *   ")
# # print("  *       *  ")
# # print(" *         * ")
# # print("***       ***")
# # print("  *       *  ")
# # print("  *       *  ")
# # print("  *********  ")

# #PUNTO 19
# print("    *****    /n   *     *   /n  *       *  /n *         * /n***       ***/n  *       *  /n  *       *  /n  *********  ")

# #PUNTO 21
# palabra = input("Ingresa una palabra: ")

# palabra_modificada = palabra.replace('a', '�')

# print("Palabra modificada:", palabra_modificada)

#PUNTO 22

frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."

# Divide la frase en palabras
palabras = frase.split()

print(' '.join(palabras[2:len(palabras)]))

#PUNTO 23
frase = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
frase_sin_espacios = frase.strip()

print(frase_sin_espacios)

#PUNTO 24
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."
frase_separada = frase[:2] + '\n' + frase[2:]

print(frase_separada)

#PUNTO 25 
data = "Nombre\tEdad\tPais\tCiudad\nAlexa\t25\tUSA\tCapeCod"
print(data)













