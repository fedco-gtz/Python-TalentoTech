# |------------------------------------------------------|
# | Ejercicio 1 - Gestión de Inventario con Diccionarios |
# |------------------------------------------------------|

productos = {}

for i in range(3):
    nombre_producto = input(f"Ingrese el nombre del producto {i + 1}: ")
    precio_producto = float(input(f"Ingrese el precio de {nombre_producto}: "))
    productos[nombre_producto] = precio_producto

print("\nLista de productos y precios:")
for producto, precio in productos.items():
    print(f"Producto: {producto}, Precio: {precio}")