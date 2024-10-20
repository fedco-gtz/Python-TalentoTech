def mostrar_menu():
    print("Bienvenido al sistema de gestión de inventario")
    print("Por favor selecciona una opción:")
    print("1. Registrar un producto nuevo")
    print("2. Mostrar todos los productos")
    print("3. Actualizar el stock de un producto")
    print("4. Eliminar un producto")
    print("5. Reporte de productos con bajo stock")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input("Ingresa el número de opción: "))
        return opcion
    except ValueError:
        print("Por favor ingresa un número válido.")
        return None

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Registrar un producto nuevo...")

    elif opcion == 2:
        print("Mostrar todos los productos...")

    elif opcion == 3:
        print("Actualizar el stock de un producto...")

    elif opcion == 4:
        print("Eliminar un producto...")

    elif opcion == 5:
        print("Reporte de productos con bajo stock...")

    elif opcion == 6:
        print("Saliendo del sistema...")
    else:
        print("Opción no válida. Por favor elige otra opción.")


while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 6:
        ejecutar_opcion(opcion)
        break
    elif opcion:
        ejecutar_opcion(opcion)
