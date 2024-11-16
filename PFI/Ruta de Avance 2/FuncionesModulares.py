# Lista de productos
productos = []

# Funciones de menú y entrada de opciones
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

# Función principal para ejecutar opciones del menú
def ejecutar_opcion(opcion):
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        actualizar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        reporte_bajo_stock()
    elif opcion == 6:
        print("Saliendo del sistema...")
    else:
        print("Opción no válida. Por favor elige otra opción.")

# Funciones modulares
def agregar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = input("Ingresa la cantidad del producto: ")
    
    try:
        cantidad = int(cantidad)
        productos.append({"nombre": nombre, "cantidad": cantidad})
        print(f"Producto '{nombre}' registrado con cantidad {cantidad}.")
    except ValueError:
        print("Por favor, ingresa una cantidad válida.")

def mostrar_productos():
    if productos:
        print("Productos registrados:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos registrados.")

def actualizar_producto():
    nombre = input("Ingresa el nombre del producto que deseas actualizar: ")
    encontrado = False
    for producto in productos:
        if producto['nombre'] == nombre:
            try:
                nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                producto['cantidad'] = nueva_cantidad
                print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
                encontrado = True
                break
            except ValueError:
                print("Por favor, ingresa una cantidad válida.")
    if not encontrado:
        print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    nombre = input("Ingresa el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def reporte_bajo_stock():
    limite_stock = 5 
    bajo_stock = [producto for producto in productos if producto['cantidad'] < limite_stock]
    
    if bajo_stock:
        print("Productos con bajo stock:")
        for producto in bajo_stock:
            print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos con bajo stock.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 6:
        ejecutar_opcion(opcion)
        break
    elif opcion:
        ejecutar_opcion(opcion)
