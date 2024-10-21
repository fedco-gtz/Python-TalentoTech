# |-----------------------------------------|
# | Ejercicio 1 - Suma de números naturales |
# |-----------------------------------------|

def suma_numeros_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Ingresa un número "))
resultado = suma_numeros_naturales(n)
print(f"La suma de los números naturales hasta {n} es {resultado}")
