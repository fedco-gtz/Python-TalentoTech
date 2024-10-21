# |------------------------------------------|
# | Ejercicio 2 - Registro de ventas por día |
# |------------------------------------------|

def registrar_ventas():
    ventas_totales = 0
    dias = 5

    for dia in range(1, dias + 1):
        while True:
            try:
                venta = float(input(f"Ingrese el monto de ventas del día {dia}: "))
                if venta > 0:
                    ventas_totales += venta
                    break
                else:
                    print("El monto debe ser un valor positivo.")
            except ValueError:
                print("Ingrese un valor numérico válido.")

    promedio_ventas = ventas_totales / dias
    print(f"Total de ventas en 5 días: {ventas_totales}")
    print(f"Promedio de ventas por día: {promedio_ventas}")

registrar_ventas()
