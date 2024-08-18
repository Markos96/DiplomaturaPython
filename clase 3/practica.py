'''
Crear una lista con 5 elemento. Luego recorre la lista con un for y suma todos los elementos. Finalmente muestra el resultado usando print
'''

lista = [10, 20, 40, 50]
suma = 0

for i in lista:
    suma = suma + i

print(f"La suma de los elementos es: {suma}")

'''
Solicita al usuario que ingrese un número. Luego, define
una lista con varios números enteros. Utiliza un ciclo for para verificar si el número ingresado por el usuario está en
la lista. Si está, muestra un mensaje que diga "El número se encuentra en la lista", si no, muestra "El número no
está en la lista".
'''

numero = int(input("Ingrese un numero: "))
existNumer = f"El {numero} existe en la lista" if numero in lista else f"El {numero} no existe en la lista"

print(existNumer)

'''
Crea una tupla con varios elementos repetidos.
Solicita al usuario que ingrese un elemento. Luego, usa un ciclo while para contar cuántas veces aparece el
elemento en la tupla. Muestra el resultado.
'''

tupla = (1,1,2,3,3,5,6,6,8,8,10,10)
elemento = int(input("Ingrese un elemento: "))
contador = 0
indice = 0

while indice < len(tupla):
    if tupla[indice] == elemento:
        contador += 1
    indice += 1

print(f"El elemento {elemento} aparece {contador} veces en la tupla.")

'''
Crea una lista con los números del 1 al 20. Luego, usa un ciclo for y un
condicional if para imprimir solo los números pares.
'''

listaPares = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

for numero in listaPares:
    if numero % 2 == 0:
        print(numero)

'''
Solicita al usuario que ingrese 5 palabras y guárdalas en una lista. Luego, utiliza un
ciclo for para imprimir la lista en orden inverso.
'''

palabras = []

for i in range(5):
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)

for i in range(len(palabras)-1, -1, -1):
    print(palabras[i])
