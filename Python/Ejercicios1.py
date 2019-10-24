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
"""
