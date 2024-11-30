# |----------------------------------------------------|
# | Ejercicio 3 -  Escribe una función que tome un     |
# | número como argumento y devuelva "par" o "impar".  |
# | Mostrar ese retorno por pantalla desde el programa |
# | principal (fuera de la funcion)                    |
# |----------------------------------------------------|

def determinar_paridad(numero):
    return "par" if numero % 2 == 0 else "impar"

numero = int(input("Ingrese un número: "))
resultado = determinar_paridad(numero)
print(f"El número {numero} es {resultado}.")
