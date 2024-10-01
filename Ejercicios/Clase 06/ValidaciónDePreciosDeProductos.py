# |--------------------------------------------------|
# | Ejercicio 2 - Validación de precios de productos |
# |--------------------------------------------------|

# Inicializamos el precio
precio = -1

# Bucle para pedir un precio válido
while precio <= 0:
    try:
        # El usuario debe ingresar el precio del producto
        precio = float(input("Ingresá el precio del producto (debe ser mayor a 0): "))
        
        # Si el precio es inválido, mostramos un mensaje de error
        if precio <= 0:
            print("Error: El precio debe ser mayor a 0. Intentá de nuevo.")
    
    except ValueError:
        # Si se ingresa un valor que no es un número arroja este error
        print("Error: Ingresá un valor numérico válido.")

# Mostramos el precio aceptado
print(f"El precio aceptado es: {precio}")
