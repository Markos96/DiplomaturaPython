
"""
Crea un programa que solicite al usuario el nombre y la edad. Luego muestra por pantalla la informacion completa utilizando f-string
"""

nombre = input("¿Cual es tu nombre? ")
edad = input("¿Cual es tu edad? ")

print(f"Tu nombre es {nombre} y tienes {edad} años")

"""
Crea un programa para pedirle al usuario que ingrese una cantidad de metros y luego convertir ese valor a centimetros
Imprimir el resultado utilizando f-string
"""

metros = float(input("Ingrese cantidad de metros: "))

print(f"La cantidad de centimetros es: {metros * 100}")

"""
Escribe un programa que defina tres variables a, b y c. Asigna a cada una un valor numérico y luego muestra la
suma de las tres utilizando una f-string. Escribe comentarios que expliquen cada parte del código.
"""

a = 10
b = 15
c = 20

print(f"La suma es: {a + b + c}")