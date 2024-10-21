# |-------------------------------------|
# | Ejercicio 2 - Acumulador de números |
# |                                     |
# | Pedir al usuario que ingrese 5      |
# | números. El programa debe mostrar   |
# | la suma total de los números        |
# | ingresados al final.                |
# |-------------------------------------|

suma_total = 0

for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    suma_total += numero

print(f"La suma total de los números ingresados es: {suma_total}")
