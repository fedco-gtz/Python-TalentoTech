# |-----------------------------------|
# | Ejercicio 1 - Ticket de la Compra |
# |-----------------------------------|

# Función para calcular el IVA
def calcular_iva(precio_unitario, cantidad, iva=0.21):
    total_sin_iva = precio_unitario * cantidad
    monto_iva = total_sin_iva * iva
    return monto_iva, total_sin_iva + monto_iva

# Listas para almacenar los datos de los productos
productos = []

# Solicitar datos de tres productos
for i in range(1, 4):
    print(f"\nProducto {i}:")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    valor_unitario = float(input("Valor unitario: "))
    
    # Calcular IVA y el total con IVA
    iva, total_con_iva = calcular_iva(valor_unitario, cantidad)
    
    # Agregar producto al ticket
    productos.append({
        'nombre': nombre,
        'cantidad': cantidad,
        'valor_unitario': valor_unitario,
        'iva': iva,
        'total_con_iva': total_con_iva
    })

# Mostrar ticket
print("\n----- TICKET DE COMPRA -----")
total_final = 0
for producto in productos:
    print(f"Producto: {producto['nombre']}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Valor Unitario: ${producto['valor_unitario']:.2f}")
    print(f"IVA (21%): ${producto['iva']:.2f}")
    print(f"Total con IVA: ${producto['total_con_iva']:.2f}")
    print("------------------------------")
    total_final += producto['total_con_iva']

print(f"TOTAL A PAGAR: ${total_final:.2f}")
