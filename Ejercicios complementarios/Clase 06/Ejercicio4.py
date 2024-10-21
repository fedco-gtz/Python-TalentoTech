# |---------------------------------------|
# | Ejercicio 4 - Sumar números positivos |
# |                                       |
# | Pedir al usuario que ingrese números  |
# | hasta que ingrese un número negativo. |
# | El programa debe sumar solo los       |
# | números positivos y mostrar el total  |
# | acumulado al final.                   |
# |---------------------------------------|

suma_total = 0

while True:
    numero = float(input("Ingrese un número (ingrese un número negativo para detenerse): "))
    
    if numero < 0:
        break
    suma_total += numero

print(f"La suma total de los números positivos es: {suma_total}")
