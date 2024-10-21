# |-----------------------------------------------------------|
# | Ejercicio 2 - Mostrar los códigos de productos ingresados |
# |-----------------------------------------------------------|

codigos_productos = []

# Se solicita al usuario que ingrese los códigos de 4 productos
for i in range(1, 5):
    codigo = input(f"Ingresá el código del producto {i}: ")
    codigos_productos.append(codigo)

# Se muestran códigos junto con su posición
print("\nLos códigos ingresados son:")
for i in range(len(codigos_productos)):
    print(f"Producto {i + 1}: {codigos_productos[i]}")
