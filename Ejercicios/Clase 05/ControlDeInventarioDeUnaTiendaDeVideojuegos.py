# |------------------------------------------------------------------|
# | Ejercicio 1 - Control de inventario de una tienda de videojuegos |
# |------------------------------------------------------------------|

# Función para verificar el stock
def verificar_stock(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return True
    else:
        return False

# Definir el stock mínimo requerido
stock_minimo = 10

# Solicitar el stock actual al usuario
stock_actual = int(input("Ingrese la cantidad actual en stock: "))

# Verificar si es necesario reponer stock
if verificar_stock(stock_actual, stock_minimo):
    print("Es necesario hacer un nuevo pedido. El stock es insuficiente.")
else:
    print("El stock es suficiente, no es necesario hacer un pedido.")
