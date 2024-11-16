# |--------------------------------------------------------|
# | Ejercicio 2 - Visualización personalizada de productos |
# |--------------------------------------------------------|

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

        codigo = len(inventario) + 1
        producto = {"codigo": codigo, "nombre": nombre, "cantidad": cantidad, "precio": precio}
        inventario.append(producto)
        print(f"Producto '{nombre}' registrado correctamente con código {codigo}.\n")

    return inventario


def simular_venta(inventario):
    while True:
        try:
            codigo = int(input("Ingrese el código del producto a vender (o 0 para salir): "))
            if codigo == 0:
                break

            producto = next((p for p in inventario if p["codigo"] == codigo), None)
            if not producto:
                print("El código ingresado no corresponde a ningún producto.")
                continue

            print(f"Producto seleccionado: {producto['nombre']}, Stock actual: {producto['cantidad']}")
            cantidad_a_vender = int(input("Ingrese la cantidad a vender: "))

            if cantidad_a_vender <= 0:
                print("La cantidad a vender debe ser mayor que 0.")
            elif cantidad_a_vender > producto["cantidad"]:
                print("Error: No hay suficiente stock disponible.")
            else:
                producto["cantidad"] -= cantidad_a_vender
                print(f"Venta exitosa. Quedan {producto['cantidad']} unidades de '{producto['nombre']}'.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.")


# Programa principal
inventario = registrar_producto()

print("\nInventario inicial:")
for prod in inventario:
    print(f"Código: {prod['codigo']}, Nombre: {prod['nombre']}, Cantidad: {prod['cantidad']}, Precio: ${prod['precio']:.2f}")

print("\n--- Simulación de ventas ---")
simular_venta(inventario)

print("\nInventario final:")
for prod in inventario:
    print(f"Código: {prod['codigo']}, Nombre: {prod['nombre']}, Cantidad: {prod['cantidad']}, Precio: ${prod['precio']:.2f}")
