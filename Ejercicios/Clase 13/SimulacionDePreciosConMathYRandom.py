# |-------------------------------------------------------|
# | Ejercicio 2 - Simulación de precios con math y random |
# |-------------------------------------------------------|

import random
import math

def generar_precios():
    precios = []
    for _ in range(10):
        precio = random.uniform(10.00, 100.00)
        precio_redondeado = math.floor(precio * 100) / 100
        precios.append(precio_redondeado)
    return precios

precios_simulados = generar_precios()
print("Precios simulados:")
for i, precio in enumerate(precios_simulados, start=1):
    print(f"Producto {i}: ${precio:.2f}")


