# |-------------------------------------------------------------------|
# | Ejercicio 2 - Actualizacion del inventario a partir de un arreglo |
# |-------------------------------------------------------------------|

productos = [
    {'codigo': '001', 'descripcion': 'Producto 1', 'stock': 10},
    {'codigo': '002', 'descripcion': 'Producto 2', 'stock': 5},
    {'codigo': '003', 'descripcion': 'Producto 3', 'stock': 8}
]

def actualizar_inventario():
    codigo = input("Ingrese el código del producto: ")
    producto_encontrado = None
    
    for producto in productos:
        if producto['codigo'] == codigo:
            producto_encontrado = producto
            break
    
    if producto_encontrado:
        cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto_encontrado['descripcion']}: "))
        if cantidad_vendida > 0 and cantidad_vendida <= producto_encontrado['stock']:
            producto_encontrado['stock'] -= cantidad_vendida
            print(f"Stock actualizado. Nuevo stock de {producto_encontrado['descripcion']}: {producto_encontrado['stock']}")
        else:
            print("Cantidad vendida inválida.")
    else:
        print("Producto no encontrado.")

actualizar_inventario()
