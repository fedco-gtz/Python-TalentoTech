# |---------------------------------------------|
# | Ejercicio 2 - Cálculo de promedio de ventas |
# |---------------------------------------------|

def calcular_promedio_ventas(ventas):
    total_ventas = sum(ventas)
    promedio = total_ventas / len(ventas)
    return promedio

ventas_diarias = []

for i in range(7):
    venta = float(input(f"Ingrese la venta del día {i + 1}: "))
    ventas_diarias.append(venta)

promedio_ventas = calcular_promedio_ventas(ventas_diarias)
print(f"El promedio de ventas de la semana es: {promedio_ventas}")
