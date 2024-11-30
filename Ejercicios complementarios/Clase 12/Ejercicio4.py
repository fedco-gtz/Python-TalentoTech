# |----------------------------------------------------|
# | Ejercicio 4 -  Diseña una función que tome una     |
# | lista de números y devuelva la suma de los números |
# | positivos.                                         |
# |----------------------------------------------------|

def sumar_positivos(lista_numeros):
    return sum(numero for numero in lista_numeros if numero > 0)

numeros = [-3, 5, -1, 7, -8, 2]
resultado = sumar_positivos(numeros)
print("La suma de los números positivos es:", resultado)
