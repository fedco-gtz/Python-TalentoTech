# |---------------------------------------------|
# | Ejercicio 2 - Consultar stock en inventario |
# |---------------------------------------------|

inventario = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 20,
    "Bananas": 15,
    "Uvas": 25
}

nombre_producto = input("Ingrese el nombre del producto que desea consultar: ")

stock_disponible = inventario.get(nombre_producto)

if stock_disponible is not None:
    print(f"Producto: {nombre_producto}, Stock disponible: {stock_disponible} unidades")
else:
    print("Producto no encontrado")