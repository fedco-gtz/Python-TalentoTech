# |------------------------------------------------------|
# | Ejercicio 1 - Registro de productos en un inventario |
# |------------------------------------------------------|

inventario = []

print("Registro de productos en el inventario")
while True:
    # Se solicitan los datos del producto a agregar
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }

    inventario.append(producto)

    # Se le pregunta al usuario si quiere seguir agregando productos
    continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
    if continuar != 's':
        break

# Se imprimen todos los productos agregados
print("\n Productos en el inventario:")
for producto in inventario:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
