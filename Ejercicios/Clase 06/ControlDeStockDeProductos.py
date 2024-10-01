# |---------------------------------------------|
# | Ejercicio 1 - Control de stock de productos |
# |---------------------------------------------|

# Se inicia el contador
contador_productos = 0

while True:
    # Se solicita el producto
    producto = input("Ingresá el nombre del producto (o escribí 'salir' para finalizar): ")
    
    # Si el usuario escribe 'salir', se rompe el bucle
    if producto.lower() == 'salir':
        break
    
    # Se solicita el stock de cada producto
    cantidad = int(input(f"Ingresá la cantidad en stock de {producto}: "))
    
    # Acá se incrementa el contador
    contador_productos += 1

# Se muestra la cantidad de productos ingresados
print(f"Total de productos ingresados: {contador_productos}")
