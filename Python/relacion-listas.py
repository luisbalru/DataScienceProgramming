# Introducción a la programación en Ciencia de Datos
# Relación de ejercicios sobre listas
# Autor: Luis Balderas Ruiz


def sum_nums_lista(numeros):
    sum = 0
    for i in range(len(numeros)):
        sum += numeros[i]
    return(sum)


print("1. Escribe una función sum_nums_lista(numeros) que sume todos los números de una lista. Compara el tiempo entre usar o no range")
l = list(range(15))
print("La lista es: ")
print(l)
print("Su suma es " + str(sum_nums_lista(l)))

input("Pulsa enter para seguir")

def contar_numeros_impares(numeros):
    contador = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 != 0:
            contador += 1
    return(contador)


print("2. Escribe una función contar_numeros_impares(numeros) que cuente la cantidad de número impares que hay en una lista.")
l = list(range(15))
print("La lista es: ")
print(l)
print("El número de impares es " + str(contar_numeros_impares(l)))

input("Pulsa enter para seguir")

def numeros_pares(numeros):
    l = []
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            l.append(numeros[i])
    return(l)

print("3. Escribe una función numeros_pares(numeros) que devuelva los números pares que hay en una lista.")
l = list(range(15))
print("La lista es: ")
print(l)
print("Los pares son " + str(numeros_pares(l)))

input("Pulsa enter para seguir")

def combinar_listas(l1,l2):
    return l1+l2

print("4. Escribe una función combinar_listas(l1, l2) que devuelva una lista que esté formada por todos los elementos de l1 y a continuación todos los de l2")
l1 = list(range(14))
l2 = list(range(17,19))
print("Lista 1: " + str(l1))
print("Lista 2: " + str(l2))
print("Combinación: " + str(combinar_listas(l1,l2)))
input("Pulsa enter para seguir")


def mezclar(la,lb):
    l = la+lb
    l.sort()
    return(l)

print("5. Escribe una función mezclar(la, lb) que dadas dos listas ordenadas devuelva una lista conteniendo los elementos de ambas listas ordenados de forma ascendente.")
l1 = list(range(14,7,-1))
l2 = list(range(19,17,-1))
print("Lista 1: " + str(l1))
print("Lista 2: " + str(l2))
print("Mezcla y orden ascendente: " + str(mezclar(l1,l2)))

input("Pulsa enter para seguir")


def traspuesta(matriz):
    traspuesta = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[i])):
            fila.append(matriz[j][i])
        traspuesta.append(fila)
    return(traspuesta)


print("6. La traspuesta de una matriz se obtiene intercambiado filas y columna. Escribe una función que devuelva la traspuesta de una matriz.")
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print("La matriz es " + str(matriz))
t_matriz = traspuesta(matriz)
print("La traspuesta es" + str(t_matriz))

input("Pulsa enter para seguir")


def contar_letras(palabra):
    lista_auxiliar = []
    for i in range(len(palabra)):
        if palabra[i] not in lista_auxiliar:
            lista_auxiliar.append(palabra[i])
            lista_auxiliar.append(1)
        else:
            lista_auxiliar[lista_auxiliar.index(palabra[i])+1] += 1
    lista_final = []
    for i in range(len(lista_auxiliar)//2):
        lista_final.append((lista_auxiliar[2*i],lista_auxiliar[2*i+1]))
    return(lista_final)

print("7. Escribe una función contar_letras(palabra) que tome una palabra como argumento y devuelva una lista de pares en la que aparece cada letra junto con el número de veces que aparece esa letra en la palabra.")
palabra = "abecedario"
print("La palabra es " + palabra)
print("El número de letras es:")
print(contar_letras(palabra))
input("Pulsa enter para seguir")


def eliminar(l1,l2):
    lista = []
    for a in l1:
        if a not in l2:
            lista.append(a)
    return(lista)

print("8. Escribe una función eliminar(l1, l2) que dadas dos listas devuelva una lista en la que estén todos los elementos de l1 que no están en l2.")
l1 = list(range(8))
l2 = list(range(15))
print("Las listas son " +  str(l2) + " y " + str(l1))
print("Eliminar: " + str(eliminar(l2,l1)))
input("Pulsa enter para seguir")


def suma_acumulada(numeros):
    lista = []
    sum = 0
    for i in range(len(numeros)):
        for j in range(i+1):
            sum += numeros[j]
        lista.append(sum)
        sum = 0
    return(lista)

print("9. Escribe una función suma_acumulada(numeros) a la que se le pase una lista de números y devuelva una lista en la que el elemento i-ésimo se obtiene como la suma de los elementos de la lista entre las posiciones 0 e i")
l1 = list(range(5))
print("La lista dada es " + str(l1))
print("Resultado: " + str(suma_acumulada(l1)))
input("Pulsa enter para seguir")


import math

def parejas(lista):
    conjunto_lista = set(lista)
    n_distintos = len(conjunto_lista)
    # Permutaciones de n_distintos elementos más las parejas iguales (que sólo se cuentan una vez)
    numero_parejas = math.factorial(n_distintos) + (len(lista) - n_distintos)
    return(numero_parejas)

print("10. Escribe una función parejas(lista) que calcule las parejas distintas de valores que aparecen en una lista.")

lista = [0,1,1,2]
print("La lista es " + str(lista))
print("Número de parejas: " + str(parejas(lista)))

input("Pulsa enter para seguir")


def cadena_mas_larga(cadenas):
    return(max(cadenas))

print("11. Escribe una función cadena_mas_larga(cadenas) a la que se pasa una lista de palabras y que devuelva la palabra más larga.")
l = ["hola","holaa","holaaaa"]
print("Las palabras son " + str(l))
print("La más larga es " + str(cadena_mas_larga(l)))
input("Pulsa enter para seguir")


def suma_primer_digito(numeros):
    sum = 0
    for n in numeros:
        if n > 0:
            sum = sum + [int(d) for d in str(n)][0]
        else:
            sum = sum - [int(d) for d in str(-n)][0]
    return sum

print("12. Escribe una función suma_primer_digito(numeros) que devuelva la suma de los primeros dígitos de todos los números de la lista que se pasa como argumento.")


list = [-10,11,12,13,14]
print(list)
suma = suma_primer_digito(list)
print(suma)

input("Pulsa enter para seguir")



def dispersa(v):
    lista = []
    for i in range(len(v)):
        if v[i] != 0:
            lista.append((v[i],i))
    return(len(lista),lista)

print("13. Escribe una función dispersa(v) a la que se le pase una lista representando un vector disperso y que devuelva el número de elementos del vector junto con una lista de pares (pos, elem) con cada una de las posiciones en las que hay un elemento no nulo y el elemento.")
l = [0,0,0,1,0,0,1,0]
print("La lista es " + str(l))
print("Resultado: " +  str(dispersa(l)))
input("Pulsa enter para seguir")


from random import randrange

def sacar_carta(baraja):
    cartas_sacadas = []
    while(len(baraja) != 0):
        i = randrange(len(baraja))
        cartas_sacadas.append(baraja[i])
        baraja.pop(i)
    return cartas_sacadas


print("14. Escribe una función que saque de forma aleatoria todas las cartas de una baraja hasta que quede vacía. Para ello debe usar unalista que tenga inicialmente todas las cartas.")

baraja = ["1-O","1-E","1-B","1-C"]
print(baraja)
cartas = sacar_carta(baraja)
print(cartas)
input("Pulsa enter para seguir")
