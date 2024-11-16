# |------------------------------------------------------|
# | Ejercicio 1 - Registro de productos con validaciones |
# |------------------------------------------------------| 

def registrar_producto():
    inventario = []
    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' para finalizar): ").strip()
        if nombre.lower() == "salir":
            break

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de productos: "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser un número mayor que 0.")
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")

        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio > 0:
                    break
                else:
                    print("El precio debe ser un número mayor que 0.")
            except ValueError:
                print("Por favor, ingrese un número válido para el precio.")

        producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        inventario.append(producto)
        print(f"Producto '{nombre}' registrado correctamente.\n")

    print("\nInventario final:")
    for prod in inventario:
        print(f"Nombre: {prod['nombre']}, Cantidad: {prod['cantidad']}, Precio: ${prod['precio']:.2f}")

registrar_producto()
