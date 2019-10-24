# Introducción a la programación en ciencia de datos
# Ejercicios 1
# Autor: Luis Balderas Ruiz

# 1. Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que
# aparece una letra en una palabra.
"""
def contar_letras(palabra,letra):
    return palabra.count(letra)

print("Ejercicio 1: Escribe una función contar_letras(palabra, letra) que devuelva el número de veces que aparece una letra en una palabra.")
palabra = "albaricoque"
print("La palabra elegida es " + palabra)
print("Número de a's")
print(contar_letras(palabra,"a"))
print("Número de u's")
print(contar_letras(palabra,"u"))
print("Número de m's")
print(contar_letras(palabra,"m"))


# 2. Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de palabra que
# no contiene el carácter letra.

def eliminar_letras(palabra,letra):
    return palabra.replace(letra, '')

print("Ejercicio 2: Escribe una función eliminar_letras(palabra, letra) que devuelva una versión de palabra que no contiene el carácter letra.")
palabra = "banana"
print("La palabra elegida es " + palabra)
print("Eliminamos las a's")
print(eliminar_letras(palabra,'a'))
print("Eliminamos la b")
print(eliminar_letras(palabra,'b'))


# 3. Escribe una función buscar(palabra, sub) que devuelva la posición en la que se puede
# encontrar sub dentro de palabra o -1 en caso de que no esté.

def buscar(palabra, sub):
    return palabra.find(sub)

print("Ejercicio 3:  Escribe una función buscar(palabra, sub) que devuelva la posición en la que se puede encontrar sub dentro de palabra o -1 en caso de que no esté.")
palabra = "estoico"
print("La palabra elegida es " + palabra)
print("Índice de la letra s")
print(buscar(palabra,'s'))
print("Índice de la letra a")
print(buscar(palabra,'a'))


# 4. Escribe una función num_vocales(palabra) que devuelva el número de vocales que aparece
# en la palabra.

def num_vocales(palabra):
    vocales = "aeiou"
    num_voc = 0
    for l in palabra:
        if l in vocales:
            num_voc = num_voc + 1
    return num_voc

print("Ejercicio 4: Escribe una función num_vocales(palabra) que devuelva el número de vocales que aparece en la palabra.")
palabra = "abecedario"
print("La palabra elegida es " + palabra)
print("El número de vocales es " + str(num_vocales(palabra)))
print("Otra palabra, por ejemplo, elefante")
print("El número de vocales es " + str(num_vocales("elefante")))


# 5. Escribe una función vocales(palabra) que devuelva las vocales que aparecen en la palabra.

def vocales(palabra):
    vocales = "aeiou"
    vocales_presentes = []
    for l in palabra:
        if l in vocales:
            vocales_presentes.append(l)
    return vocales_presentes

print("Ejercicio 5: Escribe una función vocales(palabra) que devuelva las vocales que aparecen en la palabra.")
palabra = "abecedario"
print("La palabra elegida es " + palabra)
print("Las vocales son:")
print(vocales(palabra))


# 6. Escribe una función es_inversa(palabra1, palabra2) que devuelve True si una palabra es la
# misma que la otra pero con los caracteres en orden inverso. Por ejemplo 'absd' y 'dsba'

def es_inversa(palabra1,palabra2):
    p1 = len(palabra1)
    p2 = len(palabra2)
    if p1 == p2:
        for i in range(p1):
            if palabra1[i] != palabra2[p2-i-1]:
                return False
        return True
    else:
        return False

print("Ejercicio 6:  Escribe una función es_inversa(palabra1, palabra2) que devuelve True si una palabra es la misma que la otra pero con los caracteres en orden inverso. Por ejemplo 'absd' y 'dsba'")
print("Para absd, dsba")
print(es_inversa("absd","dsba"))
print("Para manolo,olon")
print(es_inversa("manolo","olon"))
"""
