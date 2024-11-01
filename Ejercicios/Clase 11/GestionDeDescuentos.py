# |-------------------------------------|
# | Ejercicio 1 - Gestión de descuentos |
# |-------------------------------------|

def calcular_precio_final(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final

precio = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

precio_con_descuento = calcular_precio_final(precio, descuento)
print(f"El precio final después de aplicar el descuento es: {precio_con_descuento}")
