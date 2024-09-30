# |-------------------------------------|
# | Ejercicio 2 - Compra con Descuentos |
# |-------------------------------------|

# Función para calcular el descuento según la cantidad de artículos y el monto total
def calcular_descuento(monto_total, cantidad_articulos):
    descuento = 0

    if cantidad_articulos >= 5 and monto_total > 10000:
        descuento = 0.15
    elif 3 <= cantidad_articulos < 5:
        descuento = 0.10

    monto_con_descuento = monto_total - (monto_total * descuento)
    return monto_con_descuento, descuento

# Solicitar los datos del usuario
monto_total = float(input("Ingrese el monto total de la compra: $"))
cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))

# Calcular el monto final y el descuento aplicado
monto_final, descuento_aplicado = calcular_descuento(monto_total, cantidad_articulos)

# Mostrar los resultados
if descuento_aplicado > 0:
    print(f"\nSe aplicó un descuento del {int(descuento_aplicado * 100)}%.")
else:
    print("\nNo se aplicó ningún descuento.")

print(f"El monto final a pagar es: ${monto_final:.2f}")
