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


# 7. Escribe una función comunes(palabra1, palabra2) que devuelva una cadena formada por los
# caracteres comunes a las dos palabras.

def comunes(palabra1,palabra2):
    letras_comunes = ""
    l1 = len(palabra1)
    l2 = len(palabra2)
    if l1 < l2:
        for i in range(l1):
            if palabra1[i] in palabra2:
                letras_comunes = letras_comunes + palabra1[i]
    else:
        for i in range(l2):
            if palabra2[i] in palabra1:
                letras_comunes = letras_comunes + palabra2[i]
    return letras_comunes

print("Ejercicio 7: Escribe una función comunes(palabra1, palabra2) que devuelva una cadena formada por los caracteres comunes a las dos palabras.")
print("Letras en común en las palabras noria y novia")
print(comunes("noria","novia"))
print("Letras en común en las palabras pana y tapas")
print(comunes("pana","tapas"))


# 8. Escribe una función eco_palabra(palabra) que devuelva una cadena formada por palabra
# repetida tantas veces como sea su longitud. Por ejemplo 'hola' -> 'holaholaholahola'

def eco_palabra(palabra):
    l = len(palabra)
    eco = ""
    for i in range(l):
        eco = eco + palabra
    return eco

print("Ejercicio 8: Escribe una función eco_palabra(palabra) que devuelva una cadena formada por palabra repetida tantas veces como sea su longitud. Por ejemplo 'hola' -> 'holaholaholahola'")
print("Eco de hola: " + eco_palabra("hola"))
print("Eco de abecedario: " + eco_palabra("abecedario"))


# 9. Escribe una función palindromo(frase) que determine si frase es un palíndromo. Es decir,
# que se lea igual de izquierda a derecha que de derecha a izquierda (sin considerar espacios).

def palindromo(frase):
    l = len(frase)
    frase = frase.lower()
    for i in range(l):
        if(frase[i] != frase[l-i-1]):
            return False
    return True

print("Ejercicio 9: Escribe una función palindromo(frase) que determine si frase es un palíndromo.")
print("¿Es palíndromo Amor a Roma?")
print(palindromo("Amor a Roma"))
print("¿Es palíndromo hola que tal?")
print(palindromo("hola que tal"))


# 10. Escribe una función orden_alfabetico(palabra) que determine si las letras que forman
# palabra aparecen en orden alfabético. Por ejemplo: 'abejo'

def orden_alfabetico(palabra):
    l = len(palabra)
    for i in range(l):
        if i+1 < l:
            if palabra[i] > palabra[i+1]:
                return False
    return True

print("Ejercicio 10: Escribe una función orden_alfabetico(palabra) que determine si las letras que forman palabra aparecen en orden alfabético.")
print("Probamos con abejo")
print(orden_alfabetico("abejo"))
print("¿Y abeja?")
print(orden_alfabetico("abeja"))


# 11. Escribe una función trocear(palabra, num) que devuelva una lista con trozos de tamaño
# num de palabra.

def trocear(palabra,num):
    trozos = []
    i = 0
    l = len(palabra)
    while i < l:
        trozos.append(palabra[i:(i+num)])
        i = i + num
    return trozos

print("Ejercicio 11: Escribe una función trocear(palabra, num) que devuelva una lista con trozos de tamaño num de palabra.")
print("Trozos de 2 letras para abecedario")
print(trocear("abecedario",2))
print("Trozos de 3 letras para abecedario")
print(trocear("abecedario",3))
"""
