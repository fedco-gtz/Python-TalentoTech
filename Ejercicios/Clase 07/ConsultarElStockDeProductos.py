# |-----------------------------------------------|
# | Ejercicio 2 - Consultar el stock de productos |
# |-----------------------------------------------|

productos_en_stock = ['mate', 'café', 'harina', 'palmitos', 'yerba', 'mermelada', 'cacao', 'picadillo', 'paté', 'caballa', 'arroz', 'arvejas', 'sardinas', 'atún', 'choclo', 'lentejas']

print("Consulta de productos en el inventario")

# Bucle para permitir consultas múltiples
continuar = True

while continuar:
    # Solicitar al usuario el nombre del producto a consultar
    producto_a_consultar = input("Ingrese el nombre del producto que desea consultar: ").lower()

    # Variable para controlar si se encuentra el producto
    encontrado = False
    index = 0

    # Bucle para recorrer la lista y verificar si el producto está en stock
    while index < len(productos_en_stock):
        if productos_en_stock[index] == producto_a_consultar:
            encontrado = True
            break
        index += 1

    # Mostrar el resultado de la consulta
    if encontrado:
        print(f"El producto '{producto_a_consultar}' está en stock.")
    else:
        print(f"El producto '{producto_a_consultar}' no está disponible.")

    # Preguntar si desea realizar otra consulta
    respuesta = input("¿Desea consultar otro producto? (s/n): ").lower()
    if respuesta != 's':
        continuar = False

print("Gracias por usar el sistema de consulta de productos.")
