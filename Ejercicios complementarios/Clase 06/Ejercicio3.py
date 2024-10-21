# |---------------------------------------------------|
# | Ejercicio 3 - Contador de números pares e impares |
# |                                                   |
# | Pedir al usuario que ingrese 5 números. El        |
# | programa debe contar cuántos de esos números      |
# | son pares y cuántos son impares, y luego          |
# | mostrar los resultados.                           |
# |---------------------------------------------------|

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
